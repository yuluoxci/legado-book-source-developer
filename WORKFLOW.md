# Legado 书源开发 - 完整工作流程

## 概述

本工作流程分为三个阶段，确保创建的书源可靠可用：

- **阶段 1：收集信息** - 获取真实源码、分析JS、验证接口
- **阶段 2：严格审查** - 编写规则、验证语法、处理特殊情况
- **阶段 3：创建书源** - 生成 JSON、导入测试

## ⚠️ 核心原则

### 绝对禁止

- ❌ **禁止基于假设进行分析**
- ❌ **禁止不获取真实HTML源码就编写规则**
- ❌ **禁止不分析JavaScript就推断搜索接口参数**
- ❌ **禁止不确定时继续下一步**

### 必须做到

- ✅ **必须获取并分析真实HTML源码**
- ✅ **必须分析网站的JavaScript代码**
- ✅ **必须通过浏览器Network面板验证真实请求**
- ✅ **不确定时必须询问用户并提供建议**

### 工作流程图

```
阶段1：收集信息
├─ 获取真实HTML源码（必须）
├─ 分析JavaScript代码（必须）
├─ 验证搜索接口（必须）
├─ 遇到不确定的情况？
│   ├─ 是 → 询问用户，提供建议 → 等待用户回复 → 继续分析
│   └─ 否 → 继续下一步
└─ 完成信息收集

阶段2：严格审查
├─ 基于真实源码编写规则
├─ 验证每个选择器
├─ 处理特殊情况
└─ 完成规则编写

阶段3：创建书源
├─ 生成完整JSON
├─ 导入测试
└─ 验证功能
```

---

## 阶段 1：收集信息

**目标：** 基于真实源码收集所有必要信息

### ⭐ 步骤 1：使用核心工具快速分析（推荐）

**这是最快速、最准确的方法！**

```bash
cd tools
python quick_analyze.py https://www.example.com
```

**工具会自动完成：**
1. ✓ 检测网站编码
2. ✓ 下载并分析JavaScript文件
3. ✓ 搜索可能的搜索接口模式
4. ✓ 分析HTML结构
5. ✓ **保存HTML到 `references/html_storage/`**
6. ✓ **生成HTML元数据JSON**
7. ✓ 测试搜索接口
8. ✓ 生成结构化的JSON分析报告
9. ✓ **生成符合JSON格式的书源草稿**

**输出文件：**
```
tools/
├── book_source_时间戳.json        # 书源JSON草稿
└── analysis_report_时间戳.json   # 分析报告

references/html_storage/
├── abc123.html                    # HTML文件
├── abc123.meta.json              # HTML元数据
├── def456.js                     # JavaScript文件
└── def456.js.meta.json           # JS元数据
```

**html_storage 结构：**
```
references/html_storage/
├── {md5_hash}.html          # HTML文件
├── {md5_hash}.meta.json    # HTML元数据（URL、大小、时间戳等）
├── {md5_hash}.js           # JavaScript文件
└── {md5_hash}.js.meta.json # JS元数据
```

**元数据JSON格式：**
```json
{
  "url": "https://www.example.com",
  "size": 11041,
  "timestamp": 1771407694.9349854,
  "datetime": "2026-03-13T10:34:54.934985",
  "page_type": "home",
  "storage_path": "references/html_storage/abc123.html"
}
```

### ⭐ 步骤 2：验证书源JSON格式（必须！）

```bash
cd tools
python validate_book_source.py book_source_时间戳.json
```

**验证规则：**
- ✅ 必须是JSON数组格式
- ✅ 必须包含所有23个书源级别必需字段
- ✅ 必须包含ruleSearch的9个必需字段
- ✅ 必须包含ruleToc的5个必需字段
- ✅ 必须包含ruleContent的7个必需字段
- ✅ 字段类型必须正确

**验证输出示例：**
```
======================================================================
验证书源JSON: book_source.json
======================================================================
✓ 找到 1 个书源

--- 验证书源 1/1 ---
  书源名称: 示例书源
  书源URL: https://www.example.com
  bookList: .book-list
  bookUrl: a@href
  name: .title@text
  author: .author@text
  coverUrl: img@src

======================================================================
验证结果
======================================================================

✓ 验证通过！书源JSON格式正确
```

### 步骤 3：查看分析报告

```bash
cd tools
cat analysis_report_时间戳.json
```

### 步骤 4：查看保存的HTML文件

```bash
# 查看HTML
cat references/html_storage/abc123.html

# 查看元数据
cat references/html_storage/abc123.meta.json
```

### ⚠️ 步骤 5：如果工具失败，使用手动方法

**5.1 使用浏览器开发者工具获取真实请求**

**这是最关键的步骤！**

**打开开发者工具：**
1. 打开目标网站
2. 按F12打开开发者工具
3. 切换到 Network 标签

**执行搜索操作：**
1. 在网站中执行一次搜索
2. 在 Network 中找到搜索请求
3. 右键点击请求 → Copy → Copy as cURL

**记录以下信息：**
```
Request URL: ______________________
Request Method: __________________
Request Headers: __________________
  - User-Agent: __________________
  - Content-Type: __________________
  - 其他重要请求头：__________________
Request Body: __________________
  （如果是POST请求）
Response: __________________
  - 状态码：__________________
  - Content-Type：__________________
  - 响应内容：__________________
```

**使用Python工具分析cURL：**
```bash
cd tools
python js_param_analyzer.py --curl '复制的cURL命令'
```

**5.2 获取并保存真实HTML源码到html_storage**

**保存HTML函数：**
```python
from pathlib import Path
import hashlib
import json
import time
from datetime import datetime

# 创建存储目录
storage_dir = Path('references/html_storage')
storage_dir.mkdir(parents=True, exist_ok=True)

# 保存HTML函数
def save_html(url, content, page_type='page'):
    file_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    html_file = storage_dir / f"{file_hash}.html"
    meta_file = storage_dir / f"{file_hash}.meta.json"
    
    # 保存HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 生成元数据
    metadata = {
        'url': url,
        'size': len(content),
        'timestamp': time.time(),
        'datetime': datetime.now().isoformat(),
        'page_type': page_type,
        'storage_path': str(html_file.relative_to(storage_dir.parent))
    }
    
    # 保存元数据JSON
    with open(meta_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    return html_file, metadata

# 获取并保存首页
import requests
headers = {'User-Agent': 'Mozilla/5.0...'}
response = requests.get('https://example.com', headers=headers)

html_file, metadata = save_html('https://example.com', response.text, 'home')
print(f"✓ 首页已保存: {html_file}")
print(f"✓ 元数据: {metadata}")
```

**必须获取的页面：**
```python
# 1. 首页
save_html('https://example.com', home_html, 'home')

# 2. 搜索页（包含搜索结果的HTML）
save_html('https://example.com/search?q=test', search_html, 'search')

# 3. 书籍详情页
save_html('https://example.com/book/123', detail_html, 'detail')

# 4. 目录页
save_html('https://example.com/book/123/toc', toc_html, 'toc')

# 5. 章节内容页
save_html('https://example.com/chapter/1', content_html, 'content')
```

**5.3 分析JavaScript代码**

**使用JS参数分析工具：**
```bash
cd tools
python js_param_analyzer.py --analyze https://www.example.com
```

**工具会自动完成：**
1. ✓ 提取所有JavaScript代码
2. ✓ 查找搜索相关函数
3. ✓ 查找API端点
4. ✓ 查找参数生成函数
5. ✓ 查找加密库引用
6. ✓ 生成参数分析报告

### 步骤 1.3：查询知识库（参考已有知识）

**必须查询的内容：**

1. **CSS 选择器规则**
   - 文件：`references/css_selector_rules.md`
   - 了解：选择器格式、提取类型、正则表达式
   - 重点：@text, @html, @href, @src 的区别

2. **书源模板**
   - 文件：`references/book_source_templates.md`
   - 了解：8 个真实模板的适用场景
   - 重点：找到与你目标网站相似的模板

3. **真实书源分析**
   - 文件：`references/real_book_source_examples.md`
   - 了解：134 个真实书源的模式
   - 重点：最常用的选择器和提取类型

4. **用户交互指南**（重要！）
   - 文件：`references/用户交互指南.md`
   - 了解：遇到不确定情况如何处理
   - 重点：何时询问用户，如何提供建议

**查询示例：**
```bash
cat references/css_selector_rules.md | grep "@text"
cat references/book_source_templates.md | grep "笔趣阁"
cat references/用户交互指南.md | grep "不确定"
```

### 步骤 1.4：验证搜索接口（必须！）

**基于真实Network请求验证：**

```python
import requests

# 从cURL中提取的信息
url = "https://api.example.com/search"
headers = {
    'User-Agent': 'Mozilla/5.0...',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'keyword': '斗破苍穹',
    'page': 1
}

response = requests.post(url, json=data, headers=headers)
print(f"状态码: {response.status_code}")
print(f"响应: {response.text[:500]}")
```

**检查清单：**
- [ ] URL是否正确
- [ ] 方法（GET/POST）是否正确
- [ ] 请求头是否完整
- [ ] 参数是否正确
- [ ] 响应是否包含搜索结果

**如果失败，查阅 `references/用户交互指南.md` 中的场景1和场景3**

### 步骤 1.5：分析HTML结构（必须基于真实HTML！）

**不要猜测！基于保存的HTML文件分析：**

```python
from bs4 import BeautifulSoup

# 加载真实HTML
with open('search.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 查找书籍列表
book_items = soup.select('.book-list .item, .result-list li')
if book_items:
    print(f"✓ 找到 {len(book_items)} 个书籍项")
    # 打印第一个书籍项的结构
    print(book_items[0].prettify())
else:
    print("✗ 未找到书籍列表，需要查找其他选择器")

# 查找常见元素
common_selectors = {
    '书籍列表': ['.book-list', '.result-list', '.hot-sale'],
    '书名': ['.title', 'h1', 'h3', 'a'],
    '作者': ['.author', '.writer', '.by'],
    '封面': ['img', '.cover', '.book-cover']
}

for label, selectors in common_selectors.items():
    for selector in selectors:
        elements = soup.select(selector)
        if elements:
            print(f"✓ {label} ({selector}): {len(elements)} 个")
            break
```

**需要识别的内容：**

#### 1. 搜索页结构
```
书籍列表容器：.book-list, .result-list, ul.hot_sale
书籍名称：.title, h3, a@text
作者信息：.author, p.1, span@text
分类信息：.kind, .category
封面图片：img@src, img@data-original
最新章节：.last-chapter, .update
书籍链接：a@href
```

#### 2. 书籍详情页结构
```
书名：h1, .book-title, #main h1
作者：.author, #info p.1
简介：.intro, #intro, .summary
封面：.cover img@src, img@data-original
分类：.kind, .category, .tags
状态：.status, #info p.2
最新章节：.last-chapter, .update
```

#### 3. 目录页结构
```
章节列表：#chapter-list, #list, .chapter-list
章节名称：a@text, dd a@text
章节链接：a@href, a@textNode
下一页按钮：text.下一页@href, .next-page@href
```

#### 4. 内容页结构
```
正文内容：#content, .content, #txt
下一章按钮：text.下一章@href, .next-chapter@href
章节标题：.title, h1@text
```

**特殊情况识别：**

- [ ] 搜索页没有封面图片 → `coverUrl: ""`
- [ ] 图片使用懒加载 → `img@data-original||img@src`
- [ ] 作者和分类信息合并 → 使用正则表达式拆分
- [ ] 信息包含广告 → 使用 `@ownText` 或正则清理
- [ ] 有分页 → 配置 `nextTocUrl` 或 `nextContentUrl`

### 步骤 1.6：遇到不确定的情况？询问用户！

**不要继续！先查阅 `references/用户交互指南.md`**

**常见的需要询问的情况：**

1. ❌ 无法确定搜索接口参数生成方式
   → 查阅：场景1 - 搜索接口参数来源不明

2. ❌ HTML结构复杂或有动态加载
   → 查阅：场景2 - HTML结构复杂或有动态加载

3. ❌ 检测到反爬虫机制
   → 查阅：场景3 - 检测到反爬虫机制

4. ❌ GBK编码导致乱码
   → 查阅：场景4 - GBK编码导致乱码

5. ❌ 找不到书籍列表容器
   → 查阅：场景5 - 找不到书籍列表容器

6. ❌ nextContentUrl判断不明确
   → 查阅：场景6 - nextContentUrl判断不明确

7. ❌ 封面图片使用懒加载
   → 查阅：场景7 - 封面图片使用懒加载

8. ❌ 作者和分类信息合并
   → 查阅：场景8 - 作者和分类信息合并

**询问格式：**
```
【问题】简洁描述问题

观察到的现象：
- ✓ 发现1
- ✓ 发现2
- ✗ 问题点

【建议/分析】
- 分析1
- 分析2

请用户提供：
- 需要的信息1
- 需要的信息2
```

**等待用户回复后再继续！**

---

## 阶段 2：严格审查

**目标：** 基于收集的信息编写和验证规则

### 步骤 2.1：编写规则

**参考资源：**
1. `references/book_source_templates.md` - 选择合适的模板
2. `references/real_book_source_examples.md` - 参考真实案例
3. 阶段 1 获取的真实 HTML

**编写原则：**

1. **参考模板，而不是从零开始**
2. **使用阶段 1 检测到的编码**
3. **处理识别到的特殊情况**
4. **使用最常用的选择器和提取类型**

**最常用的选择器（来自 134 个真实书源）：**
```
img        - 40 次 - 封面图片
h1         - 30 次 - 书名
div        - 13 次 - 通用容器
content    - 12 次 - 内容区域
intro      - 11 次 - 简介
h3         - 9 次 - 章节名
span       - 9 次 - 通用元素
```

**最常用的提取类型：**
```
@href  - 81 次 - 链接地址
@text  - 72 次 - 文本内容
@src   - 60 次 - 图片地址
@html  - 33 次 - HTML 结构
@js    - 25 次 - JavaScript 处理
```

### 步骤 2.2：验证规则语法

**检查清单：**

#### CSS 选择器格式
- [ ] 格式正确：`CSS选择器@提取类型`
- [ ] 选择器有效（在浏览器控制台测试）
- [ ] 提取类型正确（@text, @html, @href, @src 等）

#### 提取类型验证
- [ ] @text - 需要完整文本
- [ ] @html - 需要保留格式
- [ ] @ownText - 需要去广告
- [ ] @href - 提取链接
- [ ] @src - 提取图片

#### 正则表达式格式
- [ ] 格式正确：`##正则表达式##替换内容`
- [ ] 使用 `##` 作为分隔符
- [ ] 捕获组使用 `()`，引用用 `$1`, `$2`

#### JSON 结构完整性
- [ ] bookSourceName - 书源名称
- [ ] bookSourceUrl - 书源地址
- [ ] searchUrl - 搜索地址
- [ ] ruleSearch - 搜索规则
- [ ] ruleBookInfo - 书籍信息规则
- [ ] ruleToc - 目录规则
- [ ] ruleContent - 内容规则

### 步骤 2.3：处理特殊情况

**情况 1：搜索页没有封面图片**

```json
{
  "ruleSearch": {
    "coverUrl": ""
  }
}
```

**情况 2：懒加载图片**

```json
{
  "coverUrl": "img@data-original||img@src"
}
```

**情况 3：作者和分类信息合并**

```html
<p class="info">玄幻 | 作者：张三</p>
```

```json
{
  "author": ".info@text##.*\\| |作者：##",
  "kind": ".info@text##\\|.*##"
}
```

**情况 4：信息包含广告**

```html
<div class="content">
  正文内容...
  <div class="ad">广告内容</div>
</div>
```

```json
{
  "content": ".content@ownText"
}
```

或使用正则：

```json
{
  "content": ".content@html##<div class=\"ad\">[\\s\\S]*?</div>##"
}
```

**情况 5：多个同名元素**

```html
<ul class="book-list">
  <li>书籍 1</li>
  <li>书籍 2</li>
</ul>
```

```json
{
  "bookList": ".book-list li.0"  // 第一个
}
```

或：

```json
{
  "bookList": ".book-list li.-1"  // 最后一个
}
```

**情况 6：文本选择器（替代 :contains()）**

```html
<a href="/chapter/2">下一章</a>
```

```json
{
  "nextContentUrl": "text.下一章@href"
}
```

**情况 7：GBK 编码**

```json
{
  "searchUrl": "/search?q={{key}},{\"charset\":\"gbk\"}"
}
```

或 POST 请求：

```json
{
  "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"charset\":\"gbk\"}"
}
```

### 步骤 2.4：nextContentUrl 判断

**核心原则：** 只有真正跳转到下一章节时才设置！

**判断流程：**

1. 查看按钮文字
2. 对比当前 URL 和按钮 URL
3. 判断章节号是否变化

**场景 1：真正的下一章（必须设置）**

```
按钮文字：下一章、下章、下一节、下一话
当前 URL：/chapter/1.html
按钮 URL：/chapter/2.html
章节号：1 → 2（变化）
结论：设置 nextContentUrl
```

```json
{
  "ruleContent": {
    "nextContentUrl": "text.下一章@href"
  }
}
```

**场景 2：同一章节分页（必须留空）**

```
按钮文字：下一页、继续阅读、翻到下一页
当前 URL：/chapter/1_1.html
按钮 URL：/chapter/1_2.html
章节号：1 → 1（不变）
页码：1 → 2（变化）
结论：nextContentUrl 留空
```

```json
{
  "ruleContent": {
    "nextContentUrl": ""
  }
}
```

**场景 3：模糊按钮（需要 URL 判断）**

```
按钮文字：下一、下页
判断方法：对比当前 URL 和按钮 URL
- 章节号变化 → 设置
- 页码变化 → 留空
```

---

## 阶段 3：创建书源

**目标：** 生成完整的书源 JSON

### 步骤 3.1：准备完整书源 JSON

**包含所有必需字段：**

```json
[
  {
    "bookSourceName": "书源名称",
    "bookSourceUrl": "https://example.com",
    "searchUrl": "/search?q={{key}}",
    "ruleSearch": {
      "bookList": ".book-list .item",
      "name": ".title@text",
      "author": ".author@text",
      "kind": ".kind@text",
      "lastChapter": ".last-chapter@text",
      "bookUrl": "a@href",
      "coverUrl": "img@src"
    },
    "ruleBookInfo": {
      "name": "h1@text",
      "author": ".author@text",
      "kind": ".kind@text",
      "intro": ".intro@text",
      "coverUrl": ".cover img@src",
      "tocUrl": ""
    },
    "ruleToc": {
      "chapterList": "#chapter-list li",
      "chapterName": "a@text",
      "chapterUrl": "a@href",
      "nextTocUrl": ""
    },
    "ruleContent": {
      "content": "#content@html",
      "nextContentUrl": ""
    }
  }
]
```

**确保：**
- [ ] 所有必需字段都包含
- [ ] 使用阶段 2 编写的规则
- [ ] 特殊情况已处理
- [ ] 编码配置正确
- [ ] JSON 格式正确（无注释、无多余逗号）

### 步骤 3.2：输出标准 JSON

**格式要求：**
- 标准 JSON 数组
- 无注释
- 无 Markdown 代码块
- 包含所有必需字段
- 可以直接导入 Legado

**输出示例：**

```json
[
  {
    "bookSourceName": "fhysc",
    "bookSourceUrl": "https://www.fhysc.com",
    "searchUrl": "/user/search.html?q={{key}}",
    "ruleSearch": {
      "bookList": ".book-list .item",
      "name": ".title@text",
      "author": ".author@text",
      "bookUrl": "a@href",
      "coverUrl": "img@src"
    },
    "ruleBookInfo": {
      "name": "h1@text",
      "author": ".author@text",
      "intro": ".intro@text"
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

### 步骤 3.3：导入测试

1. 打开 Legado APP
2. 进入"书源管理"
3. 点击"+"导入书源
4. 复制上面的 JSON 并粘贴
5. 保存并测试

**测试清单：**
- [ ] 搜索功能正常
- [ ] 搜索结果正确显示
- [ ] 书籍详情正确
- [ ] 目录列表正确
- [ ] 章节内容正确
- [ ] 下一章功能正常（如果配置了）

---

### ⭐ 步骤 3.4：上传书源到图床（可选）

如果需要分享书源给他人，可以使用上传工具生成直链：

```bash
# 进入tools目录
cd tools

# 上传书源（使用默认配置 - 鲸落图床）
python upload_book_source.py book_source_1678901234.json
```

**输出示例：**

```
============================================================
  ✅ 书源上传成功！
============================================================

📚 书源信息:
  名称: 示例书源
  地址: https://www.example.com
  分组: 小说

📤 上传信息:
  服务: 鲸落图床
  时间: 2026-03-13 10:30:45
  压缩: 否

🔗 下载链接:
  https://tu.406np.xyz/files/abc123def456.json

💡 使用方法:
  方法1: 复制链接后，在阅读APP中点击"导入书源"，粘贴链接
  方法2: 直接打开链接，长按分享到阅读APP
  💡 提示：可以将链接生成二维码，扫描即可导入

============================================================
```

**使用场景：**
- 分享书源给朋友
- 备份书源到云端
- 在社区发布书源

**自定义上传配置：**

如果需要使用其他图床服务，创建配置文件（例如 `my_upload_config.json`）：

```json
{
  "compress": false,
  "downloadUrlRule": "$.data.links.url",
  "summary": "自定义图床",
  "uploadUrl": "https://your-image-host.com/api/upload",
  "method": "POST",
  "headers": {
    "Accept": "application/json",
    "Authorization": "Bearer YOUR_TOKEN"
  },
  "body": {
    "file": "fileRequest",
    "folder": "book_sources"
  },
  "type": "multipart/form-data"
}
```

然后使用自定义配置上传：

```bash
python upload_book_source.py book_source.json my_upload_config.json
```

**详细使用说明** → 查看 `tools/工具使用说明.md` 中的 `upload_book_source.py` 章节

---

## 检查清单总结

### 阶段 1：收集信息

- [ ] 查询 CSS 选择器规则
- [ ] 查看书源模板
- [ ] 查看真实书源分析
- [ ] 检测网站编码
- [ ] 获取搜索页 HTML
- [ ] 获取书籍详情页 HTML
- [ ] 获取目录页 HTML
- [ ] 获取内容页 HTML
- [ ] 分析 HTML 结构
- [ ] 识别特殊情况

### 阶段 2：严格审查

- [ ] 选择合适的模板
- [ ] 编写 CSS 选择器规则
- [ ] 验证选择器格式
- [ ] 验证提取类型
- [ ] 验证正则表达式
- [ ] 验证 JSON 结构
- [ ] 处理无封面情况
- [ ] 处理懒加载图片
- [ ] 处理信息合并
- [ ] 处理广告内容
- [ ] 判断 nextContentUrl

### 阶段 3：创建书源

- [ ] 准备完整 JSON
- [ ] 包含所有必需字段
- [ ] 应用编写的规则
- [ ] 配置正确的编码
- [ ] 输出标准 JSON
- [ ] 导入测试
- [ ] 验证所有功能
- [ ] （可选）上传书源到图床

---

## 常见错误

### ❌ 错误 1：不查询知识库直接写规则

**后果：** 容易遗漏细节，规则不完善

**正确做法：** 先查询知识库，参考真实模板

---

### ❌ 错误 2：不检测编码

**后果：** 中文乱码

**正确做法：** 在阶段 1 检测编码，全程使用

---

### ❌ 错误 3：不获取真实 HTML

**后果：** 规则基于假设，容易出错

**正确做法：** 必须获取真实 HTML 分析

---

### ❌ 锌误 4：使用不存在的字段

```json
{
  "prevContentUrl": "/prev"  // ❌ Legado 中不存在
}
```

**正确做法：** 使用 `nextContentUrl` 或留空

---

### ❌ 错误 5：使用 :contains() 选择器

```json
{
  "nextContentUrl": "a:contains('下一章')@href"  // ❌ Legado 不支持
}
```

**正确做法：** 使用文本选择器

```json
{
  "nextContentUrl": "text.下一章@href"  // ✅
}
```

---

### ❌ 错误 6：使用 :first-child/:last-child

```json
{
  "bookList": ".book-list a:first-child"  // ❌ Legado 不支持
}
```

**正确做法：** 使用数字索引

```json
{
  "bookList": ".book-list a.0"  // ✅
}
```

---

### ❌ 错误 7：混淆"下一页"和"下一章"

```json
{
  // 同一章节分页，不应该设置
  "nextContentUrl": "text.下一页@href"
}
```

**正确做法：** 判断章节号是否变化

```json
{
  // 章节号变化，才设置
  "nextContentUrl": "text.下一章@href"
}
```

---

## 学习资源

1. **QUICKSTART.md** - 5 分钟快速开始
2. **references/css_selector_rules.md** - CSS 选择器完整规范
3. **references/book_source_templates.md** - 8 个真实模板
4. **references/real_book_source_examples.md** - 134 个真实书源分析
5. **references/troubleshooting.md** - 问题排查指南
6. **tools/** - 分析工具集合

## 下一步

1. 阅读 [QUICKSTART.md](QUICKSTART.md) 快速上手
2. 使用 [tools/analyze_fhysc.py](tools/analyze_fhysc.py) 分析你的目标网站
3. 参考 [references/book_source_templates.md](references/book_source_templates.md) 选择模板
4. 遵循本工作流程创建你的第一个书源
