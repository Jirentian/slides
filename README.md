# Retro Pop Art PPT Generator

> 将复杂专业知识转化为 70 年代复古波普网格风格的干货内容

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 简介

这是一个开源的 PPT 提示词系统，专为生成**复古波普艺术风格**的知识卡片和演示文稿而设计。

### 特色功能

- 深度搜索平台高赞笔记，快速提炼爆款逻辑
- 采用「数据说话」策略，每个模块包含具体数字
- 生成高度还原复古波普艺术（Retro Pop Art）风格
- 支持图像反推 Prompt，快速复刻喜欢的风格

---

## 配色系统

### 标准配色

| 角色 | 颜色 | HEX | 用途 |
|------|------|-----|------|
| Background | Warm Cream | `#F5F0E6` | 统一背景 |
| Primary | Salmon Pink | `#FF6B6B` | 重点数据、关键标题 |
| Secondary | Sky Blue | `#4ECDC4` | 辅助信息、图表元素 |
| Accent | Mustard Yellow | `#FFD93D` | 高亮标注、强调框 |
| Success | Mint Green | `#6BCB77` | 正面数据、增长指标 |
| Text | Pure Black | `#000000` | 文字、描边、分割线 |

### 使用示例

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

---

## 快速开始

### 1. 内容生成

使用内容生成 Prompt 创建结构化内容：

```markdown
你是一位 [领域] 专家，请根据以下要求生成 PPT 内容：

【主题】[输入你的主题]
【受众】[目标受众描述]
【页数】[期望页数]

要求：
1. 每页必须包含至少 3 个具体数据点
2. 采用「问题 - 分析 - 解决方案」结构
3. 关键结论用粗体标注
```

### 2. 视觉生成

使用视觉生成 Prompt 创建视觉稿：

```
Retro pop art style, 1970s aesthetic, flat design, thick black outlines
Background: #F5F0E6
Colors: #FF6B6B, #4ECDC4, #FFD93D, #6BCB77
12-column grid, symmetric layout
--ar 16:9 --style raw
```

### 3. 图像反推

有新图想要复刻风格？使用反推工具：

```bash
# 安装依赖
pip install -r requirements.txt

# 提取图片配色
python scripts/extract-colors.py path/to/image.png --prompt
```

---

## 项目结构

```
retro-pop-ppt/
├── README.md                 # 项目说明
├── prompt-system.md          # 完整提示词系统文档
├── prompts/
│   ├── image-to-prompt.md    # 图像反推指南
│   └── ...
├── scripts/
│   └── extract-colors.py     # 图片取色脚本
├── templates/                # PPT 模板
├── color-palette/            # 配色方案
├── examples/                 # 示例作品
└── assets/                   # 素材资源
```

---

## 模板预览

### Type A: 封面页
```
┌─────────────────────────────────┐
│         [装饰性几何图形]          │
│      ╔═══════════════════╗      │
│      ║   主标题 (粗体 48pt) ║      │
│      ╚═══════════════════╝      │
│      ──── 副标题 (24pt) ────    │
│  [数据标签]  [数据标签]  [数据标签] │
└─────────────────────────────────┘
```

### Type B: 数据对比页
```
┌─────────────────────────────────┐
│  标题区域 (居中，28pt)            │
├─────────────┬───────────────────┤
│   图表区     │    关键洞察        │
│   (40%)     │    (60%)          │
└─────────────┴───────────────────┘
```

---

## 工具推荐

### 在线工具
- [Image Color Picker](https://imagecolorpicker.com/) - 在线取色
- [Coolors](https://coolors.co/) - 配色生成
- [Figma](https://figma.com) - 设计工具

### AI 工具
- Midjourney - 图像生成
- Stable Diffusion - 图像生成
- Claude - 内容生成

---

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

## 更新日志

### v1.0.0 - 2024-03-24
- 初始版本发布
- 包含核心 Prompt 系统
- 图像反推功能
- Python 取色脚本

---

## 联系方式

- 问题反馈：开 Issue
- 示例分享：欢迎在 Discussions 分享你的作品！
