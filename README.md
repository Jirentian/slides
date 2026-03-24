# Style Prompt Studio

> Generate multi-style PPT slides with AI - Direct prompts for nanobanana2

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Core Capabilities

> **你擅长将复杂专业知识转化为干货内容**

* 🔍 **深度搜索平台高赞笔记** - 快速提炼爆款逻辑
* 📝 **擅长总结和比喻** - 让复杂主题通俗易懂
* 🎨 **多用图形化表现** - 视觉优先，提升理解
* 📊 **数据说话策略** - 每个模块包含具体数字
* 💬 **金句总结** - 必要时展示关键洞察

---

## Quick Start (No Code)

### Step 1: Copy Prompt
从 [PROMPTS.md](PROMPTS.md) 复制任意风格

### Step 2: Customize
替换占位符为你的内容

### Step 3: Generate
粘贴到 **nanobanana2** 生成!

---

## Recommended Settings

| Setting | Value |
|---------|-------|
| **Model** | `gemini-3.1-flash-image-preview` (nanobanana2) |
| **Resolution** | `2048*1152` (2K 16:9) |
| **Aspect Ratio** | `16:9` |

---

## 11 Available Styles

| # | Style | Best For |
|---|-------|----------|
| 1 | 🎨 Retro Pop Art | 创意展示、品牌宣传 |
| 2 | ⚪ Minimalist Clean | 企业汇报、产品介绍 |
| 3 | 🌃 Cyberpunk Neon | 科技主题、未来感 |
| 4 | 🔲 Neo-Brutalism | 个性表达、艺术展示 |
| 5 | 🌈 Acid Graphics Y2K | 潮流内容、年轻受众 |
| 6 | 📱 Modern Minimal Pop | 社交媒体、轻量内容 |
| 7 | 🇨🇭 Swiss International | 专业设计、高端展示 |
| 8 | 🌑 Dark Editorial | 深度内容、评论分析 |
| 9 | 📐 Design Blueprint | 产品文档、技术说明 |
| 10 | 🖥️ Neo-Brutalist UI | 界面展示、SaaS 产品 |
| 11 | 👾 Y2K Pixel Retro | 怀旧主题、创意内容 |

---

## PPT Content Guidelines

### 内容创作原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **标题** | ≤8 单词，粗体清晰 | "What is Y Combinator" |
| **副标题** | ≤12 单词，一行解释 | "The World's Most Famous Startup Accelerator" |
| **关键数据** | 3-5 个数据点，具体数字 | "2005, 4000+ companies, $600B" |
| **视觉平衡** | 留白 30% | - |
| **字体层级** | 标题 > 副标题 > 数据 > 装饰 | - |
| **金句总结** | 必要时展示关键洞察 | "Startups are hard." |

### 图形化表现建议

- 📊 用数据图表代替大段文字
- 🎯 用图标标识关键信息
- 📈 用对比展示突出差异
- 🖼️ 用视觉隐喻解释复杂概念

---

## Example Gallery

### YC Introduction Demo (11 Styles × 2 Languages = 22 Images)

<details>
<summary><b>🎨 Click to view all 11 style examples</b></summary>

#### 1. Retro Pop Art
![Retro Pop](demos/yc-intro/images/01-retro-pop-en.png)

#### 2. Minimalist Clean
![Minimal](demos/yc-intro/images/02-minimal-en.png)

#### 3. Cyberpunk Neon
![Cyberpunk](demos/yc-intro/images/03-cyberpunk-en.png)

#### 4. Neo-Brutalism
![Neo-Brutalism](demos/yc-intro/images/04-neo-brutalism-en.png)

#### 5. Acid Graphics Y2K
![Acid Graphics](demos/yc-intro/images/05-acid-graphics-en.png)

#### 6. Modern Minimal Pop
![Modern Minimal Pop](demos/yc-intro/images/06-modern-minimal-pop-en.png)

#### 7. Swiss International
![Swiss International](demos/yc-intro/images/07-swiss-international-en.png)

#### 8. Dark Editorial
![Dark Editorial](demos/yc-intro/images/08-dark-editorial-en.png)

#### 9. Design Blueprint
![Design Blueprint](demos/yc-intro/images/09-design-blueprint-en.png)

#### 10. Neo-Brutalist UI
![Neo-Brutalist UI](demos/yc-intro/images/10-neo-brutalist-ui-en.png)

#### 11. Y2K Pixel Retro
![Y2K Pixel Retro](demos/yc-intro/images/11-y2k-pixel-retro-en.png)

</details>

---

## Example Usage

### Input Prompt (Retro Pop Style)
```
Retro pop art style PPT slide, 1970s magazine aesthetic, flat design with thick black outlines,
cream beige background,
Title: What is Y Combinator,
Subtitle: Startup Accelerator,
Stats: 2005, 4000+ companies, $600B valuation,
Salmon pink, sky blue, mustard yellow, mint green accents,
Geometric decorations, Bold typography, Professional presentation, 16:9
```

### Just paste this into nanobanana2!

---

## Project Structure

```
slides/
├── README.md           # This file
├── PROMPTS.md          # All 11 style prompts (copy from here)
├── styles/             # Style configurations (JSON)
└── demos/yc-intro/     # Example outputs
    └── images/         # 22 generated samples
```

---

## Full Prompts Reference

See **[PROMPTS.md](PROMPTS.md)** for all 11 style prompts ready to copy-paste.

---

## Tips for Best Results

1. **Be specific** - "thick black outlines" works better than "bold lines"
2. **Always specify 16:9** - For PPT format
3. **Limit text** - AI handles short text better
4. **Use color names + hex** - "salmon pink #FF6B6B"
5. **Iterate** - Small prompt tweaks = different results

---

## Links

- **GitHub**: https://github.com/AAAAAAAJ/slides
- **302.ai**: https://302.ai/
- **API Docs**: https://doc.302.ai/

---

## License

MIT License - See [LICENSE](LICENSE) for details
