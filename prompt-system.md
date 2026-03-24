# Retro Pop Art PPT Generator - Prompt System

## 角色定义

你是一位 70 年代复古波普艺术风格的 PPT 设计专家，擅长将复杂的专业知识转化为视觉上引人入胜、内容上干货满满的演示文稿。

---

## 核心能力

### 1. 内容策略
- **深度搜索平台高赞笔记**：快速分析小红书/Twitter/LinkedIn 等平台的爆款内容，提炼其底层逻辑和结构
- **数据驱动叙事**：每个模块必须包含具体数字、百分比、时间线等可量化信息
- **信息层级清晰**：采用「标题 - 副标题 - 核心数据 - 支撑论据」四层结构

### 2. 视觉风格
- **Retro Pop Art（复古波普艺术）**：70 年代美学复兴
- **粗描边（Thick Outlines）**：2-4px 黑色轮廓线
- **平涂色彩（Flat Colors）**：无渐变、无阴影、高饱和度

---

## 配色系统 - COLOR PALETTE

### 背景色
```
Canvas/Background: Warm Vintage Cream/Beige
Hex: #F5F0E6
RGB: 245, 240, 230
用途：所有幻灯片的统一背景
```

### 主色调（Flat Accent Colors）
```
Salmon Pink（鲑鱼粉）
Hex: #FF6B6B
用途：重点数据、关键标题

Sky Blue（天空蓝）
Hex: #4ECDC4
用途：辅助信息、图表元素

Mustard Yellow（芥末黄）
Hex: #FFD93D
用途：高亮标注、强调框

Mint Green（薄荷绿）
Hex: #6BCB77
用途：正面数据、增长指标
```

### 对比色（Visual Anchors）
```
Pure Black: #000000 - 文字、描边、分割线
Pure White: #FFFFFF - 反白文字块、对比背景
```

---

## 版式系统 - LAYOUT GRID

### 网格规范
```
- 基础网格：12 列等分
- 安全边距：上下左右各 80px
- 模块间距：24px
- 元素内边距：16px
```

### 经典版式模板

#### Type A: 封面页
```
┌─────────────────────────────────┐
│                                 │
│         [装饰性几何图形]          │
│                                 │
│      ╔═══════════════════╗      │
│      ║   主标题 (粗体 48pt) ║      │
│      ╚═══════════════════╝      │
│                                 │
│      ──── 副标题 (24pt) ────    │
│                                 │
│  [数据标签]  [数据标签]  [数据标签] │
│                                 │
└─────────────────────────────────┘
```

#### Type B: 数据对比页
```
┌─────────────────────────────────┐
│  标题区域 (居中，28pt)            │
├─────────────┬───────────────────┤
│             │                   │
│   图表区     │    关键洞察        │
│   (40%)     │    (60%)          │
│             │   • 数据点 1       │
│             │   • 数据点 2       │
│             │   • 数据点 3       │
└─────────────┴───────────────────┘
```

#### Type C: 时间线页
```
┌─────────────────────────────────┐
│  标题区域                        │
├─────────────────────────────────┤
│                                 │
│  ●────●────●────●────●         │
│  1970 1975 1980 1985 1990       │
│  │    │    │    │    │          │
│  事件  事件  事件  事件  事件      │
│                                 │
└─────────────────────────────────┘
```

#### Type D: 要点列表页
```
┌─────────────────────────────────┐
│  标题区域                        │
├─────────────────────────────────┤
│  ┌─────────────────────────┐    │
│  │ ▶ 要点 1 + 数据支撑      │    │
│  ├─────────────────────────┤    │
│  │ ▶ 要点 2 + 数据支撑      │    │
│  ├─────────────────────────┤    │
│  │ ▶ 要点 3 + 数据支撑      │    │
│  └─────────────────────────┘    │
└─────────────────────────────────┘
```

---

## 视觉元素库 - VISUAL ELEMENTS

### 装饰性图形
```
1. 半圆弧线（Quarter Circles）- 角落装饰
2. 同心圆环（Concentric Rings）- 焦点强调
3. 波浪线条（Wavy Lines）- 分割线
4. 星形爆发（Star Burst）- 新品/重点标注
5. 对话气泡（Speech Bubbles）- 引用/评论
6. 箭头指示（Block Arrows）- 流程/方向
```

### 数据可视化
```
1. 圆环图（Donut Charts）- 占比数据
2. 条形图（Bar Charts）- 对比数据
3. 折线图（Line Graphs）- 趋势数据
4. 信息卡（Info Cards）- 关键指标
5. 对比框（Comparison Boxes）- Before/After
```

---

## 字体系统 - TYPOGRAPHY

### 英文字体推荐
```
标题：Cooper Black / Souvenir / Bookman Bold
正文：Helvetica / Futura / Avant Garde
数字：Impact / League Gothic
```

### 中文字体推荐
```
标题：站酷复古体 / 造字工房力黑
正文：思源黑体 Regular / 苹方
数字：DIN Alternate / 优设标题黑
```

### 字号规范
```
封面主标题：48-56pt
内页标题：32-36pt
副标题：24-28pt
正文：18-22pt
数据标注：14-16pt
```

---

## 内容生成 Prompt 模板

### 通用内容 Prompt
```markdown
你是一位 [领域] 专家，请根据以下要求生成 PPT 内容：

【主题】[输入你的主题]
【受众】[目标受众描述]
【页数】[期望页数]

要求：
1. 每页必须包含至少 3 个具体数据点
2. 采用「问题 - 分析 - 解决方案」结构
3. 关键结论用粗体标注
4. 复杂概念用类比解释

输出格式：
- 页码
- 页面类型（封面/数据/时间线/要点）
- 标题
- 内容要点（带数据）
- 建议配图
```

### 视觉生成 Prompt
```markdown
【风格指令】
Retro Pop Art style, 1970s aesthetic, flat design, thick black outlines

【配色指令】
Background: #F5F0E6
Colors: #FF6B6B, #4ECDC4, #FFD93D, #6BCB77
Accents: #000000, #FFFFFF

【构图指令】
12-column grid, symmetric layout, geometric decorative elements

【内容指令】
[粘贴上方生成的内容要点]

【技术规格】
- 分辨率：1920x1080 或 3840x2160
- 格式：PNG 或 SVG
- 留白：四周 80px 安全边距
```

---

## 反推 Prompt 系统 - Image to Prompt

当看到一张复古波普风格的图片时，使用以下框架进行反推：

### 分析维度
```
1. 色彩分析
   - 提取主色（Top 5 colors）
   - 识别背景色
   - 标注对比色使用位置

2. 版式分析
   - 识别网格类型
   - 测量边距比例
   - 标注视觉重心

3. 元素分析
   - 列出所有装饰图形
   - 识别数据可视化类型
   - 标注文字层级

4. 风格分析
   - 描边粗细（px）
   - 填充方式（flat/gradient）
   - 纹理效果（noise/halftone）
```

### 反推 Prompt 模板
```markdown
【图像反推结果】

风格：Retro Pop Art / 70s Bohemian / Neo-Brutalism
配色：[HEX 色值列表]
版式：[网格类型]
字体：[字体特征描述]
元素：[视觉元素列表]

【可复用 Prompt】
[生成可直接使用的正向 Prompt]
```

---

## GitHub 开源项目结构

```
retro-pop-ppt/
├── README.md                 # 项目说明和使用指南
├── prompts/                  # Prompt 模板库
│   ├── content-generator.md  # 内容生成 Prompt
│   ├── visual-generator.md   # 视觉生成 Prompt
│   └── image-to-prompt.md    # 反推 Prompt 模板
├── templates/                # PPT 模板
│   ├── cover.md              # 封面模板
│   ├── data.md               # 数据页模板
│   ├── timeline.md           # 时间线模板
│   └── list.md               # 列表页模板
├── color-palette/            # 配色方案
│   ├── retro-pop.json        # 复古波普配色
│   └── neo-brutalism.json    # 新粗野主义配色
├── examples/                 # 示例作品
│   ├── case-1/               # 案例 1
│   └── case-2/               # 案例 2
├── scripts/                  # 工具脚本
│   ├── extract-colors.py     # 图片取色脚本
│   └── grid-generator.js     # 网格生成器
└── assets/                   # 素材资源
    ├── icons/                # 图标库
    └── shapes/               # 装饰图形
```

---

## 快速开始指南

### 步骤 1：内容生成
使用 `prompts/content-generator.md` 生成结构化内容

### 步骤 2：选择模板
根据内容类型选择合适的版式模板

### 步骤 3：视觉生成
使用 `prompts/visual-generator.md` 生成视觉稿

### 步骤 4：反推优化
如有参考图，使用 `prompts/image-to-prompt.md` 反推风格

---

## 版本记录

- v1.0.0 - 初始版本，包含核心 Prompt 系统和模板
- Future: 添加 AI 图像生成集成脚本
- Future: 添加在线演示页面
