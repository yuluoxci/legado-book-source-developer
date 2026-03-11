# Legado 书源开发 - 实战经验与模式

## 目录

- [最常用的 CSS 选择器](#最常用的-css-选择器)
- [最常用的提取类型](#最常用的提取类型)
- [134 个真实书源分析总结](#134-个真实书源分析总结)
- [常见网站模式](#常见网站模式)
- [高级技巧](#高级技巧)
- [调试技巧](#调试技巧)

---

## 最常用的 CSS 选择器

基于 134 个真实书源分析，以下是最常用的选择器：

| 选择器 | 使用次数 | 说明 | 示例 |
|--------|----------|------|------|
| `img` | 40 | 封面图片 | `img@src`, `img@data-original` |
| `h1` | 30 | 书名 | `h1@text` |
| `div` | 13 | 通用容器 | `.content@text`, `div.intro@text` |
| `content` | 12 | 内容区域 | `#content@html`, `.content@text` |
| `intro` | 11 | 简介 | `.intro@text`, `#intro@text` |
| `h3` | 9 | 章节名 | `h3@text` |
| `span` | 9 | 通用元素 | `.author span@text` |
| `a` | 8 | 链接 | `a@href`, `a@text` |
| `p` | 7 | 段落 | `.info p@text` |

### 选择器使用技巧

**1. 优先使用类选择器**

```json
// ✅ 推荐
{
  "name": ".book-title@text"
}

// ⚠️ 可用
{
  "name": "div.title@text"
}

// ❌ 不推荐（过于具体）
{
  "name": "div.container div.main div.title@text"
}
```

**2. 使用 ID 选择器获取主要内容**

```json
{
  "content": "#content@html"
}
```

**3. 使用数字索引替代伪类**

```json
// ✅ 推荐
{
  "author": ".info p.0@text"
}

// ❌ Legado 不支持
{
  "author": ".info p:first-child@text"
}
```

**4. 使用文本选择器**

```json
// ✅ 推荐
{
  "nextContentUrl": "text.下一章@href"
}

// ❌ Legado 不支持
{
  "nextContentUrl": "a:contains('下一章')@href"
}
```

---

## 最常用的提取类型

基于 134 个真实书源分析：

| 提取类型 | 使用次数 | 说明 | 适用场景 |
|----------|----------|------|----------|
| `@href` | 81 | 链接地址 | 书籍链接、章节链接 |
| `@text` | 72 | 文本内容 | 书名、作者、章节名 |
| `@src` | 60 | 图片地址 | 封面图片 |
| `@html` | 33 | HTML 结构 | 正文内容（保留格式） |
| `@js` | 25 | JavaScript 处理 | 复杂逻辑 |
| `@ownText` | 8 | 仅元素文本 | 去除广告 |
| `@textNode` | 3 | 文本节点 | 特殊情况 |

### 提取类型使用技巧

**1. @text - 完整文本**

```html
<div class="title">
  <span>玄幻</span>
  <h1>修仙世界</h1>
</div>
```

```json
{
  "name": ".title@text"
  // 提取结果："玄幻修仙世界"
}
```

**2. @ownText - 仅元素文本（去除子元素）**

```html
<div class="content">
  正文内容...
  <div class="ad">广告内容</div>
</div>
```

```json
{
  "content": ".content@ownText"
  // 提取结果："正文内容..."（不包含广告）
}
```

**3. @html - 完整 HTML**

```html
<div class="content">
  <p>段落1</p>
  <p>段落2</p>
</div>
```

```json
{
  "content": ".content@html"
  // 提取结果：完整的 HTML 结构
}
```

**4. @href - 链接地址**

```html
<a href="/book/12345" class="book-link">书名</a>
```

```json
{
  "bookUrl": "a@href"
  // 提取结果："/book/12345"
}
```

**5. @src - 图片地址**

```html
<img src="https://example.com/cover.jpg" alt="封面">
```

```json
{
  "coverUrl": "img@src"
  // 提取结果："https://example.com/cover.jpg"
}
```

---

## 134 个真实书源分析总结

### 网站类型分布

| 类型 | 数量 | 占比 | 特征 |
|------|------|------|------|
| 标准小说站 | 58 | 43% | 有封面、完整信息 |
| 笔趣阁类 | 42 | 31% | 无封面、信息合并 |
| POST 请求站 | 18 | 13% | 需要 POST、可能 GBK |
| API 聚合源 | 12 | 9% | 返回 JSON 数据 |
| 动态加载站 | 4 | 3% | 需要 webView |

### 编码分布

| 编码 | 数量 | 占比 |
|------|------|------|
| UTF-8 | 118 | 88% |
| GBK | 14 | 10% |
| GB2312 | 2 | 2% |

**结论：**
- UTF-8 是主流（默认，无需指定）
- GBK 需要添加 `charset="gbk"`

### 搜索页特征

| 特征 | 数量 | 占比 |
|------|------|------|
| 有封面图片 | 67 | 50% |
| 无封面图片 | 67 | 50% |
| 信息合并 | 45 | 34% |
| 懒加载图片 | 23 | 17% |

### ruleSearch 字段使用频率

| 字段 | 使用次数 | 占比 |
|------|----------|------|
| bookList | 134 | 100% |
| name | 134 | 100% |
| bookUrl | 134 | 100% |
| author | 128 | 96% |
| coverUrl | 67 | 50% |
| kind | 98 | 73% |
| lastChapter | 89 | 66% |

---

## 常见网站模式

### 模式 1：标准小说站（最常见）

**特征：**
- ✅ 有封面图片
- ✅ 信息完整独立
- ✅ 结构清晰

**HTML 示例：**
```html
<div class="book-list">
  <div class="item">
    <img src="cover.jpg" class="cover"/>
    <h3 class="title">修仙世界</h3>
    <p class="author">作者：张三</p>
    <p class="kind">玄幻</p>
    <p class="last-chapter">最新：第一章</p>
    <a href="/book/12345" class="detail-link">详情</a>
  </div>
</div>
```

**规则示例：**
```json
{
  "ruleSearch": {
    "bookList": ".book-list .item",
    "name": ".title@text",
    "author": ".author@text##作者：##",
    "kind": ".kind@text",
    "lastChapter": ".last-chapter@text##最新：##",
    "bookUrl": "a@href",
    "coverUrl": "img@src"
  }
}
```

---

### 模式 2：笔趣阁类（无封面）

**特征：**
- ❌ 无封面图片
- ✅ 信息可能合并
- ⚠️ 需要正则拆分

**HTML 示例：**
```html
<div class="result-list">
  <tr>
    <td class="title"><a href="/book/12345">修仙世界</a></td>
    <td class="author">张三</td>
    <td class="kind">玄幻</td>
    <td class="update">2024-01-01</td>
  </tr>
</div>
```

**规则示例：**
```json
{
  "ruleSearch": {
    "bookList": ".result-list tr",
    "name": "td.title a@text",
    "author": "td.author@text",
    "kind": "td.kind@text",
    "bookUrl": "a@href",
    "coverUrl": ""
  }
}
```

---

### 模式 3：信息合并

**特征：**
- ⚠️ 多个信息在一个元素中
- ⚠️ 需要正则表达式拆分

**HTML 示例：**
```html
<div class="hot_sale">
  <a href="/book/12345">
    <p class="title">修仙世界</p>
    <p class="info">玄幻 | 作者：张三 | 2024-01-01</p>
  </a>
</div>
```

**规则示例：**
```json
{
  "ruleSearch": {
    "bookList": ".hot_sale",
    "name": ".title@text",
    "author": ".info@text##.*\\| |作者：##",
    "kind": ".info@text##([^|]+)\\|.*##$1",
    "bookUrl": "a@href",
    "coverUrl": ""
  }
}
```

**正则解释：**
```
##.*\\| |作者：##
删除第一个"|"及其前面的内容，再删除"作者："

##([^|]+)\\|.*##$1
提取第一个"|"前面的内容
```

---

### 模式 4：懒加载图片

**特征：**
- ⚠️ 图片使用 `data-original` 属性
- ⚠️ 需要备用方案

**HTML 示例：**
```html
<img class="lazy" data-original="real.jpg" src="placeholder.jpg"/>
```

**规则示例：**
```json
{
  "coverUrl": "img@data-original||img@src"
}
```

**说明：**
- 先尝试 `data-original`
- 如果不存在，使用 `src`
- `||` 表示"或"

---

### 模式 5：POST 请求 + GBK

**特征：**
- ⚠️ 需要 POST 请求
- ⚠️ 使用 GBK 编码

**规则示例：**
```json
{
  "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"charset\":\"gbk\"}"
}
```

---

### 模式 6：API 聚合源

**特征：**
- ✅ 返回 JSON 数据
- ✅ 结构清晰
- ⚠️ 可能需要特殊处理

**响应示例：**
```json
{
  "code": 0,
  "data": [
    {
      "name": "修仙世界",
      "author": "张三",
      "url": "/book/12345",
      "cover": "cover.jpg"
    }
  ]
}
```

**规则示例：**
```json
{
  "searchUrl": "/api/search?q={{key}}",
  "ruleSearch": {
    "bookList": "$.data[*]",
    "name": "$.name",
    "author": "$.author",
    "bookUrl": "$.url",
    "coverUrl": "$.cover"
  }
}
```

---

### 模式 7：动态加载

**特征：**
- ⚠️ 内容需要 JavaScript 渲染
- ⚠️ 可能需要 webView

**规则示例：**
```json
{
  "searchUrl": "/search,{\"webView\":true,\"webJs\":\"setTimeout(function(){window.location.href='/search?q={{key}}'},1000)\"}"
}
```

---

### 模式 8：分页目录

**特征：**
- ⚠️ 目录有多页
- ⚠️ 需要配置 nextTocUrl

**规则示例：**
```json
{
  "ruleToc": {
    "chapterList": ".chapter-list a",
    "chapterName": "@text",
    "chapterUrl": "@href",
    "nextTocUrl": "text.下一页@href"
  }
}
```

---

## 高级技巧

### 技巧 1：使用 || 提供备选方案

```json
{
  "coverUrl": "img@data-original||img@data-src||img@src"
}
```

说明：
- 依次尝试 `data-original`、`data-src`、`src`
- 使用第一个存在的值

---

### 技巧 2：使用 ## 清理多个内容

```json
{
  "author": ".info@text##请收藏本站|本章完|继续阅读"
}
```

说明：
- 使用 `|` 分隔多个清理规则
- 删除所有匹配的内容

---

### 技巧 3：使用正则提取特定内容

```json
{
  "author": ".info@text##作者：(.*)##$1"
}
```

说明：
- 提取"作者："后面的内容
- `$1` 表示第一个捕获组

---

### 技巧 4：使用多个规则组合

```json
{
  "name": ".title@text##《##"  // 删除开头的"《"
}
```

---

### 技巧 5：处理多个同名元素

```html
<div class="info">
  <span>分类</span>
  <span>作者</span>
  <span>状态</span>
</div>
```

```json
{
  "kind": ".info span.0@text",
  "author": ".info span.1@text",
  "status": ".info span.2@text"
}
```

---

### 技巧 6：处理嵌套链接

```html
<div class="item">
  <a href="/book/12345">
    <img src="cover.jpg"/>
    <h3>书名</h3>
  </a>
</div>
```

```json
{
  "bookList": ".item",
  "name": "h3@text",
  "bookUrl": "a@href",
  "coverUrl": "img@src"
}
```

---

### 技巧 7：处理相对路径

如果链接是相对路径，Legado 会自动处理：

```html
<a href="/book/12345">详情</a>
```

```json
{
  "bookUrl": "a@href"
  // Legado 会自动拼接完整 URL
}
```

---

### 技巧 8：处理空值

如果某些字段不存在，可以留空：

```json
{
  "ruleSearch": {
    "bookList": ".item",
    "name": ".title@text",
    "author": ".author@text",
    "coverUrl": ""  // 搜索页没有封面
  }
}
```

---

## 调试技巧

### 技巧 1：使用浏览器开发者工具

1. 按 F12 打开开发者工具
2. 使用 Ctrl+Shift+C 选择元素
3. 右键 → Copy → Copy selector

### 技巧 2：验证选择器

在控制台输入：

```javascript
document.querySelectorAll('.book-list .item')
```

查看返回的元素数量是否正确。

### 技巧 3：测试提取结果

```javascript
document.querySelector('.title').textContent
document.querySelector('.title').href
document.querySelector('img').src
```

### 技巧 4：使用 Network 面板

1. 打开 Network 面板
2. 执行搜索操作
3. 查看请求的 URL、方法、参数

### 技巧 5：查看响应内容

在 Network 面板中：
1. 点击请求
2. 查看 Response 标签
3. 分析返回的 HTML 或 JSON

---

## 常见问题

### Q1：为什么有些书源使用 @html 而不是 @text？

**A：** `@html` 保留 HTML 结构，适用于正文内容。`@text` 只提取纯文本。

---

### Q2：如何处理多个相同的选择器？

**A：** 使用数字索引：`.0`（第一个）、`.-1`（最后一个）、`.1`（第二个）。

---

### Q3：为什么有些书源的 coverUrl 是空的？

**A：** 搜索页可能没有封面图片，这是正常的。

---

### Q4：如何处理 GBK 编码的网站？

**A：** 在 searchUrl 中添加 `"charset":"gbk"`。

---

### Q5：nextContentUrl 什么时候设置？

**A：** 只有真正跳转到下一章节时才设置。同一章节的分页不要设置。

---

## 下一步

- 阅读 [css_selector_rules.md](css_selector_rules.md) 了解完整的 CSS 选择器规则
- 查看 [book_source_templates.md](book_source_templates.md) 获取 8 个真实模板
- 使用 [tools/analyze_fhysc.py](../tools/analyze_fhysc.py) 分析你的目标网站
