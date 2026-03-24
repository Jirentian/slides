# Image to Prompt - 图像反推系统

## 使用说明

当你有一张复古波普风格的图片想要分析并生成类似风格时，使用此系统。

---

## 反推分析框架

### 第一步：色彩提取

```python
# 使用 Python 提取图片主色
import colorthief
from PIL import Image

def extract_palette(image_path, num_colors=6):
    """提取图片配色方案"""
    img = Image.open(image_path)
    img = img.convert('RGB')

    # 调整大小加速处理
    img = img.resize((150, 150))

    # 提取主色
    color_thief = colorthief.ColorThief(image_path)
    dominant_colors = color_thief.get_palette(num_colors)

    # 转换为 HEX
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)

    return [rgb_to_hex(c) for c in dominant_colors]

# 输出示例
# ['#F5F0E6', '#FF6B6B', '#4ECDC4', '#FFD93D', '#6BCB77', '#000000']
```

### 第二步：版式分析

分析维度清单：

| 维度 | 检查项 | 记录值 |
|------|--------|--------|
| 画布比例 | 16:9 / 4:3 / 1:1 | |
| 网格类型 | 对称/不对称/自由 | |
| 边距比例 | 上/下/左/右 | |
| 视觉重心 | 中心/左上/黄金分割点 | |
| 模块数量 | 独立区域数量 | |

### 第三步：元素识别

```
装饰图形清单：
□ 圆形/椭圆
□ 矩形/方形
□ 三角形
□ 星形
□ 波浪线
□ 箭头
□ 对话气泡
□ 其他：_______

数据可视化类型：
□ 圆环图
□ 条形图
□ 折线图
□ 饼图
□ 信息卡
□ 无

文字层级：
□ 主标题（最醒目）
□ 副标题（次级）
□ 正文（常规）
□ 标注（最小）
```

### 第四步：风格参数

```
描边粗细：___ px (估计值)
填充方式：□ 纯色 □ 渐变 □ 纹理
纹理类型：□ 无 □ 颗粒 □ 半调网点 □ 纸张
色彩饱和度：□ 低 □ 中 □ 高
对比度：□ 柔和 □ 标准 □ 强烈
```

---

## 反推 Prompt 生成器

### 输入模板

```markdown
【原图信息】
- 图片来源：[URL 或本地路径]
- 图片主题：[描述图片内容]
- 喜欢元素：[具体喜欢哪些部分]

【自动分析结果】
配色方案：[从第一步获取的 HEX 列表]
版式类型：[从第二步获取的分析]
包含元素：[从第三步获取的清单]
风格参数：[从第四步获取的参数]

【期望输出】
- 保持风格：是/否
- 修改内容：[需要调整的部分]
- 新主题：[新图片的主题]
```

### 输出模板

```markdown
## 反推风格定义

### Style Token
```
retro-pop-art-v1
```

### Color Palette
```json
{
  "background": "#F5F0E6",
  "primary": "#FF6B6B",
  "secondary": "#4ECDC4",
  "accent": "#FFD93D",
  "success": "#6BCB77",
  "text": "#000000"
}
```

### Layout
- Grid: 12-column symmetric
- Margins: 80px all sides
- Module gap: 24px
- Visual focus: Center-top

### Elements
- Thick outlines: 3px solid black
- Flat color fills only
- Geometric decorations: quarter circles, concentric rings
- Data visualization: donut charts, bar charts
- Typography: bold sans-serif headers

### AI Image Generation Prompt
```
Retro pop art style PPT slide, 1970s aesthetic,
flat design with thick 3px black outlines,
color palette: #F5F0E6 #FF6B6B #4ECDC4 #FFD93D #6BCB77,
cream beige background,
geometric decorative elements,
clean grid layout,
no gradients, no shadows,
high contrast, bold typography,
professional data visualization,
--ar 16:9 --style raw --v 6
```

### Negative Prompt
```
gradients, shadows, 3d effects, realistic,
photorealistic, blurry, low contrast,
pastel colors, neon colors,
cluttered layout, thin fonts
```
```

---

## 自动化脚本

### Python 取色脚本

```python
#!/usr/bin/env python3
"""
提取图片主色并生成 JSON 配色方案
"""

import sys
import json
from PIL import Image
import colorthief
import webcolors

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def get_color_name(rgb):
    """获取颜色的通用名称"""
    try:
        name = webcolors.rgb_to_name(rgb, spec='css3')
        return name
    except ValueError:
        # 计算最近的颜色名称
        min_dist = float('inf')
        closest_name = ''
        for name_hex in webcolors.CSS3_HEX:
            name_rgb = webcolors.hex_to_rgb(name_hex)
            dist = sum((a - b) ** 2 for a, b in zip(rgb, name_rgb))
            if dist < min_dist:
                min_dist = dist
                closest_name = name_hex
        return closest_name.lstrip('#')

def extract_colors(image_path, num_colors=6):
    img = Image.open(image_path)
    img = img.convert('RGB')

    # 提取主色
    color_thief = colorthief.ColorThief(image_path)
    palette = color_thief.get_palette(num_colors)

    # 识别背景色（通常是出现频率最高的浅色）
    img_small = img.resize((50, 50))
    pixels = list(img_small.getdata())

    # 简单统计
    color_count = {}
    for p in pixels:
        # 颜色量化
        q = tuple(c // 20 * 20 for c in p)
        color_count[q] = color_count.get(q, 0) + 1

    # 找到最浅的颜色作为背景
    bg_color = max(color_count.keys(), key=lambda x: sum(x))

    result = {
        "source": image_path,
        "background": rgb_to_hex(bg_color),
        "palette": [rgb_to_hex(c) for c in palette],
        "palette_rgb": palette
    }

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract-colors.py <image_path>")
        sys.exit(1)

    result = extract_colors(sys.argv[1])
    print(json.dumps(result, indent=2))
```

### 使用方法

```bash
# 安装依赖
pip install colorthief pillow webcolors

# 运行取色
python scripts/extract-colors.py path/to/image.png

# 输出 JSON 格式的配色方案
```

---

## 实战案例

### 案例：分析一张知识卡片

**输入图片描述**：
- 一张讲解"复利效应"的知识卡片
- 米色背景，有红色和蓝色的圆环图
- 粗黑边框，黄色高亮标注

**反推输出**：

```markdown
## 风格分析结果

### 配色
- Background: #F5F0E6 (Warm Cream)
- Primary: #E63946 (Red - 用于关键数据)
- Secondary: #457B9D (Blue - 用于对比数据)
- Accent: #FFB703 (Yellow - 用于高亮)
- Text: #1D3557 (Dark Blue-Black)

### 版式
- 类型：中心对称
- 网格：8 列
- 视觉重心：正中

### 元素
- 圆环图 x2
- 粗边框卡片 x1
- 星形标注 x3
- 箭头 x2

### 可复用 Prompt
```
Retro pop art educational card,
explaining compound interest concept,
cream background #F5F0E6,
two donut charts in red #E63946 and blue #457B9D,
thick black outlines 3px,
yellow #FFB703 highlight boxes,
centered layout,
bold typography,
1970s magazine style,
--ar 4:5
```
```

---

## 检查清单

反推完成后，确认以下内容：

- [ ] 配色方案完整（至少 5 色）
- [ ] 背景色明确标注
- [ ] 版式类型已识别
- [ ] 主要装饰元素已列出
- [ ] 描边粗细已估计
- [ ] 生成了可直接使用的 Prompt
- [ ] 包含了负面 Prompt

---

## 工具推荐

### 在线取色工具
- [Image Color Picker](https://imagecolorpicker.com/)
- [Canva Color Palette](https://www.canva.com/colors/color-palette-generator/)
- [Coolors Image Picker](https://coolors.co/image-picker)

### 设计分析工具
- [Figma](https://figma.com) - 导入图片后直接取样分析
- [Photopea](https://photopea.com) - 免费在线 PS 替代品

### AI 工具
- Midjourney / Stable Diffusion - 使用反推 Prompt 生成
- [Clipdrop](https://clipdrop.co) - 图像分析和编辑
