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

### Phase 1: Information Collection (DO NOT create book source!)

**Step 1: Query Knowledge Base (MUST be first!)**
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

**Step 2: Detect Website Encoding (CRITICAL - BEFORE fetching HTML!)**
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

**Step 3: Fetch Real HTML with Correct Encoding**
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

## Critical Constraints

**Strictly Prohibited:**
1. Using `prevContentUrl` field (doesn't exist in Legado)
2. Using `:contains()` pseudo-class selectors (use `text.文本` format)
3. Using `:first-child/:last-child` pseudo-class selectors (use numeric indices .0, .-1)
4. Confusing "next page" with "next chapter" for `nextContentUrl`
5. Skipping knowledge base queries
6. Creating book sources without fetching real HTML
7. Not referencing real templates and analysis results
8. Detecting encoding multiple times (detect ONCE only)

**Field Completeness Rules:**

**ruleContent MUST include:**
- `content`: Required (chapter content extraction)
- `nextContentUrl`: Conditional (only for true next chapter links)

**ruleToc MUST include:**
- `chapterList`: Required
- `chapterName`: Required
- `chapterUrl`: Required
- `nextTocUrl`: Conditional (if pagination exists)

**ruleSearch MUST include:**
- `bookList`: Required
- `name`: Required
- `bookUrl`: Required
- Optional fields based on availability: author, kind, lastChapter, coverUrl

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
- Use `@ownText` for element text only
- Use `@html` for HTML structure
- Use `@href/@src` for links/images
- Use `text.文本` for text-based selection (not `:contains()`)

**Numeric indices:**
- `.0` = first element (not `:first-child`)
- `.-1` = last element (not `:last-child`)
- `.1` = second element
- `.-2` = second-to-last element

**nextContentUrl:**
- Chapter number changes → SET it
- Page number changes only → LEAVE EMPTY
- "下一章" means next chapter
- "下一页" means next page of same chapter

**Encoding:**
- Detect ONCE at start
- Use detected encoding throughout
- UTF-8 is default (omit charset)
- GBK must specify charset="gbk"

**Forbidden fields/selectors:**
- NO `prevContentUrl` (doesn't exist)
- NO `:contains()` (use `text.文本`)
- NO `:first-child/:last-child` (use `.0/.-1`)

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

## Advanced Features

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
