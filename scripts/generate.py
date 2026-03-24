#!/usr/bin/env python3
"""
PPT Slide Generator - Generate slides in 11 different styles
Uses 302.ai nanobanana2 (gemini-3.1-flash-image-preview) for 2K+ quality

Usage:
  python scripts/generate.py -t "Your Title" -s "Subtitle" --style all
"""

import os
import sys
import json
import requests
import base64
import argparse
from pathlib import Path
from datetime import datetime

# API Configuration
API_KEY = os.getenv("API_KEY", "")
API_BASE = "https://api.302.ai"

# Use nanobanana2 for 2K+ quality
MODEL_ENDPOINT = "google/v1/models/gemini-3.1-flash-image-preview:predict"

# 11 Style templates
STYLE_TEMPLATES = {
    "retro-pop": {
        "name": "Retro Pop Art",
        "prompt": "Retro pop art style PPT slide, 1970s magazine aesthetic, flat design with thick black outlines, cream beige background, {title}, {subtitle}, {stats}, Salmon pink, sky blue, mustard yellow, mint green accents, Geometric decorations, Bold sans-serif typography, Professional presentation design, 16:9",
    },
    "minimal": {
        "name": "Minimalist Clean",
        "prompt": "Minimalist clean design PPT slide, White background, generous whitespace, {title}, {subtitle}, {stats}, Subtle gray and blue accents, Thin elegant lines, Inter Helvetica font, Professional corporate presentation, Simple elegant layout, 16:9",
    },
    "cyberpunk": {
        "name": "Cyberpunk Neon",
        "prompt": "Cyberpunk neon style PPT slide, Dark charcoal background, {title} with neon glow, {subtitle}, Neon colors: magenta cyan yellow, Tech grid patterns, circuit decorations, Holographic data panels, glow effects, Futuristic UI elements, Digital presentation, 16:9",
    },
    "neo-brutalism": {
        "name": "Neo-Brutalism",
        "prompt": "Neo-brutalism style PPT slide, raw design, Cream background, {title}, {subtitle}, Bold primary colors: red blue yellow, Thick 4px black outlines, hard shadows, Brutalist frames, bold typography, Stark contrast, 16:9",
    },
    "acid-graphics": {
        "name": "Acid Graphics Y2K",
        "prompt": "Acid graphics Y2K style PPT slide, Light gray background, {title}, {subtitle}, Metallic chrome elements, holographic accents, Colors: purple pink mint gold, Liquid shapes, star sparkles, mesh gradients, Y2K aesthetic, futuristic design, 16:9",
    },
    "modern-minimal-pop": {
        "name": "Modern Minimal Pop",
        "prompt": "Modern minimal pop art PPT slide, Instagram aesthetic, Pastel background, {title}, {subtitle}, Pastel colors: mint cream coral purple, Star burst graphics, thin line circles, Tilted color blocks, small arrows, Clean sans-serif typography, Swiss design influence, 16:9",
    },
    "swiss-international": {
        "name": "Swiss International",
        "prompt": "Swiss international style PPT slide, brutalist graphic design, Light gray background, {title}, {subtitle}, Bold geometric color blocks, diagonal typography, High saturation colors: blue green yellow purple pink orange, Helvetica font, Asymmetric composition, 16:9",
    },
    "dark-editorial": {
        "name": "Dark Editorial",
        "prompt": "Dark editorial PPT slide, New York Times style, Black background with white dot grid, {title}, {subtitle}, White text, orange accent, Minimalist wireframe illustrations, Serif typography, Dramatic negative space, Newspaper aesthetic, 16:9",
    },
    "design-blueprint": {
        "name": "Design Blueprint",
        "prompt": "Design blueprint PPT slide, Figma documentation style, White background with cyan grid lines, {title}, {subtitle}, Figma selection boxes, Annotation lines, numbered labels, Technical UI mockup, Clean sans-serif font, 16:9",
    },
    "neo-brutalist-ui": {
        "name": "Neo-Brutalist UI",
        "prompt": "Neo-brutalist UI PPT slide, dashboard interface, Cream background, {title}, {subtitle}, Pastel panels: mint yellow lavender, Thick 3px black outlines, Card-based layout, flat colors, Bold typography, stat cards, SaaS dashboard, 16:9",
    },
    "y2k-pixel-retro": {
        "name": "Y2K Pixel Retro",
        "prompt": "Y2K pixel retro PPT slide, 1990s aesthetic, Dark background with noise texture, {title}, {subtitle}, Bright colors: yellow orange green, Pixel art computer icons, CRT monitor graphics, Isometric tech, Pixel font, Vintage 1990s design, 16:9",
    },
}


def generate_image_nanobanana2(prompt_text, output_path, resolution="2048*1152"):
    """Generate image using nanobanana2 (gemini-3.1-flash-image-preview) API"""
    if not API_KEY:
        print("❌ Error: API_KEY not set. Set with: export API_KEY='your-key'")
        return False

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # nanobanana2 expects Gemini format
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_text
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {
                "aspectRatio": "16:9"
            }
        }
    }

    try:
        response = requests.post(
            f"{API_BASE}/{MODEL_ENDPOINT}",
            headers=headers,
            json=payload,
            timeout=180
        )

        if response.status_code == 200:
            result = response.json()

            # Parse Gemini response format
            if "candidates" in result:
                for candidate in result.get("candidates", []):
                    if "content" in candidate:
                        content = candidate["content"]
                        if "parts" in content:
                            for part in content["parts"]:
                                if "inlineData" in part:
                                    img_data = base64.b64decode(part["inlineData"]["data"])
                                    with open(output_path, "wb") as f:
                                        f.write(img_data)
                                    return True

            print(f"   Unexpected response format")
            return False

        print(f"   API Error: {response.status_code}")
        return False

    except Exception as e:
        print(f"   Exception: {e}")
        return False


def generate_slide(title, subtitle, stats, style, output_dir, lang="en"):
    """Generate a single slide in specified style"""
    template = STYLE_TEMPLATES.get(style)
    if not template:
        print(f"❌ Unknown style: {style}")
        return False

    prompt = template["prompt"].format(
        title=title,
        subtitle=subtitle,
        stats=stats
    )

    output_path = output_dir / f"{style}-{lang}.png"

    print(f"🎨 {template['name']} ({lang})...")
    if generate_image_nanobanana2(prompt, output_path):
        print(f"   ✅ {output_path}")
        return True
    else:
        print(f"   ❌ Failed")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate PPT slides in 11 styles using nanobanana2 2K",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all styles with English title
  python scripts/generate.py -t "What is Y Combinator" -s "Startup Accelerator" --stats "2005, 4000+, $600B"

  # Generate single style
  python scripts/generate.py -t "My Topic" --style cyberpunk

  # Generate Chinese only
  python scripts/generate.py -t "我的主题" --lang cn
        """
    )
    parser.add_argument("--title", "-t", required=True, help="Slide title")
    parser.add_argument("--subtitle", "-s", default="", help="Slide subtitle")
    parser.add_argument("--stats", default="", help="Statistics (comma-separated)")
    parser.add_argument("--style", choices=list(STYLE_TEMPLATES.keys()) + ["all"], default="all", help="Style")
    parser.add_argument("--output", "-o", default="./output", help="Output directory")
    parser.add_argument("--lang", choices=["en", "cn", "both"], default="both", help="Language")
    parser.add_argument("--resolution", default="2048*1152", help="Output resolution (default: 2K 16:9)")

    args = parser.parse_args()

    if not API_KEY:
        print("⚠️  Warning: API_KEY not set")
        print("   Get your key: https://app.inference.sh/settings/keys")
        print("   Set with: export API_KEY='sk-...'")
        print()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("PPT Slide Generator - nanobanana2 2K")
    print("=" * 60)
    print(f"Title: {args.title}")
    print(f"Subtitle: {args.subtitle}")
    print(f"Stats: {args.stats}")
    print(f"Styles: {args.style}")
    print(f"Language: {args.lang}")
    print(f"Output: {output_dir}")
    print(f"Resolution: {args.resolution}")
    print("=" * 60)

    styles_to_generate = list(STYLE_TEMPLATES.keys()) if args.style == "all" else [args.style]

    generated = 0
    failed = 0

    for style in styles_to_generate:
        if args.lang in ["en", "both"]:
            if generate_slide(args.title, args.subtitle, args.stats, style, output_dir, "en"):
                generated += 1
            else:
                failed += 1

        if args.lang in ["cn", "both"]:
            if generate_slide(args.title, args.subtitle, args.stats, style, output_dir, "cn"):
                generated += 1
            else:
                failed += 1

        # Rate limiting
        import time
        time.sleep(3)

    print()
    print("=" * 60)
    print(f"Complete! Success: {generated}, Failed: {failed}")
    print("=" * 60)


if __name__ == "__main__":
    main()
