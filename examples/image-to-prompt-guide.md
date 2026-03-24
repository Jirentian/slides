# Image to Prompt - 快速使用指南

## 在线工作流（推荐）

当你有一张图片想要反推风格时，按以下步骤操作：

### 步骤 1：取色

使用在线工具快速提取配色：
- [Image Color Picker](https://imagecolorpicker.com/)
- [Coolors Image Picker](https://coolors.co/image-picker)

上传你的图片，获取 HEX 色值列表。

### 步骤 2：分析版式

回答以下问题：
1. **画布比例**：16:9 / 4:3 / 1:1 / 其他
2. **视觉重心**：中心 / 左上 / 黄金分割
3. **主要元素**：圆环图 / 条形图 / 卡片 / 图标
4. **装饰风格**：几何图形 / 线条 / 点阵

### 步骤 3：生成 Prompt

使用以下模板，填入你的分析结果：

```
Retro pop art style, 1970s aesthetic,
flat design with thick black outlines,
background: [背景色 HEX],
accent colors: [配色 1] [配色 2] [配色 3],
[布局描述：centered / grid / asymmetric],
[元素描述：donut charts / cards / icons],
geometric decorative elements,
no gradients, no shadows,
--ar [比例] --style raw
```

---

## 本地工作流

### 前提条件

```bash
# 安装依赖
pip install -r requirements.txt
```

### 使用方法

```bash
# 提取配色
python scripts/extract-colors.py path/to/image.png

# 提取配色并生成 Prompt
python scripts/extract-colors.py path/to/image.png --prompt
```

### 输出示例

```json
{
  "source": "path/to/image.png",
  "background": "#F5F0E6",
  "palette": ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6BCB77"],
  "analysis": {
    "style_suggestion": "retro-pop-art",
    "color_harmony": "analogous"
  }
}
```

---

## 风格参考表

### 识别特征

| 特征 | Retro Pop | Neo-Brutalism | Minimalist |
|------|-----------|---------------|------------|
| 描边 | 2-4px 黑边 | 4px+ 黑边 | 无/极细 |
| 色彩 | 高饱和 | 原色 | 低饱和 |
| 阴影 | 无 | 硬阴影 | 软阴影 |
| 纹理 | 无 | 可能有 | 无 |

### Prompt 关键词

```
Retro Pop Art:
- 1970s aesthetic
- flat design
- thick black outlines
- geometric decorations
- high saturation

Neo-Brutalism:
- brutalist
- raw design
- harsh shadows
- bold typography
- stark contrast

Minimalist:
- clean
- subtle
- soft shadows
- muted colors
- whitespace
```

---

## 案例模板

### 案例 1：知识卡片反推

**原图描述**：讲解"习惯养成"的知识卡片，有 3 个步骤圆圈

**反推结果**：

```json
{
  "background": "#FFF8E7",
  "palette": ["#FF6B6B", "#4ECDC4", "#95E1D3"],
  "layout": "vertical-center",
  "elements": ["numbered-circles", "divider-lines", "icons"]
}
```

**生成 Prompt**：

```
Retro pop art educational card,
explaining habit formation,
cream background #FFF8E7,
three numbered circles in salmon #FF6B6B,
step-by-step vertical layout,
divider lines between sections,
minimal icons,
thick black outlines 2px,
--ar 4:5 --style raw
```

### 案例 2：数据图表反推

**原图描述**：销售数据对比，柱状图 + 关键指标卡

**反推结果**：

```json
{
  "background": "#F5F0E6",
  "palette": ["#E63946", "#457B9D", "#FFB703"],
  "layout": "grid-2-column",
  "elements": ["bar-chart", "kpi-cards", "trend-arrows"]
}
```

**生成 Prompt**：

```
Retro pop art data visualization slide,
sales comparison chart,
cream background #F5F0E6,
bar chart in red #E63946,
KPI cards with big numbers,
trend arrows up/down,
2-column grid layout,
thick black outlines,
--ar 16:9 --style raw
```

---

## 检查清单

反推完成后确认：

- [ ] 已提取背景色
- [ ] 已提取至少 4 个主色
- [ ] 已识别布局类型
- [ ] 已列出主要元素
- [ ] 已估算描边粗细
- [ ] 已生成正向 Prompt
- [ ] 已生成负面 Prompt

---

## 分享到 GitHub

完成反推后，欢迎将案例贡献到项目：

```bash
# 创建案例目录
mkdir -p examples/case-[编号]

# 保存原图和反推结果
cp image.png examples/case-[编号]/original.png
vim examples/case-[编号]/analysis.md

# 提交
git add examples/case-[编号]
git commit -m "Add case [编号]: [主题]"
git push
```
