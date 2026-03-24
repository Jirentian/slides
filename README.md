# Style Prompt Studio

> Generate multi-style PPT slides with AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Core Capabilities

* **Expert at transforming complex professional knowledge into digestible content**

* **Deep search platform upvoted notes** - Quickly extract viral content logic

* **Skilled in summarization and analogies** - Make complex topics accessible

* **Visual-first approach** - Leverage graphics for better comprehension

* **Data-driven strategy** - Include specific numbers in each module when needed

* **Golden quotes summary** - Highlight key takeaways when necessary

---

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install requests
```

### 2. Set API Key

Get your 302.ai API Key: https://app.inference.sh/settings/keys

```bash
export API_KEY="sk-your-api-key-here"
```

### 3. Generate Slides

```bash
# Generate YC intro demo (11 styles, 22 images)
python demos/yc-intro/generate.py

# Generate custom slides
python scripts/generate.py -t "Your Title" -s "Subtitle" --style all
```

---

## Supported Styles (11 Total)

| Style | Description | Best For |
|-------|-------------|----------|
| Retro Pop Art | 70s magazine aesthetic | Creative showcases |
| Minimalist Clean | Clean corporate look | Business presentations |
| Cyberpunk Neon | Dark futuristic theme | Tech topics |
| Neo-Brutalism | Bold raw design | Artistic expression |
| Acid Graphics Y2K | Metallic chrome Y2K | Trendy content |
| Modern Minimal Pop | Instagram pastel | Social media |
| Swiss International | Swiss design | Professional decks |
| Dark Editorial | NYT review style | Deep analysis |
| Design Blueprint | Figma doc style | Technical docs |
| Neo-Brutalist UI | Dashboard UI | SaaS products |
| Y2K Pixel Retro | 90s pixel art | Nostalgic themes |

---

## PPT Generation Best Practices

### Content Guidelines

1. **Title**: Keep it under 8 words, bold and clear
2. **Subtitle**: One line explanation, max 12 words
3. **Key Stats**: 3-5 data points maximum
4. **Visual Balance**: Leave 30% whitespace
5. **Font Hierarchy**: Title > Subtitle > Stats > Decorations

### Recommended API Settings

```bash
# Use nanobanana2 2K for best quality
Model: gemini-3.1-flash-image-preview
Resolution: 2048*1152 (2K 16:9) or higher
Format: PNG for transparency support
```

### Prompt Structure

```
[Style] PPT slide, [aesthetic description],
Title: [your title],
Subtitle: [your subtitle],
Key data: [stat1, stat2, stat3],
[Color palette],
[Decorative elements],
Professional presentation design, 16:9
```

---

## Project Structure

```
slides/
├── README.md                 # This file
├── styles/                   # Style configurations (JSON)
│   ├── retro-pop.json
│   ├── minimal.json
│   ├── cyberpunk.json
│   └── ...
├── demos/
│   └── yc-intro/             # YC Demo
│       ├── generate.py       # Demo generator
│       ├── SHOWCASE.md       # Visual showcase
│       └── images/           # Generated images
└── scripts/
    └── generate.py           # Main generator
```

---

## API Reference

### Using nanobanana2 (Recommended for 2K+)

```python
import requests

API_KEY = "sk-your-api-key"
prompt = "Your design prompt here"

# Note: Use nanobanana2 for 2K+ quality
response = requests.post(
    "https://api.302.ai/google/v1/models/gemini-3.1-flash-image-preview:predict",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "16:9"}
        }
    }
)
```

### Using Seedream 4.0 (Alternative)

```python
response = requests.post(
    "https://api.302.ai/ws/api/v3/bytedance/seedream-v4",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "prompt": prompt,
        "size": "1920*1080",  # Or 3840*2160 for 4K
        "enable_base64_output": True,
        "enable_sync_mode": True
    }
)
```

---

## Examples

View all 11 style examples in [demos/yc-intro/SHOWCASE.md](demos/yc-intro/SHOWCASE.md)

---

## Tips for Better Results

1. **Be specific with style descriptors** - "thick black outlines" vs "bold lines"
2. **Include aspect ratio** - Always specify "16:9" for PPT
3. **Limit text in prompts** - AI struggles with long text
4. **Use color names + hex codes** - "salmon pink #FF6B6B"
5. **Iterate on prompts** - Small tweaks yield different results

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

## Links

- **GitHub**: https://github.com/AAAAAAAJ/slides
- **302.ai**: https://302.ai/
- **API Docs**: https://doc.302.ai/
