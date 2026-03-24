# 风格反推指南

当你看到一张喜欢的图片，想要反推并生成类似风格时，使用这个指南。

---

## 快速开始

### 方法 1：一键反推（推荐）

```bash
python scripts/extract-style.py path/to/image.png --prompt
```

**输出包含：**
- 提取的配色方案
- 风格特征分析
- 版式分析
- 可直接使用的 AI 绘图 Prompt

### 方法 2：手动分析

使用在线工具逐步分析：

1. **取色**：[imagecolorpicker.com](https://imagecolorpicker.com/)
2. **分析版式**：导入 Figma 或 Photopea
3. **生成 Prompt**：使用下方模板

---

## 风格分析框架

### 1. 色彩分析

提取以下颜色：
- **背景色**：通常是面积最大的颜色
- **主色调**：2-4 个主要强调色
- **对比色**：用于文字和边框的深浅色

```yaml
# 示例输出
colors:
  background: "#F5F0E6"
  palette:
    - "#FF6B6B"  # 主色
    - "#4ECDC4"  # 辅助色
    - "#FFD93D"  # 强调色
    - "#6BCB77"  # 成功色
```

### 2. 版式分析

检查项目：
- **画布比例**：16:9 / 4:3 / 1:1 / 4:5
- **网格类型**：对称 / 不对称 / 自由
- **视觉重心**：中心 / 左上 / 黄金分割
- **边距**：宽松 (>100px) / 标准 (60-80px) / 紧凑 (<40px)

### 3. 元素分析

识别视觉元素：

| 类别 | 检查项 |
|------|--------|
| 描边 | 无 / 细 (1px) / 中 (2px) / 粗 (3px+) |
| 填充 | 纯色 / 渐变 / 纹理 / 金属 |
| 装饰 | 几何图形 / 线条 / 点阵 / 波浪 |
| 阴影 | 无 / 硬阴影 / 软阴影 / 彩色阴影 |
| 特效 | 无 / 发光 / 模糊 / 扭曲 |

### 4. 风格分类

根据特征自动归类：

| 特征组合 | 风格类型 |
|----------|----------|
| 厚边框 + 高饱和 + 几何图形 | Retro Pop Art |
| 留白 + 细线 + 低饱和 | Minimalist |
| 深色背景 + 霓虹色 + 发光 | Cyberpunk |
| 粗体字 + 原色 + 硬阴影 | Neo-Brutalism |
| 金属色 + 液态形状 + Y2K | Acid Graphics |

---

## Prompt 生成模板

### 通用模板

```
[风格类型] style, [风格描述],
background: [背景色],
accent colors: [配色列表],
[布局描述],
[元素特征],
[质感描述],
--ar [比例] --style [raw/natural]
```

### 风格特定模板

#### Retro Pop Art
```
Retro pop art style, 1970s aesthetic,
flat design with thick 3px black outlines,
background: #F5F0E6,
accent colors: #FF6B6B #4ECDC4 #FFD93D #6BCB77,
geometric decorative elements,
clean grid layout,
no gradients, no shadows,
--ar 16:9 --style raw
```

#### Minimalist
```
Minimalist design, clean aesthetic,
white background #FFFFFF,
subtle shadows,
#343A40 #007BFF accent colors,
thin 1px lines,
sans-serif typography,
generous whitespace,
--ar 16:9 --style raw
```

#### Cyberpunk
```
Cyberpunk style, neon lights,
dark background #0D0D1A,
vibrant colors #FF00FF #00FFFF #FFFF00,
glow effects, tech grids,
futuristic UI elements,
scanlines, holographic accents,
--ar 16:9 --style raw --q 2
```

#### Neo-Brutalism
```
Neo-brutalism style, raw design,
bold typography,
#FFF8E7 background,
primary colors #FF4D4D #4D94FF #FFD93D,
thick 4px black outlines,
hard shadows, stark contrast,
--ar 16:9 --style raw
```

#### Acid Graphics
```
Acid graphics style, Y2K aesthetic,
metallic chrome elements,
#E8E8E8 background,
#B185FF #FF6EC7 #7BFFCB colors,
liquid shapes, holographic accents,
mesh gradients, star sparkles,
--ar 16:9 --style raw --v 6
```

---

## 实战案例

### 案例：反推知识卡片

**原图**：一张讲解"习惯养成"的小红书笔记

**步骤 1：提取配色**
```bash
python scripts/extract-style.py habit-card.png
```

**步骤 2：查看分析结果**
```json
{
  "style_name": "habit-card",
  "colors": {
    "background": "#FFF8F0",
    "palette": ["#FF8E72", "#4ECDC4", "#FFE66D"]
  },
  "characteristics": {
    "style_type": "soft-pop",
    "mood": "friendly"
  },
  "layout": {
    "format": "4:5 portrait",
    "symmetry": "symmetric"
  }
}
```

**步骤 3：生成 Prompt**
```
Soft pop art style, friendly colors,
rounded shapes, approachable design,
background: #FFF8F0,
accent colors: #FF8E72 #4ECDC4 #FFE66D,
4:5 portrait layout,
symmetric composition,
--ar 4:5 --style raw
```

---

## 保存你的风格

反推成功后，保存为 JSON 文件方便复用：

```json
{
  "name": "your-style-name",
  "display_name": "显示名称",
  "description": "风格描述",
  "colors": {
    "background": "#HEX",
    "palette": ["#HEX1", "#HEX2", "#HEX3"]
  },
  "layout": {
    "grid": "描述",
    "margins": "80px",
    "focus": "center"
  },
  "elements": ["元素列表"],
  "prompt_template": "Prompt 模板",
  "negative_prompt": "负面提示词"
}
```

保存到 `styles/your-style.json`

---

## 贡献风格到项目

欢迎分享你反推的风格！

1. 将风格保存为 `styles/your-style.json`
2. 添加示例图片到 `examples/cases/`
3. 提交 Pull Request

格式参考现有风格文件。

---

## 工具推荐

### 在线工具
- [Image Color Picker](https://imagecolorpicker.com/) - 取色
- [Coolors](https://coolors.co/) - 配色生成
- [Figma](https://figma.com) - 版式分析

### AI 工具
- Midjourney - 图像生成
- Stable Diffusion - 本地部署
- Claude - 内容生成

---

## 常见问题

**Q: 提取的颜色不准确怎么办？**
A: 尝试调整 `--colors` 参数，如 `--colors 8` 提取更多颜色。

**Q: 生成的 Prompt 效果不好？**
A: 检查风格识别是否正确，可以手动调整 prompt_template。

**Q: 如何批量处理多张图片？**
A: 使用循环脚本：
```bash
for img in images/*.png; do
  python extract-style.py "$img" --output "styles/$(basename "$img" .png).json"
done
```
