---
name: legado-book-source-developer
description: This skill should be used when working with Legado (阅读) book source development, debugging, or knowledge management tasks. It provides specialized workflows for creating book sources from web pages, debugging book source rules, querying Legado knowledge base, and managing book source databases. Use this skill when users need to create book sources for novel websites, debug existing book sources, or query Legado-specific knowledge about CSS selectors, rule formats, and book source JSON structure.
---

# Legado Book Source Developer Skill

This skill provides comprehensive support for Legado (阅读) Android app book source development. It combines MCP Server architecture with specialized tools for automated book source creation, knowledge management, and intelligent analysis.

## Skill Overview

Transform model into a Legado book source development specialist equipped with:
- 25+ specialized tools for book source development and analysis
- Complete Legado knowledge base (24.93 MB, 169 files)
- 134 real book source analysis results as references
- Real HTML fetching and intelligent analysis capabilities
- Automated book source crawler and learning system
- 3-phase workflow for reliable book source creation

## When to Use This Skill

Use this skill when:
- Creating new book sources for novel/manga websites
- Debugging existing book source rules
- Querying Legado-specific knowledge (CSS selectors, rule formats, POST requests)
- Analyzing website HTML structure for book source development
- Managing book source database and knowledge base
- Learning Legado book source development best practices

## Skill Architecture

### Core Components

**1. MCP Server Infrastructure** (`_internal/mcp_server/`)
- **server.py**: Main server with HTTP/WebSocket support, JSON-RPC protocol handling
- **tool_registry.py**: Extensible tool management with metadata, parameters, adapters
- **discovery.py**: Dynamic tool discovery from Python files and modules
- **config_loader.py**: Hot-reload configuration management
- **protocol.py**: JSON-RPC message protocol implementation
- **async_manager.py**: Concurrent task execution management
- **system_prompt_injector.py**: System prompt injection for AI models

**2. Knowledge Base** (`assets/`)
- **Total Files**: 169 files, 24.93 MB
- **Core Knowledge Files**:
  - `css选择器规则.txt` (80KB) - Complete CSS selector handbook
  - `书源规则：从入门到入土.md` (39KB) - Comprehensive tutorial
  - `真实书源模板库.txt` (8KB) - 8 proven templates
  - `真实书源高级功能分析.md` (9KB) - 134 real sources analysis
  - `阅读源码.txt` (40万行) - Complete Legado source code
- **Real Book Sources**: 134 analyzed sources in `knowledge_base/book_sources/`
- **Knowledge Index**: `knowledge_index.json` - Searchable metadata for all files

**3. Specialized Tools** (25+ tools from config/agent_llm_config.json)

### Complete Tool List

**Knowledge Query Tools:**
1. `search_knowledge` - Query knowledge base with keywords
2. `search_knowledge_index` - Search knowledge base index
3. `get_css_selector_rules` - Get complete CSS selector rules (paginated)
4. `get_real_book_source_examples` - Retrieve 134 real book source analysis results
5. `get_book_source_templates` - Get proven book source templates
6. `list_all_knowledge_files` - List all knowledge files
7. `read_file_paginated` - Read files with pagination support
8. `get_file_summary` - Get file summary information

**HTML Analysis Tools:**
9. `smart_fetch_html` - Fetch real HTML with encoding support
10. `smart_web_analyzer` - Intelligent web page structure analysis
11. `smart_bookinfo_analyzer` - Analyze book information pages
12. `smart_toc_analyzer` - Analyze table of contents pages
13. `smart_content_analyzer` - Analyze content pages
14. `smart_full_analyzer` - Complete page analysis

**Learning System Tools:**
15. `knowledge_learner` - Learn from new book sources
16. `knowledge_applier` - Apply learned knowledge to new tasks
17. `knowledge_enhanced_analyzer` - Enhanced analysis with knowledge
18. `learn_knowledge_base` - Re-learn knowledge base after updates
19. `audit_knowledge_base` - Audit knowledge base validity
20. `knowledge_auditor` - Audit specific knowledge items

**User Interaction Tools:**
21. `user_intervention` - Request user input for complex tasks
22. `collaborative_edit` - Collaborative book source editing

**Encoding Detection Tools:**
23. `detect_charset` - Detect website encoding
24. `detect_charset_from_html` - Detect encoding from HTML content

**Book Source Management:**
25. `edit_book_source` - Create/edit book sources (complete_source parameter)

## Workflow Phases

### ⚠️ 核心原则：必须基于真实源码分析

**绝对禁止：**
- ❌ 禁止基于假设或推测进行分析
- ❌ 禁止不获取真实HTML源码就编写规则
- ❌ 禁止不分析JS就推断搜索接口参数
- ❌ 禁止不确定时继续下一步

**必须做到：**
- ✅ 必须获取并分析真实HTML源码
- ✅ 必须分析网站的JavaScript代码
- ✅ 必须通过浏览器Network面板验证真实请求
- ✅ 不确定时必须询问用户并提供建议

### Phase 1: Information Collection (DO NOT create book source!)

**Step 1: 获取网站真实源码（MUST be first!)**

**1.1 使用浏览器开发者工具获取真实请求**

```javascript
// 在浏览器控制台执行
// 1. 打开开发者工具（F12）
// 2. 切换到 Network 标签
// 3. 执行搜索操作
// 4. 查看实际发出的请求
// 5. 记录以下信息：
```

**必须记录的信息：**
- [ ] 请求方法（GET/POST）
- [ ] 完整的请求URL
- [ ] 所有请求头（Headers）
- [ ] 请求体（Body，如果是POST）
- [ ] 所有查询参数（Query Parameters）
- [ ] 响应状态码
- [ ] 响应内容类型（Content-Type）

**1.2 下载并分析JavaScript文件**

**识别关键JS文件：**
- 搜索页面加载的所有JS文件
- 特别关注 `search.js`、`common.js`、`app.js` 等文件
- 查找内嵌的 `<script>` 标签

**分析方法：**
```bash
# 使用Python工具分析JS
cd tools
python analyze_js_params.py
```

**需要从JS中提取的信息：**
- 搜索函数的调用方式
- 参数生成逻辑（加密、签名等）
- API端点配置
- 请求头配置
- 请求编码方式

**1.3 获取并保存真实HTML源码**

**必须获取的页面：**
```python
# 1. 首页
fetch_and_save('https://example.com', 'home.html')

# 2. 搜索页（包含搜索结果的HTML）
fetch_and_save('https://example.com/search?q=test', 'search.html')

# 3. 书籍详情页
fetch_and_save('https://example.com/book/123', 'detail.html')

# 4. 目录页
fetch_and_save('https://example.com/book/123/toc', 'toc.html')

# 5. 章节内容页
fetch_and_save('https://example.com/chapter/1', 'content.html')
```

**保存要求：**
- 保存完整的HTML源码（不截断）
- 使用正确的编码（UTF-8或GBK）
- 包含所有 `<script>` 和 `<link>` 标签
- 保留完整的CSS样式和内联脚本

**Step 2: 分析真实源码并推断规则**

**2.1 分析搜索接口（基于真实请求）**

**从Network面板获取的示例：**
```
Request URL: https://api.example.com/search
Request Method: POST
Request Headers:
  Content-Type: application/json
  User-Agent: Mozilla/5.0...
  X-Requested-With: XMLHttpRequest
Request Body:
  {"keyword":"test","page":1,"timestamp":1700000000,"signature":"abc123"}
```

**分析步骤：**
1. 识别请求方式（GET/POST）
2. 识别请求格式（JSON/Form-Data/Query String）
3. 识别所有必需参数
4. 识别参数生成逻辑（在JS中查找）
5. 识别请求头要求

**2.2 分析HTML结构（基于真实HTML源码）**

**分析方法：**
```python
# 使用BeautifulSoup分析
from bs4 import BeautifulSoup

with open('search.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 查找书籍列表容器
book_list = soup.select('.book-list, .result-list, .search-result')

# 分析单个书籍项的结构
if book_list:
    first_book = book_list[0].find('li', class_='item') or book_list[0].find('div', class_='item')
    print(first_book.prettify())  # 打印完整结构
```

**必须验证的选择器：**
- 书籍列表容器：测试 `.book-list`、`.result-list` 等是否有效
- 书名提取：测试 `.title@text` 是否能正确提取
- 作者提取：测试 `.author@text` 是否能正确提取
- 封面提取：测试 `img@src` 或 `img@data-original` 是否有效
- 链接提取：测试 `a@href` 是否能获取正确URL

**2.3 疑问处理机制**

**遇到不确定的情况时：**

**情况1：搜索接口参数来源不明**
```
❌ 不要继续编写规则！
✅ 向用户提问：

【问题】搜索接口需要以下参数，但不确定它们的生成方式：

参数列表：
- timestamp: 时间戳（可能是毫秒或秒）
- signature: 签名（需要查看JS代码）
- token: 令牌（可能需要登录或从首页获取）

【建议】
1. 请打开浏览器开发者工具（F12）
2. 切换到 Sources 标签
3. 搜索以下关键词：signature、token、encrypt、sign
4. 找到相关的函数定义
5. 或者告诉我网站是否有登录要求

请用户提供：
- 登录账号（如果有）
- JavaScript文件中相关的代码片段
- 或者网站的特殊访问要求
```

**情况2：HTML结构复杂或有反爬虫**
```
❌ 不要猜测规则！
✅ 向用户提问：

【问题】搜索页面的HTML结构可能包含动态加载内容

观察到的现象：
- 书籍列表在HTML中为空
- 存在大量JavaScript代码
- 可能需要渲染后才能看到内容

【建议】
1. 检查是否有API接口返回JSON数据
2. 查看Network面板的XHR/Fetch请求
3. 或者使用Headless浏览器获取渲染后的HTML

请用户提供：
- Network面板中找到的API请求（如果有）
- 或者选择使用webView配置
```

**情况3：检测到反爬虫机制**
```
❌ 不要绕过反爬虫！
✅ 向用户提问：

【问题】网站可能使用了反爬虫机制

检测到的特征：
- 需要复杂的参数签名
- 需要特定的请求头
- 可能需要Cookie或Session
- 可能有频率限制

【建议】
1. 此类网站可能需要手动配置headers
2. 可能需要登录账号
3. 可能需要使用webView模式

请用户提供：
- 登录账号（如果有）
- 网站的使用说明或文档
- 或者选择其他网站
```

**Step 3: Query Knowledge Base and Reference Real Sources**
```
# Get CSS selector rules
get_css_selector_rules()

# Query book source structure
search_knowledge("CSS选择器格式 提取类型 @text @html @ownText @textNode @href @src")

# Query POST request configuration
search_knowledge("POST请求配置 method body String() charset webView")

# Get real book source analysis (134 sources)
get_real_book_source_examples(limit=10)

# Get proven templates
get_book_source_templates(limit=5)

# Query common patterns from 134 real sources
search_knowledge("常用CSS选择器 img h1 div content intro h3")
search_knowledge("常用提取类型 @href @text @src @html @js")
search_knowledge("常见书源结构模式 标准小说站 笔趣阁 聚合源")
```

**Step 2: Query Knowledge Base (参考已有知识)**
```
# 获取CSS选择器规则
get_css_selector_rules()

# 查询书源结构
search_knowledge("CSS选择器格式 提取类型 @text @html @ownText @textNode @href @src")

# 查询POST请求配置
search_knowledge("POST请求配置 method body String() charset webView")

# 获取真实书源分析（134个源）
get_real_book_source_examples(limit=10)

# 获取经过验证的模板
get_book_source_templates(limit=5)

# 查询常见模式
search_knowledge("常用CSS选择器 img h1 div content intro h3")
search_knowledge("常用提取类型 @href @text @src @html @js")
search_knowledge("常见书源结构模式 标准小说站 笔趣阁 聚合源")
```

**Step 3: Detect Website Encoding (CRITICAL - BEFORE fetching HTML!)**
```
detect_charset(url="http://example.com")
```

**Key Principles:**
1. Detect encoding ONCE at workflow start
2. Record detected encoding (UTF-8, GBK, GB2312, etc.)
3. Use this encoding in ALL subsequent operations
4. Do NOT repeat detection in later steps

**Encoding Handling:**
- **UTF-8**: Omit charset parameter (default)
- **GBK**: Add `"charset":"gbk"` to POST/GET requests
- **GB2312**: Use `"charset":"gbk"` (GBK compatible)

**Step 4: Fetch and Analyze Real HTML (必须基于真实源码!)**

**4.1 获取真实HTML（使用检测到的编码）**
```
# GET request with detected encoding
smart_fetch_html(url="http://example.com/search", charset="gbk")

# POST request with detected encoding
smart_fetch_html(
    url="http://m.gashuw.com/s.php",
    method="POST",
    body="keyword={{key}}&t=1",
    headers={"Content-Length": "0"},
    charset="gbk"  # Use encoding from step 2
)
```

**Critical Rules:**
1. Use correct HTTP method (GET vs POST)
2. Use encoding detected in step 2
3. Fetch complete HTML source code (no compression/truncation)
4. Check for lazy loading (data-original vs src)
5. Check if search page has cover images
6. Permanently save HTML for later use

**Step 4: Analyze HTML Structure**
```
smart_web_analyzer(html="<html>...</html>")  # Full page analysis
smart_bookinfo_analyzer(html="<html>...</html>")  # Book info page
smart_toc_analyzer(html="<html>...</html>")  # Table of contents
smart_content_analyzer(html="<html>...</html>")  # Content page
```

**Analysis Checklist:**
- [ ] List structure (identify book list containers and repeating elements)
- [ ] Element positions (book name, author, category, cover, latest chapter)
- [ ] Special attributes (lazy loading data-original, custom attributes)
- [ ] Nesting relationships (parent-child element relationships)
- [ ] Information distribution (which fields are merged, which are separate)
- [ ] Pagination elements (next page/next chapter buttons)
- [ ] Search page cover images (many sites don't have them)

**Record WITHOUT Creating Book Source:**
- CSS selector rules from knowledge base
- Book source JSON structure
- POST request configuration
- 134 real book source analysis results
- Real book source templates
- Real HTML source code (permanently saved)
- HTML structure analysis
- Special cases (no cover, lazy loading, merged info)
- Inferred CSS selectors
- searchUrl format

### Phase 2: Strict Review

**Step 1: Write Rules Based on Knowledge**
- Reference 134 real book source analysis results
- Follow proven templates from `get_book_source_templates()`
- Use detected encoding from phase 1
- Handle special cases (no cover, lazy loading, merged info)

**Most Used CSS Selectors (from 134 sources):**
- `img` (40 times) - Cover images
- `h1` (30 times) - Book titles
- `div` (13 times) - Generic containers
- `content` (12 times) - Content areas
- `intro` (11 times) - Introductions
- `h3` (9 times) - Chapter names
- `span` (9 times) - Generic inline elements

**Most Used Extraction Types:**
- `@href` (81 times) - Link addresses
- `@text` (72 times) - Text content
- `@src` (60 times) - Image sources
- `@html` (33 times) - HTML structure
- `@js` (25 times) - JavaScript processing

**Step 2: Validate Rule Syntax**
- Verify CSS selector format: `CSS选择器@提取类型`
- Check extraction types: @text, @html, @ownText, @textNode, @href, @src
- Validate regular expression format: `##正则表达式##替换内容`
- Confirm JSON structure completeness
- Validate POST request configuration

**Step 3: Handle Special Cases**
- No cover image: `"coverUrl": ""`
- Lazy loading: `"img@data-original||img@src"`
- Merged information: Use regex to split
- Multiple same-name tags: Use numeric indices (.0, .1, .-1)

### Phase 3: Create Book Source (Final Step!)

**Step 1: Prepare Complete Book Source JSON**
- Include all required fields based on HTML analysis
- Apply rules from phase 2
- Ensure special cases are handled
- Reference real templates

**Step 2: Create Book Source in One Call**
- Call `edit_book_source(complete_source="完整JSON")` ONLY ONCE
- Use `complete_source` parameter
- Include all mandatory fields

**Step 3: Output Complete JSON**
- Output as standard JSON array
- Ready for import into Legado app

## Legado Source Code Analysis

Based on analysis of Legado source code (397,380 lines), key findings:

### Core BookSource Data Structure (BookSource.kt)

```kotlin
data class BookSource(
    @PrimaryKey var bookSourceUrl: String = "",
    var bookSourceName: String = "",
    var bookSourceGroup: String? = null,
    var bookSourceType: Int = 0,  // 0=文本, 1=音频, 2=图片, 3=文件, 4=视频
    var bookUrlPattern: String? = null,
    var customOrder: Int = 0,
    var enabled: Boolean = true,
    var enabledExplore: Boolean = true,
    var jsLib: String? = null,
    var enabledCookieJar: Boolean? = true,
    var concurrentRate: String? = null,
    var header: String? = null,
    var loginUrl: String? = null,
    var loginUi: String? = null,
    var loginCheckJs: String? = null,
    var coverDecodeJs: String? = null,
    var bookSourceComment: String? = null,
    var variableComment: String? = null,
    var lastUpdateTime: Long = 0,
    var respondTime: Long = 180000L,
    var weight: Int = 0,
    var exploreUrl: String? = null,
    var exploreScreen: String? = null,
    var ruleExplore: ExploreRule? = null,
    var searchUrl: String? = null,
    var ruleSearch: SearchRule? = null,
    var ruleBookInfo: BookInfoRule? = null,
    var ruleToc: TocRule? = null,
    var ruleContent: ContentRule? = null,
    var ruleReview: ReviewRule? = null,
    var eventListener: Boolean = false,
    var customButton: Boolean = false
)
```

### Rule Data Structures

#### BookInfoRule
```kotlin
data class BookInfoRule(
    var init: String? = null,
    var name: String? = null,
    var author: String? = null,
    var intro: String? = null,
    var kind: String? = null,
    var lastChapter: String? = null,
    var updateTime: String? = null,
    var coverUrl: String? = null,
    var tocUrl: String? = null,
    var wordCount: String? = null,
    var canReName: String? = null,
    var downloadUrls: String? = null
)
```

#### ContentRule
```kotlin
data class ContentRule(
    var content: String? = null,
    var subContent: String? = null,      // 副文规则
    var title: String? = null,           // 有些网站只能在正文中获取标题
    var nextContentUrl: String? = null,   // 下一章链接
    var webJs: String? = null,
    var sourceRegex: String? = null,
    var replaceRegex: String? = null,
    var imageStyle: String? = null,
    var imageDecode: String? = null,
    var payAction: String? = null,
    var callBackJs: String? = null
)
```

#### TocRule
```kotlin
data class TocRule(
    var preUpdateJs: String? = null,
    var chapterList: String? = null,
    var chapterName: String? = null,
    var chapterUrl: String? = null,
    var formatJs: String? = null,
    var isVolume: String? = null,
    var isVip: String? = null,
    var isPay: String? = null,
    var updateTime: String? = null,
    var nextTocUrl: String? = null
)
```

#### SearchRule
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

### Rule Parsing Engine (AnalyzeRule.kt)

The `AnalyzeRule` class is the core rule parsing engine supporting:

**1. Multiple Parsing Modes:**
- **Mode.Default**: JSoup CSS selector parsing (default for HTML)
- **Mode.Json**: JSONPath parsing for JSON data
- **Mode.XPath**: XPath parsing for XML/HTML
- **Mode.Js**: JavaScript execution
- **Mode.WebJs**: WebView-based JavaScript (for dynamic content)

**2. Rule String Format:**
```
CSS选择器@提取类型##正则表达式##替换内容
```

**3. Supported Extraction Types (from source code):**
- `@text` - Text content (includes children)
- `@html` - HTML structure
- `@ownText` - Element text only (excludes children)
- `@textNode` - Text nodes
- `@href` - Link URL
- `@src` - Image source
- `@js` - JavaScript processing

**4. Key Methods:**
```kotlin
fun getString(ruleStr: String?, mContent: Any?, isUrl: Boolean): String
fun getStringList(ruleStr: String?, mContent: Any?, isUrl: Boolean): List<String>?
fun setContent(content: Any?, baseUrl: String?): AnalyzeRule
fun setBaseUrl(baseUrl: String?): AnalyzeRule
```

**5. Rule Processing Flow:**
1. Parse rule string into `SourceRule` list
2. Apply each rule sequentially
3. Handle mode switching (CSS/JSON/XPath/JS)
4. Apply regex replacements
5. Return final result

### Database Schema (from Room)

**BookSource Table:**
```sql
CREATE TABLE bookSources (
    bookSourceName TEXT NOT NULL,
    bookSourceGroup TEXT,
    bookSourceUrl TEXT NOT NULL PRIMARY KEY,
    bookSourceType INTEGER NOT NULL,
    bookUrlPattern TEXT,
    customOrder INTEGER NOT NULL DEFAULT 0,
    enabled INTEGER NOT NULL DEFAULT 1,
    enabledExplore INTEGER NOT NULL DEFAULT 1,
    jsLib TEXT,
    enabledCookieJar INTEGER DEFAULT 0,
    header TEXT,
    loginUrl TEXT,
    loginUi TEXT,
    coverDecodeJs TEXT,
    bookSourceComment TEXT,
    variableComment TEXT,
    lastUpdateTime INTEGER NOT NULL,
    respondTime INTEGER NOT NULL DEFAULT 180000,
    weight INTEGER NOT NULL DEFAULT 0,
    exploreUrl TEXT,
    exploreScreen TEXT,
    ruleExplore TEXT,
    searchUrl TEXT,
    ruleSearch TEXT,
    ruleBookInfo TEXT,
    ruleToc TEXT,
    ruleContent TEXT
)
```

**Index:**
- `index_book_sources_bookSourceUrl` on `bookSourceUrl`

### WebSocket Debug Interface

**Book Source Debug WebSocket:**
```javascript
URL: ws://127.0.0.1:1235/bookSourceDebug
Message: {key: "搜索关键词", tag: "源链接"}
```

### Key Findings from Source Code

1. **No `prevContentUrl`**: The source code confirms this field does not exist in Legado
2. **Rule Storage**: All rules are stored as TEXT and converted via GSON JSON serialization
3. **Caching**: String rules are cached in `stringRuleCache` HashMap
4. **Multiple Format Support**: Rules support both JSON object and primitive string formats
5. **Regex Caching**: Regular expressions are cached for performance
6. **WebView Integration**: Dynamic content can be handled via `webJs` and `BackstageWebView`

## Critical Constraints

**Strictly Prohibited:**
1. Using `prevContentUrl` field (confirmed nonexistent in Legado source code)
2. Using `:contains()` pseudo-class selectors (use `text.文本` format)
3. Using `:first-child/:last-child` pseudo-class selectors (use numeric indices .0, .-1)
4. Confusing "next page" with "next chapter" for `nextContentUrl`
5. Skipping knowledge base queries
6. Creating book sources without fetching real HTML
7. Not referencing real templates and analysis results
8. Detecting encoding multiple times (detect ONCE only)

**Field Completeness Rules (from source code):**

**ruleContent MUST include (ContentRule.kt):**
- `content`: Required (chapter content extraction)
- `nextContentUrl`: Conditional (only for true next chapter links)
- Optional fields:
  - `subContent` - 副文规则，拼接在正文后面或获取歌词等
  - `title` - 有些网站只能在正文中获取标题
  - `webJs` - WebView JavaScript
  - `sourceRegex` - 源正则
  - `replaceRegex` - 替换规则
  - `imageStyle` - 图片样式（默认大小居中，FULL最大宽度）
  - `imageDecode` - 图片bytes二次解密js
  - `payAction` - 购买操作
  - `callBackJs` - 事件监听回调

**ruleToc MUST include (TocRule.kt):**
- `chapterList`: Required
- `chapterName`: Required
- `chapterUrl`: Required
- Optional fields:
  - `nextTocUrl`: Conditional (if pagination exists)
  - `preUpdateJs` - 更新前执行
  - `formatJs` - 格式化
  - `isVolume` - 是否卷
  - `isVip` - 是否VIP
  - `isPay` - 是否付费
  - `updateTime` - 更新时间

**ruleSearch MUST include (SearchRule.kt):**
- `checkKeyWord`: 校验关键字
- `bookList`: Required
- `name`: Required
- `bookUrl`: Required
- Optional fields based on availability: author, kind, lastChapter, coverUrl, wordCount, intro, updateTime

**ruleBookInfo MUST include (BookInfoRule.kt):**
- `name`: Required
- Optional fields:
  - `init` - 初始化
  - `author` - 作者
  - `intro` - 简介
  - `kind` - 分类
  - `lastChapter` - 最新章节
  - `updateTime` - 更新时间
  - `coverUrl` - 封面
  - `tocUrl` - 目录页
  - `wordCount` - 字数
  - `canReName` - 可重命名
  - `downloadUrls` - 下载链接

**BookSource MUST include (BookSource.kt):**
- `bookSourceUrl`: Required (Primary Key)
- `bookSourceName`: Required
- Optional fields:
  - `bookSourceType` - 0=文本, 1=音频, 2=图片, 3=文件, 4=视频
  - `searchUrl` - 搜索URL
  - `exploreUrl` - 发现URL
  - `ruleSearch` - 搜索规则
  - `ruleExplore` - 发现规则
  - `ruleBookInfo` - 书籍信息规则
  - `ruleToc` - 目录规则
  - `ruleContent` - 正文规则
  - `ruleReview` - 段评规则
  - `header` - 请求头
  - `loginUrl` - 登录地址
  - `loginUi` - 登录UI
  - `jsLib` - JS库
  - `enabledCookieJar` - CookieJar
  - `concurrentRate` - 并发率
  - `weight` - 智能排序权重
  - `respondTime` - 响应时间
  - `lastUpdateTime` - 最后更新时间
  - `bookUrlPattern` - 详情页URL正则
  - `bookSourceGroup` - 分组
  - `customOrder` - 手动排序编号
  - `enabled` - 是否启用
  - `enabledExplore` - 启用发现
  - `loginCheckJs` - 登录检测js
  - `coverDecodeJs` - 封面解密js
  - `bookSourceComment` - 注释
  - `variableComment` - 自定义变量说明
  - `eventListener` - 是否监听事件
  - `customButton` - 自定义按钮

## Using Bundled Resources

### References (`references/`)

When detailed information is needed, load these reference files:

- `references/legado_knowledge_base.md` - Complete knowledge base
- `references/css_selector_rules.txt` - CSS selector specifications
- `references/real_book_source_examples.md` - 134 real book sources
- `references/book_source_templates.md` - Proven templates
- `references/post_request_config.md` - POST request guidelines
- `references/encoding_detection.md` - Encoding handling

**Grep patterns for large files:**
```bash
grep -r "CSS选择器格式" references/
grep -r "POST请求配置" references/
grep -r "nextContentUrl判断" references/
```

### Assets (`assets/`)

Files used in output, not loaded into context:

- `assets/book_source_database/` - Book source files
- `assets/knowledge_base/` - Knowledge files
- `assets/html_storage/` - Stored HTML samples
- Templates and example files for book source generation

## Common HTML Structures and Solutions

### Structure 1: Standard List (with cover)
```html
<div class="book-list">
  <div class="item">
    <img src="cover.jpg" class="cover"/>
    <a href="/book/1" class="title">Book Name</a>
  </div>
</div>
```

**Rule:**
```json
{
  "ruleSearch": {
    "bookList": ".book-list .item",
    "name": ".title@text",
    "bookUrl": "a@href",
    "coverUrl": "img@src"
  }
}
```

### Structure 2: Search Page (no cover, merged info)
```html
<div class="hot_sale">
  <a href="/book/1">
    <p class="title">Book Name</p>
    <p class="author">Category | Author: Name</p>
  </a>
</div>
```

**Rule:**
```json
{
  "ruleSearch": {
    "bookList": ".hot_sale",
    "name": ".title@text",
    "author": ".author.0@text##.*| |Author:##",
    "kind": ".author.0@text##\\|.*##",
    "bookUrl": "a@href",
    "coverUrl": ""
  }
}
```

### Structure 3: Lazy Loading Images
```html
<img class="lazy" data-original="cover.jpg" src="placeholder.jpg"/>
```

**Rule:**
```json
{
  "coverUrl": "img.lazy@data-original||img@src"
}
```

## Encoding Detection and Handling

**Critical Rule:** Detect encoding BEFORE fetching HTML!

```python
# Step 1: Detect encoding
detected_charset = detect_charset(url="http://example.com")

# Step 2: Use detected encoding in all requests
if detected_charset == "gbk":
    searchUrl = "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"charset\":\"gbk\"}"
else:
    searchUrl = "/search?q={{key}}"  # UTF-8 is default
```

## nextContentUrl Decision Rules

**Core Principle:** Set `nextContentUrl` ONLY for true next chapter links!

**Scenario 1: True Next Chapter (SET nextContentUrl)**
- Button links to actual next chapter (Chapter 1 → Chapter 2)
- Button text: "下一章", "下章", "下一节", "下一话"
- URL pattern: /chapter/1.html → /chapter/2.html (chapter number changes)

```json
{
  "ruleContent": {
    "nextContentUrl": "text.下一章@href"
  }
}
```

**Scenario 2: Same Chapter Pagination (LEAVE EMPTY)**
- Button splits long chapter into pages
- Button text: "下一页", "继续阅读", "翻到下一页"
- URL pattern: /chapter/1_1.html → /chapter/1_2.html (chapter number unchanged)

```json
{
  "ruleContent": {
    "nextContentUrl": ""
  }
}
```

**Scenario 3: Ambiguous Button (CHECK URL)**
- Button text unclear ("下一", "下页")
- Compare current URL with button URL
- If chapter number changes → SET
- If only page number changes → LEAVE EMPTY

## Regular Expression Formats

**Format 1: Delete matched content**
```
选择器@提取类型##正则表达式
```

**Format 2: Replace matched content**
```
选择器@提取类型##正则表达式##替换内容
```

**Format 3: Extract using capture groups**
```
选择器@提取类型##正则表达式(捕获组)##$1
```

**Examples:**
```json
{
  "author": ".author@text##.*Author:##",
  "author": ".author@text##Author:(.*)##$1",
  "content": "#content@html##<div id=\"ad\">[\\s\\S]*?</div>|Please bookmark##"
}
```

## Knowledge Base Query Examples

**Query CSS Selectors:**
```
search_knowledge("CSS选择器格式 提取类型 @text @html @ownText @textNode @href @src")
get_css_selector_rules()  # Get complete rules with pagination
```

**Query POST Requests:**
```
search_knowledge("POST请求配置 method body String() webView charset")
```

**Query Real Book Source Analysis (134 sources):**
```
get_real_book_source_examples(limit=5)  # Get top 5 examples
search_knowledge("134个真实书源分析 常用选择器 提取类型 正则模式")
```

**Most Used CSS Selectors (from 134 sources):**
- `img` (40 times) - Cover images
- `h1` (30 times) - Book titles
- `div` (13 times) - Generic containers
- `content` (12 times) - Content areas
- `intro` (11 times) - Introductions
- `h3` (9 times) - Chapter names

**Most Used Extraction Types:**
- `@href` (81 times) - Link addresses
- `@text` (72 times) - Text content
- `@src` (60 times) - Image sources
- `@html` (33 times) - HTML structure
- `@js` (25 times) - JavaScript processing

**Query Templates:**
```
get_book_source_templates(limit=3)  # Get 3 proven templates
search_knowledge("真实书源模板 69书吧 笔趣阁 起点")
```

**Query Specific Topics:**
```
search_knowledge("常见书源结构模式 标准小说站 笔趣阁 聚合源")
search_knowledge("常见陷阱 选择器误用 提取类型混淆")
search_knowledge("动态加载 webView webJs JavaScript注入")
search_knowledge("正则表达式模式 清理前缀后缀 提取特定内容")
```

**Paginated File Reading:**
```
read_file_paginated(file_path="assets/css选择器规则.txt", page=1)
list_all_knowledge_files()
```

## Output Format Requirements

**Standard JSON Array (required):**
```json
[
  {
    "bookSourceName": "Example Source",
    "bookSourceUrl": "https://example.com",
    "searchUrl": "/search?q={{key}}",
    "ruleSearch": {
      "bookList": ".book-item",
      "name": ".title@text",
      "author": ".author@text",
      "bookUrl": "a@href"
    },
    "ruleToc": {
      "chapterList": "#chapter-list li",
      "chapterName": "a@text",
      "chapterUrl": "a@href"
    },
    "ruleContent": {
      "content": "#content@html"
    }
  }
]
```

**Requirements:**
- Must be standard JSON array
- No comments
- No Markdown code blocks
- Include all required fields
- Ready for import into Legado app

## Troubleshooting

**Search returns no results:**
- Verify CSS selectors are correct
- Check if website structure changed
- Add proper headers and cookies

**Content missing:**
- Check if content is dynamically loaded
- Set correct cookies
- Add login logic if needed

**Directory order is wrong:**
- Add minus sign before list selector: `-ul.chapter-list li`

**Advertisements in content:**
- Use `@ownText` instead of `@text`
- Clean with regex: `##advertisement|推广##`

**Pagination needed:**
- Configure `nextContentUrl` for content
- Configure `nextTocUrl` for TOC

**Image hotlinking:**
- Configure Referer header in `header` field

**Encoding issues (garbled text):**
- Always detect encoding BEFORE fetching HTML
- Use detected encoding in all requests
- For GBK sites, add `"charset":"gbk"` to POST/GET requests

## Memory Mnemonics

**Selector formats:**
- Use `@text` for complete text
- Use `@ownText` for element text only (excludes children)
- Use `@html` for HTML structure
- Use `@href/@src` for links/images
- Use `@textNode` for text nodes
- Use `@js` for JavaScript processing
- Use `text.文本` for text-based selection (not `:contains()`)

**Numeric indices (from source code AnalyzeRule.kt):**
- `.0` = first element (not `:first-child`)
- `.-1` = last element (not `:last-child`)
- `.1` = second element
- `.-2` = second-to-last element

**nextContentUrl (from ContentRule.kt):**
- Chapter number changes → SET it
- Page number changes only → LEAVE EMPTY
- "下一章" means next chapter
- "下一页" means next page of same chapter

**Encoding:**
- Detect ONCE at start
- Use detected encoding throughout
- UTF-8 is default (omit charset)
- GBK must specify charset="gbk"

**Forbidden fields/selectors (confirmed in source):**
- NO `prevContentUrl` (doesn't exist in BookSource.kt)
- NO `:contains()` (use `text.文本`)
- NO `:first-child/:last-child` (use `.0/.-1`)

**Rule Processing Modes (from AnalyzeRule.kt):**
- Default → JSoup CSS selectors
- Json → JSONPath
- XPath → XPath selectors
- Js → JavaScript execution
- WebJs → WebView JavaScript

**Additional Fields (from source code):**
- `checkKeyWord` (SearchRule) - 校验关键字
- `subContent` (ContentRule) - 副文规则，拼接在正文后面
- `title` (ContentRule) - 有些网站只能在正文中获取标题
- `payAction` (ContentRule) - 购买操作
- `callBackJs` (ContentRule) - 事件监听回调
- `preUpdateJs` (TocRule) - 更新前执行
- `formatJs` (TocRule) - 格式化
- `isVolume/isVip/isPay` (TocRule) - 章节标记
- `webJs` (BookSource) - WebView JavaScript
- `imageDecode` (BookSource) - 封面解密
- `exploreScreen` (BookSource) - 发现筛选规则

## Best Practices

1. **Always query knowledge base first** - Never write rules from memory
2. **Detect encoding before fetching HTML** - Critical for proper text display
3. **Reference real examples** - Use 134 real book source analysis results
4. **Validate with real HTML** - Never assume HTML structure
5. **Handle special cases** - No cover, lazy loading, merged info
6. **Use proven templates** - Follow patterns from successful book sources
7. **Test thoroughly** - Verify each rule works correctly
8. **Document changes** - Keep track of modifications
9. **Learn continuously** - Use knowledge_learner to improve
10. **Collaborate** - Use user_intervention for complex tasks

## Advanced Features (from source code)

**Rule Processing Modes:**
- **Mode.Default**: JSoup CSS selector (standard HTML parsing)
- **Mode.Json**: JSONPath for JSON data sources
- **Mode.XPath**: XPath for XML/HTML documents
- **Mode.Js**: JavaScript evaluation with result binding
- **Mode.WebJs**: WebView-based JavaScript (for SPA/dynamic content)

**Advanced BookSource Fields:**
- **checkKeyWord**: 校验关键字，用于搜索验证
- **subContent**: 副文规则，可拼接在正文后面或获取歌词等
- **payAction**: 购买操作，支持js或包含{{js}}的url
- **callBackJs**: 事件监听回调，监听到事件后执行的js代码
- **preUpdateJs**: 更新前执行的js代码
- **formatJs**: 格式化js代码
- **imageStyle**: 图片样式（默认大小居中，FULL最大宽度）
- **imageDecode**: 图片bytes二次解密js
- **webJs**: WebView JavaScript注入（用于动态内容）
- **coverDecodeJs**: 封面解密js
- **loginCheckJs**: 登录检测js

**Learning System:**
- `knowledge_learner` - Learn from new book sources
- `knowledge_applier` - Apply learned patterns
- `knowledge_enhanced_analyzer` - Enhanced analysis with learned knowledge

**Auditing:**
- `audit_knowledge_base` - Validate knowledge base integrity
- `knowledge_auditor` - Audit specific knowledge items

**Collaboration:**
- `user_intervention` - Request user input for complex scenarios
- `collaborative_edit` - Work together on book source refinement

**Caching Mechanisms:**
- String rules cached in `stringRuleCache` HashMap
- Regular expressions cached in `regexCache` HashMap
- Scripts cached in `scriptCache` HashMap

**JSON Deserialization:**
- Rules support both JSON object and primitive string formats
- Custom JSON deserializers handle flexible input
- GSON used for all JSON serialization/deserialization

**WebSocket Debug Interface:**
- BookSourceDebugWebSocket at `ws://127.0.0.1:1235/bookSourceDebug`
- Supports real-time book source debugging
- Message format: `{key: "搜索关键词", tag: "源链接"}`
