#!/usr/bin/env python3
"""
YC Introduction Demo - Generate all 11 styles
Uses 302.ai nanobanana2 (gemini-3.1-flash-image-preview) for 2K+ quality
"""

import os
import requests
import base64
from pathlib import Path
import time

API_KEY = os.getenv("API_KEY", "")
API_BASE = "https://api.302.ai"
MODEL_ENDPOINT = "google/v1/models/gemini-3.1-flash-image-preview:predict"

OUTPUT_DIR = Path(__file__).parent / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

STYLES = [
    {"name": "01-retro-pop", "display": "Retro Pop Art",
     "prompt_en": "Retro pop art style PPT slide, 1970s magazine aesthetic, flat design with thick black outlines, cream beige background, Large title: What is Y Combinator, Subtitle: Startup Accelerator, Stats: 2005, 4000+ companies, $600B valuation, Salmon pink sky blue mustard yellow mint green accents, Geometric decorations, Bold typography, Professional presentation, 16:9",
     "prompt_cn": "复古波普艺术风格 PPT 幻灯片，70 年代杂志美学，平涂设计配粗黑边框，米色背景，大标题：什么是 Y Combinator，副标题：创业加速器，数据：2005 年、4000+ 公司、$600B 估值，鲑鱼粉天空蓝芥末黄薄荷绿配色，几何装饰，粗体字体，专业演示文稿，16:9"},

    {"name": "02-minimal", "display": "Minimalist Clean",
     "prompt_en": "Minimalist clean design PPT slide, White background, generous whitespace, Title: What is Y Combinator, Subtitle: Startup Accelerator, Stats: 2005, 4000+, $600B, Subtle gray blue accents, Thin elegant lines, Helvetica font, Professional corporate presentation, 16:9",
     "prompt_cn": "极简主义设计 PPT 幻灯片，白色背景，大量留白，标题：什么是 Y Combinator，副标题：创业加速器，数据：2005、4000+、$600B，微妙灰色蓝色点缀，细雅线条，Helvetica 字体，专业企业幻灯片，16:9"},

    {"name": "03-cyberpunk", "display": "Cyberpunk Neon",
     "prompt_en": "Cyberpunk neon style PPT slide, Dark background, Title: What is Y Combinator with neon glow, Subtitle: Startup Accelerator, Neon colors magenta cyan yellow, Tech grid patterns, holographic panels, glow effects, Futuristic UI, Digital presentation, 16:9",
     "prompt_cn": "赛博朋克霓虹风格 PPT 幻灯片，深色背景，标题：什么是 Y Combinator 配霓虹发光，副标题：创业加速器，霓虹配色品红青色黄色，科技网格图案，全息面板，发光效果，未来主义 UI，数字化演示，16:9"},

    {"name": "04-neo-brutalism", "display": "Neo-Brutalism",
     "prompt_en": "Neo-brutalism style PPT slide, raw design, Cream background, Title: What is Y Combinator, Subtitle: Startup Accelerator, Bold primary colors red blue yellow, Thick 4px black outlines, hard shadows, Brutalist frames, bold typography, 16:9",
     "prompt_cn": "新粗野主义风格 PPT 幻灯片，原始设计，奶油色背景，标题：什么是 Y Combinator，副标题：创业加速器，大胆原色红色蓝色黄色，4px 粗黑边框，硬阴影，粗野主义框架，粗体排版，16:9"},

    {"name": "05-acid-graphics", "display": "Acid Graphics Y2K",
     "prompt_en": "Acid graphics Y2K style PPT slide, Light gray background, Title: What is Y Combinator, Subtitle: Startup Accelerator, Metallic chrome elements, holographic accents, Colors purple pink mint gold, Liquid shapes, star sparkles, mesh gradients, Y2K aesthetic, 16:9",
     "prompt_cn": "酸性图形 Y2K 风格 PPT 幻灯片，浅灰背景，标题：什么是 Y Combinator，副标题：创业加速器，金属铬元素，全息点缀，配色紫色粉色薄荷绿金色，液态形状，星形闪光，网格渐变，Y2K 美学，16:9"},

    {"name": "06-modern-minimal-pop", "display": "Modern Minimal Pop",
     "prompt_en": "Modern minimal pop art PPT slide, Instagram aesthetic, Pastel background, Title: What is Y Combinator, Subtitle: Startup Accelerator, Pastel colors mint cream coral purple, Star burst graphics, thin circles, Tilted blocks, Swiss design influence, 16:9",
     "prompt_cn": "现代极简波普艺术 PPT 幻灯片，Instagram 美学，柔和粉彩背景，标题：什么是 Y Combinator，副标题：创业加速器，粉彩色薄荷绿奶油黄珊瑚橙紫色，星爆图形，细圆圈，倾斜色块，瑞士设计影响，16:9"},

    {"name": "07-swiss-international", "display": "Swiss International",
     "prompt_en": "Swiss international style PPT slide, brutalist graphic design, Light gray background, Title: What is Y Combinator, Subtitle: Startup Accelerator, Bold geometric color blocks, diagonal typography, High saturation colors blue green yellow purple pink orange, Helvetica, Asymmetric, 16:9",
     "prompt_cn": "瑞士国际主义风格 PPT 幻灯片，粗野主义平面设计，浅灰背景，标题：什么是 Y Combinator，副标题：创业加速器，大胆几何色块，斜向排版，高饱和度配色蓝绿黄紫粉橙，Helvetica 字体，非对称构图，16:9"},

    {"name": "08-dark-editorial", "display": "Dark Editorial",
     "prompt_en": "Dark editorial PPT slide, New York Times style, Black background with white dot grid, Title: What is Y Combinator, Subtitle: Startup Accelerator, White text, orange accent, Minimalist wireframe, Serif typography, Dramatic negative space, Newspaper aesthetic, 16:9",
     "prompt_cn": "暗黑编辑出版风格 PPT 幻灯片，纽约时报风格，黑色背景配白色点阵网格，标题：什么是 Y Combinator，副标题：创业加速器，白色文字，橙色点缀，极简线框，衬线字体，戏剧性留白，报纸美学，16:9"},

    {"name": "09-design-blueprint", "display": "Design Blueprint",
     "prompt_en": "Design blueprint PPT slide, Figma documentation style, White background with cyan grid lines, Title: What is Y Combinator, Subtitle: Startup Accelerator, Figma selection boxes, Annotation lines, numbered labels, Technical UI mockup, Clean sans-serif, 16:9",
     "prompt_cn": "设计蓝图风格 PPT 幻灯片，Figma 文档风格，白色背景配青色网格线，标题：什么是 Y Combinator，副标题：创业加速器，Figma 选择框，标注线，编号标签，技术 UI 模型，干净无衬线字体，16:9"},

    {"name": "10-neo-brutalist-ui", "display": "Neo-Brutalist UI",
     "prompt_en": "Neo-brutalist UI PPT slide, dashboard interface, Cream background, Title: What is Y Combinator, Subtitle: Startup Accelerator, Pastel panels mint yellow lavender, Thick 3px black outlines, Card-based layout, flat colors, Bold typography, SaaS dashboard, 16:9",
     "prompt_cn": "新粗野主义 UI PPT 幻灯片，仪表板界面，奶油色背景，标题：什么是 Y Combinator，副标题：创业加速器，柔和色板薄荷绿黄色淡紫色，3px 粗黑边框，卡片布局，平涂色彩，粗体排版，SaaS 仪表板，16:9"},

    {"name": "11-y2k-pixel-retro", "display": "Y2K Pixel Retro",
     "prompt_en": "Y2K pixel retro PPT slide, 1990s aesthetic, Dark background with noise texture, Title: What is Y Combinator, Subtitle: Startup Accelerator, Bright colors yellow orange green, Pixel art computer icons, CRT monitor, Isometric tech, Pixel font, Vintage 90s design, 16:9",
     "prompt_cn": "Y2K 像素复古风格 PPT 幻灯片，1990 年代美学，深色背景配噪点纹理，标题：什么是 Y Combinator，副标题：创业加速器，明亮配色黄色橙色绿色，像素艺术电脑图标，CRT 显示器，等距技术，像素字体，复古 90 年代设计，16:9"},
]


def generate_image(prompt, output_path):
    """Generate image using nanobanana2 API"""
    if not API_KEY:
        print("⚠️  API_KEY not set")
        return False

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "16:9"}
        }
    }

    try:
        response = requests.post(f"{API_BASE}/{MODEL_ENDPOINT}", headers=headers, json=payload, timeout=180)
        if response.status_code == 200:
            result = response.json()
            if "candidates" in result:
                for candidate in result.get("candidates", []):
                    if "content" in candidate and "parts" in candidate["content"]:
                        for part in candidate["content"]["parts"]:
                            if "inlineData" in part:
                                with open(output_path, "wb") as f:
                                    f.write(base64.b64decode(part["inlineData"]["data"]))
                                return True
        return False
    except Exception as e:
        print(f"❌ {e}")
        return False


def main():
    if not API_KEY:
        print("⚠️  Set API_KEY: export API_KEY='sk-...'")
        print("   Get key: https://app.inference.sh/settings/keys")
        return

    print("=" * 60)
    print("YC Intro Demo - nanobanana2 2K")
    print("11 Styles × 2 Languages = 22 Images")
    print("=" * 60)

    generated = 0
    failed = 0

    for style in STYLES:
        for lang, prompt in [("en", style["prompt_en"]), ("cn", style["prompt_cn"])]:
            output_path = OUTPUT_DIR / f"{style['name']}-{lang}.png"
            print(f"\n🎨 {style['display']} ({lang})...")
            if generate_image(prompt, output_path):
                print(f"   ✅ {output_path.name}")
                generated += 1
            else:
                print(f"   ❌ Failed")
                failed += 1
            time.sleep(3)

    print(f"\n{'='*60}")
    print(f"Complete! Success: {generated}, Failed: {failed}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
