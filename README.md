# Legado Book Source Developer Skill

## 概述

这是一个专门用于 Legado（阅读）Android 应用书源开发的完整工具包，包含 25+ 专用工具、完整知识库（24.93 MB）、134 个真实书源分析结果，以及基于 **40 万行 Legado 源码** 的深度分析。

### 源码分析亮点

基于 Legado 官方源码（397,380 行代码）的分析，提供了：

- **完整的数据结构定义**：BookSource、SearchRule、TocRule、ContentRule、BookInfoRule
- **规则解析引擎机制**：AnalyzeRule 类的完整实现细节
- **多种解析模式**：JSoup CSS、JSONPath、XPath、JavaScript、WebView
- **缓存机制**：规则缓存、正则缓存、脚本缓存
- **数据库架构**：Room 数据库表结构和索引设计
- **WebSocket 调试接口**：书源调试协议

## 目录结构

```
legado-book-source-developer/
├── README.md                           # 项目说明文档
├── SKILL.md                            # 核心Skill文档（主文档）
├── QUICKSTART.md                       # 快速开始指南
├── WORKFLOW.md                         # 完整工作流程
├── 文件结构说明.md                     # 文件结构和使用指南
├── SKILL优化总结.md                    # 优化总结文档
├── tools/                              # 分析工具集合
│   ├── quick_analyze.py               # ⭐快速网站分析工具（推荐）
│   ├── js_param_analyzer.py           # ⭐JavaScript参数分析工具
│   ├── analyze_fhysc.py               # 传统网站分析工具
│   ├── get_book_detail.py             # 获取书籍详情
│   ├── get_chapter.py                 # 获取章节内容
│   └── common.js                      # 网站 JS 文件
└── references/                         # 知识库和文档
    ├── Legado书源开发完整指南.md       # ⭐完整开发指南（14.6 MB）
    ├── 用户交互指南.md                # ⭐8个常见场景处理流程
    ├── 方法-JS扩展类.md                # JavaScript API文档
    ├── Legado书源编码处理指南.md        # 编码处理指南
    ├── Legado书源开发_长记忆系统.md    # 智能体系统
    ├── 阅读源码.txt                    # 40万行Legado源码（14.7 MB）
    ├── 歌书网_书源_修复版.json         # 修复版书源示例
    ├── 傲娇的验证大佬v0.2.js           # 验证工具
    ├── eruda.js                        # 调试工具
    ├── 仿M浏览器元素审查.user.js       # 元素审查工具
    ├── knowledge_base/                 # 134个真实书源分析（MD格式）
    │   └── book_sources/
    ├── book_source_database/           # 书源数据库（JSON格式）
    └── html_storage/                   # HTML存储
```

## 核心功能

### 1. 分析工具（tools/）

**⭐ 核心工具（推荐优先使用）**

- **quick_analyze.py** - 快速网站分析工具
  - ✅ 自动检测网站编码
  - ✅ 自动下载并分析JavaScript文件
  - ✅ 自动搜索可能的搜索接口模式
  - ✅ 自动分析HTML结构
  - ✅ 自动测试搜索接口
  - ✅ 生成结构化的JSON分析报告
  - ✅ 一次完成多个分析任务，大幅提升开发速度

- **js_param_analyzer.py** - JavaScript参数分析工具
  - ✅ 从HTML提取所有JavaScript
  - ✅ 查找搜索相关函数
  - ✅ 查找API端点
  - ✅ 查找参数生成函数
  - ✅ 查找加密库引用
  - ✅ 支持分析cURL命令

**传统工具（可选）**

- **analyze_fhysc.py** - 完整的网站分析工具
  - 检测网站编码
  - 分析首页结构
  - 测试搜索接口
  - 获取书籍详情和章节

- **get_book_detail.py** - 书籍详情获取
  - 获取书籍信息页
  - 提取章节列表
  - 获取章节内容

- **get_chapter.py** - 章节内容获取
  - 获取章节 HTML
  - 提取正文内容

### 2. 知识库（references/）

**⭐ 核心文档（必读）**

**Legado书源开发完整指南.md** - 完整开发指南（14.6 MB）
- 整合了所有核心内容
- 包含数据结构、规则语法、实战案例、常见陷阱
- 基于源码分析和真实书源
- **新增：书源配置开关详解**（14个配置开关详解）

**用户交互指南.md** - 8个常见场景的交互处理流程
- 场景1：搜索接口参数来源不明
- 场景2：HTML结构复杂或有动态加载
- 场景3：检测到反爬虫机制
- 场景4：GBK编码导致乱码
- 场景5：找不到书籍列表容器
- 场景6：nextContentUrl判断不明确
- 场景7：封面图片使用懒加载
- 场景8：作者和分类信息合并
- 每个场景包含标准询问格式和清晰建议

**方法-JS扩展类.md** - JavaScript API 详细说明
- 网络请求、文件操作等
- 完整的API参考

**Legado书源编码处理指南.md** - 编码检测和处理
- 编码检测时机
- GBK/UTF-8等编码问题
- 实际案例

**Legado书源开发_长记忆系统.md** - 智能体长记忆系统
- 知识库管理和学习

**源码分析（阅读源码.txt）**
- **40 万行 Legado 官方源码**（397,380 行）
- 完整的项目树形结构
- **核心数据类**：
  - `BookSource.kt` - 书源主数据类
  - `SearchRule.kt` - 搜索规则
  - `TocRule.kt` - 目录规则
  - `ContentRule.kt` - 正文规则
  - `BookInfoRule.kt` - 书籍信息规则
  - `ExploreRule.kt` - 发现规则
  - `ReviewRule.kt` - 段评规则
- **规则解析引擎**：
  - `AnalyzeRule.kt` - 核心规则解析类
  - 支持多种解析模式（JSoup/JSONPath/XPath/JS/WebView）
  - 缓存机制实现
  - 规则字符串解析
- **数据库架构**：
  - Room 数据库表结构
  - 索引设计
  - 类型转换器
- **WebSocket 调试**：
  - BookSourceDebugWebSocket
  - 调试协议格式
  - 实时调试支持

**knowledge_base/** - 134个真实书源分析
- 每个书源包含详细的结构分析
- 最常用的 CSS 选择器统计
- 最常用的提取类型统计
- 常见模式和陷阱

## 快速开始

### ⭐ 方式 1：使用核心工具快速分析（推荐）

```bash
# 进入 tools 目录
cd tools

# 快速分析网站（推荐：一次完成多个任务）
python quick_analyze.py https://www.example.com

# 分析 JavaScript 参数（如果网站有复杂JS）
python js_param_analyzer.py --analyze https://www.example.com
```

**快速分析工具会自动完成：**
1. ✓ 检测网站编码
2. ✓ 下载并分析JavaScript文件
3. ✓ 搜索可能的搜索接口模式
4. ✓ 分析HTML结构
5. ✓ 测试搜索接口
6. ✓ 生成结构化的JSON分析报告

### 方式 2：遵循工作流程创建书源

1. **阶段 1：收集信息**
   - 阅读 `WORKFLOW.md`
   - 查询知识库（references/）
   - 检测网站编码
   - 获取真实 HTML
   - **使用 quick_analyze.py 快速分析**

2. **阶段 2：严格审查**
   - 编写 CSS 选择器规则
   - 参考真实模板
   - 验证规则语法
   - 处理特殊情况
   - **遇到不确定的情况 → 查阅 `references/用户交互指南.md`**

3. **阶段 3：创建书源**
   - 生成完整 JSON
   - 导入 Legado 测试

### 方式 3：使用传统工具（可选）

```bash
# 进入 tools 目录
cd tools

# 传统分析流程
python analyze_fhysc.py
python get_book_detail.py
python get_chapter.py
```

## 书源创建标准工作流

### ⭐ 推荐流程（使用核心工具）

```bash
# 步骤 1：快速分析网站（推荐）
cd tools
python quick_analyze.py https://www.example.com

# 工具会自动生成分析报告，包含：
# - 网站编码
# - HTML结构
# - 搜索接口
# - JavaScript分析
```

### 传统流程（分步骤）

**步骤 1：查询知识库**
```bash
# 查看完整指南
cat references/Legado书源开发完整指南.md

# 查看真实书源示例
ls references/knowledge_base/book_sources/
```

**步骤 2：检测网站编码**
```bash
# 使用工具检测
cd tools
python quick_analyze.py https://www.example.com
# 输出会显示检测到的编码（UTF-8 或 GBK）
```

**重要原则：**
- 编码只需要检测一次
- 在流程开始时检测
- 后续所有操作都使用这个编码

**步骤 3：获取真实 HTML**
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

**步骤 4：分析 HTML 结构**

根据获取的 HTML，识别：
- 书籍列表容器
- 书名位置
- 作者、分类位置
- 封面图片位置
- 章节列表位置
- 正文内容位置

**步骤 5：编写规则**

参考完整指南中的模板：
- 选择合适的模板
- 根据实际 HTML 修改选择器
- 处理特殊情况（无封面、懒加载、信息合并）

**步骤 6：遇到不确定的情况？**

**查阅 `references/用户交互指南.md`**
- 8个常见场景的详细处理流程
- 标准的询问格式
- 清晰的建议和步骤

**步骤 7：生成书源 JSON**

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

### 核心文档（必读）
1. **SKILL.md** - 完整 Skill 文档，包含源码分析
2. **WORKFLOW.md** - 完整工作流程详解
3. **文件结构说明.md** - 文件结构和使用指南

### 知识库文档
4. **references/Legado书源开发完整指南.md** - ⭐完整开发指南（14.6 MB）
5. **references/用户交互指南.md** - ⭐8个常见场景处理流程
6. **references/阅读源码.txt** - **40 万行 Legado 源码**
7. **references/方法-JS扩展类.md** - JavaScript API 文档
8. **references/Legado书源编码处理指南.md** - 编码处理指南
9. **references/knowledge_base/book_sources/** - 134 个真实书源分析

## 源码分析参考

### 核心类（从源码中提取）

**BookSource.kt** - 书源主数据类
```kotlin
data class BookSource(
    var bookSourceUrl: String = "",          // 主键
    var bookSourceName: String = "",
    var bookSourceType: Int = 0,             // 0=文本, 1=音频, 2=图片, 3=文件, 4=视频
    var searchUrl: String? = null,
    var ruleSearch: SearchRule? = null,
    var ruleToc: TocRule? = null,
    var ruleContent: ContentRule? = null,
    var ruleBookInfo: BookInfoRule? = null,
    var ruleExplore: ExploreRule? = null,
    var ruleReview: ReviewRule? = null,
    var header: String? = null,
    var loginUrl: String? = null,
    var jsLib: String? = null,
    // ... 更多字段
)
```

**ContentRule.kt** - 正文规则
```kotlin
data class ContentRule(
    var content: String? = null,
    var nextContentUrl: String? = null,
    var subContent: String? = null,         // 副文规则
    var title: String? = null,              // 有些网站只能在正文中获取标题
    var webJs: String? = null,
    var replaceRegex: String? = null,
    var imageStyle: String? = null,
    var imageDecode: String? = null,
    var payAction: String? = null,
    var callBackJs: String? = null
)
```

**TocRule.kt** - 目录规则
```kotlin
data class TocRule(
    var chapterList: String? = null,
    var chapterName: String? = null,
    var chapterUrl: String? = null,
    var nextTocUrl: String? = null,
    var preUpdateJs: String? = null,
    var formatJs: String? = null,
    var isVolume: String? = null,
    var isVip: String? = null,
    var isPay: String? = null,
    var updateTime: String? = null
)
```

**SearchRule.kt** - 搜索规则
```kotlin
data class SearchRule(
    var checkKeyWord: String? = null,
    var bookList: String? = null,
    var name: String? = null,
    var author: String? = null,
    var intro: String? = null,
    var kind: String? = null,
    var lastChapter: String? = null,
    var updateTime: String? = null,
    var bookUrl: String? = null,
    var coverUrl: String? = null,
    var wordCount: String? = null
) : BookListRule
```

**AnalyzeRule.kt** - 规则解析引擎
```kotlin
class AnalyzeRule(
    private var ruleData: RuleDataInterface? = null,
    private val source: BaseSource? = null
) : JsExtensions {
    // 支持多种解析模式：
    // - Mode.Default: JSoup CSS 选择器
    // - Mode.Json: JSONPath
    // - Mode.XPath: XPath
    // - Mode.Js: JavaScript 执行
    // - Mode.WebJs: WebView JavaScript

    fun getString(ruleStr: String?, mContent: Any?, isUrl: Boolean): String
    fun getStringList(ruleStr: String?, mContent: Any?, isUrl: Boolean): List<String>?
    fun setContent(content: Any?, baseUrl: String?): AnalyzeRule
}
```

### 关键发现（基于源码）

1. **没有 `prevContentUrl` 字段** - 源码确认该字段不存在
2. **规则存储方式** - 所有规则作为 TEXT 存储，通过 GSON 序列化
3. **多种解析模式** - 支持 CSS/JSON/XPath/JS/WebView 五种模式
4. **缓存机制** - 规则、正则、脚本都有缓存
5. **WebSocket 调试** - `ws://127.0.0.1:1235/bookSourceDebug`
6. **数据库索引** - 在 `bookSourceUrl` 上有唯一索引

## 贡献和反馈

这个工具包基于 Legado 书源开发的最佳实践整理而成。

## 许可

本工具包遵循 Legado 项目的开源许可。
