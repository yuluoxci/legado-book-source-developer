# Legado Book Source Developer Skill

## 概述

这是一个专门用于 Legado（阅读）Android 应用书源开发的完整工具包，包含 25+ 专用工具、完整知识库（24.93 MB）和 134 个真实书源分析结果。

## 目录结构

```
legado-skill-package/
├── README.md           # 本文件
├── QUICKSTART.md       # 快速开始指南
├── WORKFLOW.md         # 完整工作流程文档
├── tools/              # 分析工具集合
│   ├── analyze_fhysc.py        # 分析网站结构和编码
│   ├── analyze_js_params.py    # 分析 JavaScript 参数
│   ├── check_all_params.py     # 检查参数提取
│   ├── test_fixed_regex.py    # 测试正则表达式
│   ├── get_book_detail.py      # 获取书籍详情
│   ├── get_chapter.py         # 获取章节内容
│   └── common.js              # 网站 JS 文件
└── references/         # 知识库和文档
    ├── css_selector_rules.md       # CSS 选择器完整规范
    ├── book_source_templates.md    # 真实书源模板
    ├── real_book_source_examples.md # 134 个真实书源分析
    ├── post_request_config.md      # POST 请求配置
    ├── encoding_detection.md       # 编码检测和处理
    ├── workflow_phases.md          # 三阶段工作流详解
    ├── html_structures.md          # 常见 HTML 结构
    └── troubleshooting.md          # 问题排查指南
```

## 核心功能

### 1. 分析工具（tools/）

- **analyze_fhysc.py** - 完整的网站分析工具
  - 检测网站编码
  - 分析首页结构
  - 测试搜索接口
  - 获取书籍详情和章节

- **analyze_js_params.py** - 分析网站 JavaScript 参数
  - 提取首页 JS 变量
  - 分析反爬虫参数
  - 对比 curl 请求参数

- **check_all_params.py** - 参数提取验证
  - 检查所有必需参数
  - 识别缺失参数
  - 调试参数提取

- **test_fixed_regex.py** - 正则表达式测试
  - 测试参数提取正则
  - 验证匹配准确性

- **get_book_detail.py** - 书籍详情获取
  - 获取书籍信息页
  - 提取章节列表
  - 获取章节内容

- **get_chapter.py** - 章节内容获取
  - 获取章节 HTML
  - 提取正文内容

### 2. 知识库（references/）

**CSS 选择器规则（css_selector_rules.md）**
- 完整的 CSS 选择器语法
- 提取类型详解：@text, @html, @ownText, @href, @src
- 正则表达式格式和示例
- 数字索引使用：.0, .-1, .1
- 文本选择器：text.文本

**书源模板（book_source_templates.md）**
- 8 个经过验证的真实书源模板
- 标准小说站、笔趣阁、POST 请求等类型
- 每个模板的适用场景和规则说明
- 模板对比和修改方法

**真实书源分析（real_book_source_examples.md）**
- 134 个真实书源的分析结果
- 最常用的 CSS 选择器统计
- 最常用的提取类型统计
- 常见模式和陷阱

**POST 请求配置（post_request_config.md）**
- method 配置
- body 格式
- charset 编码
- webView 参数
- 完整配置示例

**编码检测（encoding_detection.md）**
- 编码检测时机
- GBK/UTF-8 处理
- 常见编码问题
- 实际案例

**工作流程（workflow_phases.md）**
- 三阶段工作流详解
- 每个阶段的具体步骤
- 检查清单
- 常见错误

**HTML 结构（html_structures.md）**
- 常见 HTML 结构类型
- 每种结构的解决方案
- CSS 选择器示例
- 特殊情况处理

**问题排查（troubleshooting.md）**
- 搜索无结果
- 内容缺失
- 目录顺序错误
- 广告过滤
- 分页问题
- 图片盗链
- 编码乱码

## 快速开始

### 方式 1：使用工具分析网站

```bash
# 进入 tools 目录
cd tools

# 分析网站结构和编码
python analyze_fhysc.py

# 分析 JavaScript 参数（如果网站有反爬虫）
python analyze_js_params.py

# 获取书籍详情和章节
python get_book_detail.py
```

### 方式 2：遵循工作流程创建书源

1. **阶段 1：收集信息**
   - 阅读 `WORKFLOW.md`
   - 查询知识库（references/）
   - 检测网站编码
   - 获取真实 HTML

2. **阶段 2：严格审查**
   - 编写 CSS 选择器规则
   - 参考真实模板
   - 验证规则语法
   - 处理特殊情况

3. **阶段 3：创建书源**
   - 生成完整 JSON
   - 导入 Legado 测试

## 书源创建标准工作流

### 步骤 1：查询知识库

```bash
# 查看 CSS 选择器规则
cat references/css_selector_rules.md

# 查看书源模板
cat references/book_source_templates.md

# 查看真实书源示例
cat references/real_book_source_examples.md
```

### 步骤 2：检测网站编码

```bash
# 使用工具检测
cd tools
python analyze_fhysc.py
# 输出会显示检测到的编码（UTF-8 或 GBK）
```

**重要原则：**
- 编码只需要检测一次
- 在流程开始时检测
- 后续所有操作都使用这个编码

### 步骤 3：获取真实 HTML

```bash
# 获取搜索页 HTML
python get_book_detail.py

# 获取详情页和章节
python get_chapter.py
```

**关键检查：**
- ✅ 使用正确的 HTTP 方法（GET/POST）
- ✅ 使用检测到的编码
- ✅ 获取完整 HTML 源代码
- ✅ 检查懒加载（data-original vs src）
- ✅ 检查搜索页是否有封面

### 步骤 4：分析 HTML 结构

根据获取的 HTML，识别：
- 书籍列表容器
- 书名位置
- 作者、分类位置
- 封面图片位置
- 章节列表位置
- 正文内容位置

### 步骤 5：编写规则

参考 `book_source_templates.md` 中的模板：
- 选择合适的模板
- 根据实际 HTML 修改选择器
- 处理特殊情况（无封面、懒加载、信息合并）

### 步骤 6：生成书源 JSON

按照标准格式生成书源，确保包含所有必需字段。

## CSS 选择器速查

### 常用选择器

```
元素选择器：
  div@text          # 提取 div 文本
  a@href            # 提取链接地址
  img@src           # 提取图片地址

类选择器：
  .title@text       # 提取 class="title" 的文本
  .author@text      # 提取 class="author" 的文本

ID 选择器：
  #content@html     # 提取 id="content" 的 HTML

后代选择器：
  .book-list .item .title@text  # 嵌套选择

数字索引（推荐）：
  .item.0@text      # 第一个 item
  .item.-1@text     # 最后一个 item
  .author.0@text    # 第一个 author

文本选择器（替代 :contains()）：
  text.下一章@href  # 包含"下一章"的链接
```

### 提取类型

| 类型 | 说明 | 用途 |
|------|------|------|
| @text | 元素及其子元素的完整文本 | 书名、作者、章节名 |
| @ownText | 仅元素本身的文本（不含子元素） | 去除广告后的内容 |
| @html | 完整 HTML 结构 | 保留格式的正文 |
| @href | 链接地址 | 书籍链接、章节链接 |
| @src | 图片地址 | 封面图片 |

### 正则表达式

```
删除前缀：
  ##^作者：         # 删除开头的"作者："
  ##^《             # 删除开头的"《"

删除后缀：
  ##（.*）$         # 删除括号及内容
  ##》$             # 删除结尾的"》"

提取特定内容：
  ##.*作者：(.*)##$1   # 提取"作者："后的内容
  ##第(\d+)章##$1      # 提取章节号

清理广告：
  ##<div id="ad">[\s\S]*?</div>  # 删除广告 div
  ##请收藏本站|本章完|继续阅读   # 删除提示文本
```

## POST 请求配置

### 标准 POST 请求

```json
{
  "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\"}"
}
```

### POST + GBK 编码

```json
{
  "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"charset\":\"gbk\"}"
}
```

### POST + Headers

```json
{
  "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"headers\":{\"X-Requested-With\":\"XMLHttpRequest\"}}"
}
```

## 编码处理

### UTF-8 网站（默认）

```json
{
  "searchUrl": "/search?q={{key}}"
}
```

### GBK 网站

```json
{
  "searchUrl": "/search?q={{key}},{\"charset\":\"gbk\"}"
}
```

### GBK + POST 请求

```json
{
  "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"charset\":\"gbk\"}"
}
```

## nextContentUrl 判断规则

### 必须设置的场景

- 按钮链接到真正的下一章节（第一章→第二章）
- 按钮文字：下一章、下章、下一节、下一话
- URL 模式：/chapter/1.html → /chapter/2.html（章节号变化）

```json
{
  "ruleContent": {
    "nextContentUrl": "text.下一章@href"
  }
}
```

### 必须留空的场景

- 按钮只是同一章节的分页
- 按钮文字：下一页、继续阅读、翻到下一页
- URL 模式：/chapter/1_1.html → /chapter/1_2.html（页码变化）

```json
{
  "ruleContent": {
    "nextContentUrl": ""
  }
}
```

## 常见陷阱

### ❌ 禁止使用的

1. **prevContentUrl** - Legado 中不存在
2. **:contains()** - 应使用 `text.文本`
3. **:first-child/:last-child** - 应使用 `.0`, `.-1`
4. 混淆"下一页"和"下一章"

### ✅ 推荐做法

1. 先查询知识库
2. 检测网站编码
3. 获取真实 HTML
4. 参考真实模板
5. 处理特殊情况

## 工具使用示例

### 示例 1：分析新网站

```bash
cd tools
python analyze_fhysc.py
```

输出会包含：
- 网站编码
- 首页结构
- 搜索接口测试
- 书籍详情
- 章节列表
- 章节内容

### 示例 2：处理反爬虫参数

```bash
cd tools
python analyze_js_params.py
```

输出会包含：
- 首页 JS 变量
- 参数对比分析
- common.js 相关代码

### 示例 3：验证正则表达式

```bash
cd tools
python test_fixed_regex.py
```

输出会包含：
- 提取到的参数数量
- 提取到的参数列表
- 生成的参数字符串

## 书源 JSON 格式

### 标准格式

```json
[
  {
    "bookSourceName": "示例书源",
    "bookSourceUrl": "https://example.com",
    "searchUrl": "/search?q={{key}}",
    "ruleSearch": {
      "bookList": ".book-item",
      "name": ".title@text",
      "author": ".author@text",
      "bookUrl": "a@href",
      "coverUrl": "img@src"
    },
    "ruleBookInfo": {
      "name": ".book-title@text",
      "author": ".author@text",
      "intro": ".intro@text"
    },
    "ruleToc": {
      "chapterList": "#chapter-list li",
      "chapterName": "a@text",
      "chapterUrl": "a@href"
    },
    "ruleContent": {
      "content": "#content@html",
      "nextContentUrl": ""
    }
  }
]
```

### 必需字段

**ruleSearch:**
- bookList（必需）
- name（必需）
- bookUrl（必需）
- author, kind, lastChapter, coverUrl（可选）

**ruleBookInfo:**
- name（必需）
- 其他字段（可选）

**ruleToc:**
- chapterList（必需）
- chapterName（必需）
- chapterUrl（必需）
- nextTocUrl（可选）

**ruleContent:**
- content（必需）
- nextContentUrl（可选）

## 学习资源

1. **WORKFLOW.md** - 完整工作流程详解
2. **references/css_selector_rules.md** - CSS 选择器完整规范
3. **references/book_source_templates.md** - 8 个真实模板
4. **references/real_book_source_examples.md** - 134 个真实书源分析
5. **references/troubleshooting.md** - 问题排查指南

## 贡献和反馈

这个工具包基于 Legado 书源开发的最佳实践整理而成。

## 许可

本工具包遵循 Legado 项目的开源许可。
