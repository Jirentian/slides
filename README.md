# Style Prompt Studio

> 从任何图片反推风格，生成可复用的 AI 绘图提示词

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 简介

这是一个**通用的风格反推系统**，帮助你：
1. 从喜欢的图片中提取风格（配色、版式、元素、纹理）
2. 生成可复用的 Prompt 模板
3. 批量生成相同风格的视觉内容

不限于任何特定风格 —— 无论是复古波普、极简主义、赛博朋克还是手绘插画，都能反推复用。

---

## 核心功能

### 1. 风格提取

从任意图片中提取 4 个维度的风格信息：

| 维度 | 提取内容 |
|------|----------|
| **色彩** | 背景色、主色调、强调色、对比色 |
| **版式** | 网格类型、边距比例、视觉重心 |
| **元素** | 装饰图形、图标风格、数据可视化类型 |
| **质感** | 描边粗细、填充方式、纹理效果 |

### 2. Prompt 生成

自动将分析结果转换为 AI 绘图 Prompt：
- Midjourney
- Stable Diffusion
- DALL-E 3
- Gemini

### 3. 风格库

建立你的可复用风格库，一键调用：
```bash
# 使用已保存的风格生成新内容
python generate.py --style cyberpunk --topic "AI Trends 2024"
```

---

## 快速开始

### 方法 1：在线工作流（无需安装）

```bash
# 步骤 1：访问在线取色工具
# https://imagecolorpicker.com/ 或 https://coolors.co/image-picker

# 步骤 2：上传你的参考图，获取 HEX 色值

# 步骤 3：使用 Prompt 生成器
# https://aaaaaaaj.github.io/slides/prompt-generator.html
```

### 方法 2：本地工作流

```bash
# 克隆项目
git clone https://github.com/AAAAAAAJ/slides.git
cd slides

# 安装依赖
pip install -r requirements.txt

# 提取风格并生成 Prompt
python scripts/extract-style.py path/to/image.png --prompt
```

---

## 使用示例

### 示例 1：反推复古波普风格

```bash
python scripts/extract-style.py examples/retro-pop.png --prompt
```

**输出：**
```json
{
  "style_name": "retro-pop-art",
  "colors": {
    "background": "#F5F0E6",
    "palette": ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6BCB77"]
  },
  "layout": "12-column-grid",
  "elements": ["thick-outlines", "flat-colors", "geometric-shapes"],
  "texture": "none",
  "prompt": "Retro pop art style, 1970s aesthetic, flat design with thick black outlines..."
}
```

### 示例 2：反推极简风格

```bash
python scripts/extract-style.py examples/minimal.png --prompt
```

**输出：**
```json
{
  "style_name": "minimalist-clean",
  "colors": {
    "background": "#FFFFFF",
    "palette": ["#F8F9FA", "#343A40", "#007BFF"]
  },
  "layout": "whitespace-focused",
  "elements": ["thin-lines", "subtle-shadows", "sans-serif"],
  "texture": "smooth",
  "prompt": "Minimalist design, clean aesthetic, white background, subtle shadows..."
}
```

### 示例 3：反推赛博朋克风格

```bash
python scripts/extract-style.py examples/cyberpunk.png --prompt
```

**输出：**
```json
{
  "style_name": "cyberpunk-neon",
  "colors": {
    "background": "#0D0D1A",
    "palette": ["#FF00FF", "#00FFFF", "#FFFF00", "#FF0080"]
  },
  "layout": "dynamic-asymmetric",
  "elements": ["glow-effects", "neon-lines", "tech-grids"],
  "texture": "scanlines",
  "prompt": "Cyberpunk style, neon lights, dark background with vibrant colors..."
}
```

---

## 预设风格库

项目内置了以下预设风格：

| 风格 | 文件 | 特点 |
|------|------|------|
| 复古波普 | `styles/retro-pop.json` | 厚边框、高饱和、几何图形 |
| 极简主义 | `styles/minimal.json` | 留白、细线、低饱和 |
| 新粗野主义 | `styles/neo-brutalism.json` | 原色、硬阴影、粗体字 |
| 赛博朋克 | `styles/cyberpunk.json` | 霓虹色、深色背景、发光效果 |
| 手绘插画 | `styles/hand-drawn.json` | 不规则线条、水彩质感 |
| 酸性设计 | `styles/acid-graphics.json` | 金属色、液态形状、Y2K |

---

## 项目结构

```
slides/
├── README.md                 # 项目说明
├── prompts/                  # Prompt 模板
│   ├── content-generator.md  # 内容生成
│   ├── style-analyzer.md     # 风格分析框架
│   └── reverse-engineer.md   # 反推指南
├── scripts/
│   ├── extract-style.py      # 风格提取脚本
│   └── generate.py           # 批量生成脚本
├── styles/                   # 预设风格库
│   ├── retro-pop.json
│   ├── minimal.json
│   └── ...
├── templates/                # 版式模板
│   ├── cover.md
│   ├── data.md
│   └── timeline.md
├── examples/                 # 示例
│   └── cases/
└── assets/                   # 素材
```

---

## 风格分析框架

### 色彩维度

```yaml
background:
  type: solid | gradient | texture
  color: "#HEX"

primary_colors:
  - "#HEX1"
  - "#HEX2"
  - "#HEX3"

contrast_method: complementary | analogous | triadic | monochromatic
```

### 版式维度

```yaml
grid:
  type: symmetric | asymmetric | free
  columns: 12
  margins: "80px"

visual_focus: center | top-left | golden-ratio
```

### 元素维度

```yaml
outlines:
  present: true
  width: "2-4px"
  color: "#000000"

fills:
  type: flat | gradient | texture

decorations:
  - geometric_shapes
  - lines
  - dots
  - waves
```

### 质感维度

```yaml
texture: none | noise | halftone | paper | grain
shadows: none | hard | soft | colored
effects: none | glow | blur | distortion
```

---

## 贡献指南

欢迎提交你反推的风格！

1. Fork 本项目
2. 将你的风格保存为 `styles/your-style.json`
3. 添加示例图片到 `examples/cases/`
4. 提交 Pull Request

### 风格 JSON 模板

```json
{
  "name": "your-style-name",
  "display_name": "风格显示名称",
  "description": "风格描述",
  "colors": {
    "background": "#HEX",
    "palette": ["#HEX1", "#HEX2", "#HEX3"]
  },
  "layout": {
    "grid": "description",
    "margins": "80px",
    "focus": "center"
  },
  "elements": ["list", "of", "elements"],
  "texture": "description",
  "prompt_template": "AI prompt template for this style",
  "negative_prompt": "things to avoid"
}
```

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 更新日志

### v2.0.0 - 2024-03-24
- 重构为通用风格反推系统
- 支持多种风格，不局限于复古波普
- 新增风格 JSON 配置格式
- 优化 Prompt 生成逻辑

### v1.0.0 - 初始版本
- 复古波普风格支持
- 基础取色脚本
