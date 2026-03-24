#!/usr/bin/env python3
"""
Style Extractor - Extract style from any image and generate AI prompts
Usage: python scripts/extract-style.py <image_path> [--prompt] [--output json]
"""

import sys
import json
import argparse
from PIL import Image
from collections import Counter
from pathlib import Path


def rgb_to_hex(rgb):
    """Convert RGB tuple to HEX string"""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def hex_to_rgb(hex_color):
    """Convert HEX string to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_brightness(rgb):
    """Calculate perceived brightness of a color"""
    r, g, b = rgb
    return (299 * r + 587 * g + 114 * b) / 1000


def get_color_temperature(rgb):
    """Estimate color temperature (warm/cool/neutral)"""
    r, g, b = rgb
    if r > b + 20:
        return "warm"
    elif b > r + 20:
        return "cool"
    return "neutral"


def quantify_color(rgb, factor=30):
    """Quantize color for grouping similar colors"""
    return tuple(c // factor * factor for c in rgb)


def detect_style_characteristics(colors, image_path=None):
    """
    Detect style characteristics from extracted colors

    Returns characteristics like:
    - style_type: retro-pop, minimal, cyberpunk, etc.
    - saturation_level: high, medium, low
    - contrast_level: high, medium, low
    - color_harmony: analogous, complementary, etc.
    """
    characteristics = {
        "style_type": "unknown",
        "saturation_level": "medium",
        "contrast_level": "medium",
        "color_harmony": "unknown",
        "mood": "neutral"
    }

    if not colors:
        return characteristics

    # Analyze brightness range for contrast
    brightness_values = [get_brightness(c) for c in colors]
    brightness_range = max(brightness_values) - min(brightness_values)

    if brightness_range > 150:
        characteristics["contrast_level"] = "high"
    elif brightness_range < 80:
        characteristics["contrast_level"] = "low"

    # Analyze saturation (simplified - check colorfulness)
    saturation_scores = []
    for color in colors:
        r, g, b = color
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        if max_c == 0:
            saturation_scores.append(0)
        else:
            saturation_scores.append((max_c - min_c) / max_c)

    avg_saturation = sum(saturation_scores) / len(saturation_scores)
    if avg_saturation > 0.6:
        characteristics["saturation_level"] = "high"
    elif avg_saturation < 0.3:
        characteristics["saturation_level"] = "low"

    # Detect style type based on color characteristics
    bg_color = colors[0] if colors else (255, 255, 255)
    bg_brightness = get_brightness(bg_color)

    # Check for dark background (cyberpunk, dark mode)
    if bg_brightness < 80:
        if any(get_brightness(c) > 200 and get_brightness(c) < 255 for c in colors[1:4] if len(colors) > 1):
            characteristics["style_type"] = "cyberpunk-neon"
            characteristics["mood"] = "energetic"
        else:
            characteristics["style_type"] = "dark-minimal"
            characteristics["mood"] = "calm"

    # Check for light background
    elif bg_brightness > 200:
        # Check for vibrant colors (retro pop)
        if characteristics["saturation_level"] == "high" and characteristics["contrast_level"] == "high":
            characteristics["style_type"] = "retro-pop-art"
            characteristics["mood"] = "playful"
        # Check for muted colors (minimal)
        elif characteristics["saturation_level"] == "low":
            characteristics["style_type"] = "minimalist-clean"
            characteristics["mood"] = "calm"
        else:
            characteristics["style_type"] = "soft-pop"
            characteristics["mood"] = "friendly"

    # Medium brightness background
    else:
        if any(c[0] > 200 and c[1] < 100 and c[2] < 100 for c in colors):  # Strong reds
            characteristics["style_type"] = "bold-editorial"
            characteristics["mood"] = "confident"
        else:
            characteristics["style_type"] = "balanced-corporate"
            characteristics["mood"] = "professional"

    # Determine color harmony
    if len(colors) >= 3:
        hues = []
        for c in colors[1:min(4, len(colors))]:  # Skip background
            r, g, b = c
            max_c = max(r, g, b)
            min_c = min(r, g, b)
            if max_c != min_c:
                delta = max_c - min_c
                if r == max_c:
                    h = (g - b) / delta % 6
                elif g == max_c:
                    h = (b - r) / delta + 2
                else:
                    h = (r - g) / delta + 4
                hues.append(h * 60)  # Convert to degrees

        if hues:
            hue_range = max(hues) - min(hues)
            if hue_range < 60 or hue_range > 300:
                characteristics["color_harmony"] = "analogous"
            elif 150 < hue_range < 210:
                characteristics["color_harmony"] = "complementary"
            else:
                characteristics["color_harmony"] = "triadic"

    return characteristics


def estimate_layout(image_path):
    """
    Estimate layout characteristics from image
    """
    try:
        img = Image.open(image_path)
        width, height = img.size

        # Calculate aspect ratio
        aspect_ratio = width / height

        if abs(aspect_ratio - 1.778) < 0.1:  # Close to 16:9
            format_type = "16:9 presentation"
        elif abs(aspect_ratio - 1.333) < 0.1:  # Close to 4:3
            format_type = "4:3 presentation"
        elif abs(aspect_ratio - 1.0) < 0.1:  # Square
            format_type = "1:1 square"
        elif abs(aspect_ratio - 0.8) < 0.1:  # 4:5
            format_type = "4:5 portrait"
        else:
            format_type = "custom"

        # Analyze symmetry (simplified)
        img_resized = img.resize((100, 100)).convert('L')
        pixels = list(img_resized.getdata())

        # Simple symmetry check
        left_sum = sum(pixels[i] for i in range(10000) if i % 100 < 50)
        right_sum = sum(pixels[i] for i in range(10000) if i % 100 >= 50)

        symmetry = "symmetric" if abs(left_sum - right_sum) < 50000 else "asymmetric"

        return {
            "format": format_type,
            "aspect_ratio": round(aspect_ratio, 3),
            "dimensions": f"{width}x{height}",
            "symmetry": symmetry,
            "suggested_grid": "12-column" if aspect_ratio > 1.5 else "8-column"
        }
    except Exception as e:
        return {
            "format": "unknown",
            "error": str(e)
        }


def detect_elements(image_path):
    """
    Detect visual elements in the image (simplified analysis)
    """
    elements = {
        "outlines": {
            "detected": "unknown",
            "estimated_width": "2-3px"
        },
        "fills": "flat",
        "decorations": [],
        "data_viz": []
    }

    # This is a simplified analysis
    # For better detection, you would use computer vision models

    try:
        img = Image.open(image_path).convert('RGB')
        img_small = img.resize((200, 200))

        # Edge detection (simplified - look for high contrast areas)
        pixels = list(img_small.getdata())
        edge_count = 0

        for i in range(len(pixels) - 200):
            current = pixels[i]
            right = pixels[i + 1] if (i + 1) % 200 != 0 else current

            # Check for sharp contrast (potential edge)
            diff = sum(abs(a - b) for a, b in zip(current, right))
            if diff > 150:
                edge_count += 1

        if edge_count > 500:
            elements["outlines"]["detected"] = "thick"
            elements["outlines"]["estimated_width"] = "3-4px"
        elif edge_count > 200:
            elements["outlines"]["detected"] = "medium"
            elements["outlines"]["estimated_width"] = "2px"
        else:
            elements["outlines"]["detected"] = "thin"
            elements["outlines"]["estimated_width"] = "1px"

        # Check for gradient (simplified)
        # Look for smooth color transitions
        gradient_detected = False
        for i in range(0, len(pixels) - 400, 200):
            row_start = pixels[i]
            row_end = pixels[i + 199]
            diff = sum(abs(a - b) for a, b in zip(row_start, row_end))
            if 50 < diff < 200:  # Moderate difference suggests gradient
                gradient_detected = True
                break

        if gradient_detected:
            elements["fills"] = "gradient"
        else:
            elements["fills"] = "flat"

    except Exception as e:
        elements["error"] = str(e)

    return elements


def generate_prompt(style_data):
    """Generate AI image generation prompt from style data"""

    style_type = style_data.get("characteristics", {}).get("style_type", "custom")
    bg_color = style_data["colors"].get("background", "#FFFFFF")
    palette = style_data["colors"].get("palette", [])
    palette_str = " ".join(palette) if palette else ""

    # Style-specific prompts
    style_prompts = {
        "retro-pop-art": "Retro pop art style, 1970s aesthetic, flat design with thick black outlines",
        "minimalist-clean": "Minimalist design, clean aesthetic, subtle shadows, sans-serif typography",
        "cyberpunk-neon": "Cyberpunk style, neon lights, dark background with vibrant colors, glow effects",
        "dark-minimal": "Dark minimalist design, elegant, subtle gradients, premium feel",
        "soft-pop": "Soft pop art style, friendly colors, rounded shapes, approachable design",
        "bold-editorial": "Bold editorial design, high contrast, strong typography, magazine style",
        "balanced-corporate": "Professional corporate design, balanced layout, clean and modern"
    }

    base_prompt = style_prompts.get(style_type, "Professional design, clean layout")

    prompt = f"""## AI Image Generation Prompt

### Positive Prompt
```
{base_prompt},
background: {bg_color},
accent colors: {palette_str},
{style_data['layout'].get('suggested_grid', 'grid layout')},
{style_data['elements']['fills']} color fills,
{style_data['elements']['outlines'].get('estimated_width', '2px')} outlines,
high quality, professional execution,
--ar {style_data['layout'].get('aspect_ratio', '16:9')} --style raw
```

### Negative Prompt
```
gradients, shadows, 3d effects, realistic,
photorealistic, blurry, low contrast,
cluttered layout, thin fonts, amateur design
```

### Style Token
```
{style_type}
```
"""
    return prompt


def extract_style(image_path, num_colors=6):
    """
    Extract complete style from an image

    Args:
        image_path: Path to the image file
        num_colors: Number of colors to extract

    Returns:
        Dictionary with complete style analysis
    """
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    # Resize for faster processing
    img_small = img.resize((100, 100))
    pixels = list(img_small.getdata())

    # Quantize and count colors
    color_counts = Counter()
    for pixel in pixels:
        quantized = quantify_color(pixel)
        color_counts[quantized] += 1

    # Get top colors
    top_colors = color_counts.most_common(num_colors * 2)

    # Filter out very similar colors
    unique_colors = []
    min_distance = 50

    for color, count in top_colors:
        is_unique = True
        for existing, _ in unique_colors:
            distance = sum((a - b) ** 2 for a, b in zip(color, existing))
            if distance < min_distance ** 2:
                is_unique = False
                break
        if is_unique:
            unique_colors.append((color, count))

    # Sort by brightness to identify background
    unique_colors.sort(key=lambda x: get_brightness(x[0]), reverse=True)

    # Identify background and accent colors
    background = unique_colors[0][0] if unique_colors else (255, 255, 255)

    accent_colors = []
    for color, count in unique_colors[1:]:
        brightness = get_brightness(color)
        # Skip very dark colors (likely text) and very bright colors (background variations)
        if 40 < brightness < 230:
            accent_colors.append(color)
        if len(accent_colors) >= num_colors:
            break

    # If we don't have enough colors, sample more
    if len(accent_colors) < num_colors - 1:
        sample_points = [(25, 25), (75, 25), (50, 50), (25, 75), (75, 75)]
        img_sample = img.resize((100, 100))
        for x_pct, y_pct in sample_points:
            if len(accent_colors) >= num_colors - 1:
                break
            x = int(x_pct * img_sample.width / 100)
            y = int(y_pct * img_sample.height / 100)
            color = img_sample.getpixel((x, y))
            brightness = get_brightness(color)

            if 40 < brightness < 230:
                is_duplicate = False
                for existing in accent_colors:
                    distance = sum((a - b) ** 2 for a, b in zip(color, existing))
                    if distance < 30 ** 2:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    accent_colors.append(color)

    # Build style data
    all_colors = [background] + accent_colors
    characteristics = detect_style_characteristics(all_colors, image_path)
    layout = estimate_layout(image_path)
    elements = detect_elements(image_path)

    style_data = {
        "source": str(image_path),
        "colors": {
            "background": rgb_to_hex(background),
            "background_rgb": background,
            "palette": [rgb_to_hex(c) for c in accent_colors],
            "palette_rgb": accent_colors,
            "temperature": get_color_temperature(background)
        },
        "characteristics": characteristics,
        "layout": layout,
        "elements": elements,
    }

    return style_data


def save_style(style_data, output_path):
    """Save style data to JSON file"""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(style_data, f, indent=2)

    print(f"Style saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract style from any image and generate AI prompts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python extract-style.py image.png
  python extract-style.py image.png --prompt
  python extract-style.py image.png --output style.json
  python extract-style.py image.png --prompt --output style.json
        """
    )

    parser.add_argument("image", help="Path to the image file")
    parser.add_argument("--prompt", action="store_true",
                        help="Generate AI image generation prompt")
    parser.add_argument("--output", "-o", help="Save style data to JSON file")
    parser.add_argument("--colors", "-c", type=int, default=6,
                        help="Number of colors to extract (default: 6)")
    parser.add_argument("--format", "-f", choices=["json", "markdown", "both"],
                        default="json", help="Output format (default: json)")

    args = parser.parse_args()

    # Extract style
    style_data = extract_style(args.image, args.colors)

    # Generate style name from filename
    image_name = Path(args.image).stem
    style_data["style_name"] = image_name.replace("_", "-").replace(" ", "-").lower()
    style_data["display_name"] = image_name.replace("-", " ").replace("_", " ").title()

    # Output results
    if args.format in ["json", "both"]:
        print(json.dumps(style_data, indent=2))

    if args.prompt or args.format == "markdown":
        print("\n" + generate_prompt(style_data))

    # Save to file if requested
    if args.output:
        save_style(style_data, args.output)


if __name__ == "__main__":
    main()
