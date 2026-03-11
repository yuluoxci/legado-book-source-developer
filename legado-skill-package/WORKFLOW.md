# Legado 书源开发 - 完整工作流程

## 概述

本工作流程分为三个阶段，确保创建的书源可靠可用：

- **阶段 1：收集信息** - 查询知识库、检测编码、获取 HTML
- **阶段 2：严格审查** - 编写规则、验证语法、处理特殊情况
- **阶段 3：创建书源** - 生成 JSON、导入测试

---

## 阶段 1：收集信息

**目标：** 收集所有必要信息，但不创建书源

### 步骤 1.1：查询知识库

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

4. **POST 请求配置**（如果网站使用 POST）
   - 文件：`references/post_request_config.md`
   - 了解：method, body, charset 配置

**查询示例：**
```bash
cat references/css_selector_rules.md | grep "@text"
cat references/book_source_templates.md | grep "笔趣阁"
```

### 步骤 1.2：检测网站编码

**为什么重要：**
- 中文网站可能使用 GBK 编码
- 不检测会导致中文乱码
- 编码只需要检测一次

**检测方法：**

```bash
cd tools
python analyze_fhysc.py
```

**输出示例：**
```
状态码: 200
响应编码: GBK
Content-Type: text/html; charset=gbk
实际编码: GBK
```

**记录检测结果：**
- 如果是 GBK → 后续所有请求都要加 `"charset":"gbk"`
- 如果是 UTF-8 → 不需要指定（默认）

**重要原则：**
1. 编码只需要检测一次
2. 在流程开始时检测
3. 后续所有操作都使用这个编码
4. 避免重复检测

### 步骤 1.3：获取真实 HTML

**使用检测到的编码获取 HTML：**

```bash
cd tools

# 获取搜索页
python get_book_detail.py

# 获取章节内容
python get_chapter.py
```

**关键检查清单：**

- [ ] 使用正确的 HTTP 方法（GET 或 POST）
- [ ] 使用正确的编码（UTF-8 或 GBK）
- [ ] 获取完整 HTML 源代码（不截断）
- [ ] 检查懒加载（data-original vs src）
- [ ] 检查搜索页是否有封面图片
- [ ] 永久保存 HTML 供后续分析

**HTML 保存示例：**
```bash
# 搜索页
fhysc_search_page.html

# 书籍详情页
fhysc_book_detail.html

# 章节内容页
fhysc_chapter_content.html
```

### 步骤 1.4：分析 HTML 结构

**使用浏览器开发者工具或分析工具：**

```bash
cd tools
python analyze_fhysc.py
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
