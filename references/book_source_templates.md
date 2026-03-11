# Legado Book Source Templates

This file contains proven book source templates extracted from real-world book sources. These templates have been tested and are ready for use as starting points.

## Template 1: 标准小说站（完整版）

适用于结构完整的小说网站，包含封面、作者、分类、简介等信息。

```json
[
  {
    "bookSourceComment": "标准小说站模板 - 包含完整信息",
    "bookSourceGroup": "小说",
    "bookSourceName": "标准小说站",
    "bookSourceType": 0,
    "bookSourceUrl": "https://example.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".author@text",
      "coverUrl": ".cover@src",
      "init": "",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": "h1@text",
      "tocUrl": ".toc-link@href"
    },
    "ruleContent": {
      "content": "#content@html##<div id=\"ad\">[\\s\\S]*?</div>|请收藏本站|本章完##"
    },
    "ruleExplore": {
      "author": ".author@text",
      "bookList": ".book-item",
      "bookUrl": "a@href",
      "coverUrl": "img@src",
      "intro": ".intro@text",
      "kind": ".category@text",
      "name": ".title@text",
      "wordCount": ".word-count@text"
    },
    "ruleSearch": {
      "author": ".author@text",
      "bookList": ".book-list .item",
      "bookUrl": "a@href",
      "checkKeyWord": "",
      "coverUrl": "img@src",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": ".title@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#chapter-list a",
      "chapterName": "text",
      "chapterUrl": "href",
      "nextTocUrl": ""
    },
    "searchUrl": "/search?q={{key}}&page={{page}}",
    "weight": 0
  }
]
```

## Template 2: 笔趣阁类（无封面，信息合并）

适用于搜索页无封面、信息合并在一起的网站。

```json
[
  {
    "bookSourceComment": "笔趣阁类模板 - 无封面，信息合并",
    "bookSourceGroup": "笔趣阁",
    "bookSourceName": "笔趣阁",
    "bookSourceType": 0,
    "bookSourceUrl": "https://www.biquge.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".author@text##^作者：##",
      "coverUrl": "",
      "init": "",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": "h1@text",
      "tocUrl": ".toc-link@href"
    },
    "ruleContent": {
      "content": "#content@text##免费小说就上.*|本章完|请记住本书首发域名##"
    },
    "ruleExplore": {
      "bookList": "",
      "name": "",
      "bookUrl": ""
    },
    "ruleSearch": {
      "author": ".author.0@text##.*\\| |作者：##",
      "bookList": ".result-list .result-item",
      "bookUrl": "h3 a@href",
      "checkKeyWord": "",
      "coverUrl": "",
      "intro": "",
      "kind": ".author.0@text##\\|.*##",
      "lastChapter": ".author.1@text##.*更新：##",
      "name": "h3 a@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#list dd a",
      "chapterName": "text",
      "chapterUrl": "href",
      "nextTocUrl": ""
    },
    "searchUrl": "/search.php?q={{key}}",
    "weight": 0
  }
]
```

**关键特点：**
- `coverUrl: ""` - 搜索页无封面
- 使用数字索引 `.0`, `.1` 区分同名标签
- 正则表达式拆分合并信息

## Template 3: POST请求网站（GBK编码）

适用于需要POST请求且使用GBK编码的中文网站。

```json
[
  {
    "bookSourceComment": "POST请求模板 - GBK编码",
    "bookSourceGroup": "中文小说",
    "bookSourceName": "69书吧",
    "bookSourceType": 0,
    "bookSourceUrl": "https://www.69shuba.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".booknav2 a.0@text",
      "coverUrl": ".bookimg2 img@src",
      "init": "",
      "intro": ".navtxt p.-1@text",
      "kind": ".booknav2 a.1@text",
      "lastChapter": ".qustime a@text",
      "name": ".booknav2 h1@text",
      "tocUrl": ""
    },
    "ruleContent": {
      "content": ".txtnav@html##<p>.*?</p>|<script[\\s\\S]*?</script>|广告##"
    },
    "ruleExplore": {},
    "ruleSearch": {
      "author": "span.-1@text##.*：##",
      "bookList": ".newbox li",
      "bookUrl": "a.0@href",
      "checkKeyWord": "",
      "coverUrl": "img@src",
      "intro": "",
      "kind": "",
      "lastChapter": "",
      "name": "a.0@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#catalog li",
      "chapterName": "a@text",
      "chapterUrl": "a@href",
      "nextTocUrl": ""
    },
    "searchUrl": "/modules/article/search.php,{\"method\":\"POST\",\"body\":\"searchkey={{key}}&searchtype=all\",\"charset\":\"gbk\"}",
    "weight": 0
  }
]
```

**关键特点：**
- POST请求配置：`{"method":"POST","body":"...","charset":"gbk"}`
- GBK编码声明：`"charset":"gbk"`
- body使用String()类型

## Template 4: 懒加载图片网站

适用于使用data-original属性懒加载图片的网站。

```json
[
  {
    "bookSourceComment": "懒加载图片模板",
    "bookSourceGroup": "图片网站",
    "bookSourceName": "懒加载示例",
    "bookSourceType": 0,
    "bookSourceUrl": "https://example.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0\",\"Referer\":\"https://example.com\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".author@text",
      "coverUrl": "img.lazy@data-original||img@src",
      "init": "",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": "h1@text",
      "tocUrl": ""
    },
    "ruleContent": {
      "content": "#content@html##<div class=\"ad\">[\\s\\S]*?</div>##"
    },
    "ruleExplore": {},
    "ruleSearch": {
      "author": ".author@text",
      "bookList": ".book-list .item",
      "bookUrl": "a@href",
      "checkKeyWord": "",
      "coverUrl": "img.lazy@data-original||img@src",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": "",
      "name": ".title@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#chapter-list a",
      "chapterName": "text",
      "chapterUrl": "href",
      "nextTocUrl": ""
    },
    "searchUrl": "/search?q={{key}}",
    "weight": 0
  }
]
```

**关键特点：**
- `img.lazy@data-original||img@src` - 优先使用data-original，备选src
- 添加Referer请求头防止防盗链

## Template 5: 有分页的目录

适用于目录有多页，需要分页获取的网站。

```json
[
  {
    "bookSourceComment": "分页目录模板",
    "bookSourceGroup": "分页网站",
    "bookSourceName": "分页示例",
    "bookSourceType": 0,
    "bookSourceUrl": "https://example.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".author@text",
      "coverUrl": ".cover@src",
      "init": "",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": "h1@text",
      "tocUrl": ""
    },
    "ruleContent": {
      "content": "#content@html##广告[\\s\\S]*?##",
      "nextContentUrl": "text.下一章@href"
    },
    "ruleExplore": {},
    "ruleSearch": {
      "author": ".author@text",
      "bookList": ".book-list .item",
      "bookUrl": "a@href",
      "checkKeyWord": "",
      "coverUrl": "img@src",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": ".title@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#chapter-list a",
      "chapterName": "text",
      "chapterUrl": "href",
      "nextTocUrl": "option@value"
    },
    "searchUrl": "/search?q={{key}}",
    "weight": 0
  }
]
```

**关键特点：**
- `nextTocUrl: "option@value"` - 分页选择器
- `nextContentUrl: "text.下一章@href"` - 下一章按钮
- 使用 `text.文本@href` 格式而非 `:contains()`

## Template 6: 聚合源（API型）

适用于返回JSON数据的聚合源。

```json
[
  {
    "bookSourceComment": "聚合源模板 - JSON API",
    "bookSourceGroup": "聚合",
    "bookSourceName": "聚合源示例",
    "bookSourceType": 0,
    "bookSourceUrl": "https://api.example.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": "$.data.author",
      "coverUrl": "$.data.coverUrl",
      "init": "",
      "intro": "$.data.description",
      "kind": "$.data.category",
      "lastChapter": "$.data.lastChapter",
      "name": "$.data.title",
      "tocUrl": "$.data.tocUrl"
    },
    "ruleContent": {
      "content": "$.data.content"
    },
    "ruleExplore": {},
    "ruleSearch": {
      "author": "$.data[*].author",
      "bookList": "$.data[*]",
      "bookUrl": "$.data[*].bookUrl",
      "checkKeyWord": "",
      "coverUrl": "$.data[*].coverUrl",
      "intro": "$.data[*].description",
      "kind": "$.data[*].category",
      "lastChapter": "$.data[*].lastChapter",
      "name": "$.data[*].title",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "$.data.chapters[*]",
      "chapterName": "title",
      "chapterUrl": "url",
      "nextTocUrl": ""
    },
    "searchUrl": "/api/search?keyword={{key}}&page={{page}}",
    "weight": 0
  }
]
```

**关键特点：**
- 使用JSONPath提取数据：`$.字段名`
- 数组索引：`$.data[*]`
- 直接提取字段：`"author": "$.data.author"`

## Template 7: 动态加载（webView）

适用于需要JavaScript渲染的动态网站。

```json
[
  {
    "bookSourceComment": "动态加载模板 - webView",
    "bookSourceGroup": "动态网站",
    "bookSourceName": "动态加载示例",
    "bookSourceType": 0,
    "bookSourceUrl": "https://example.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".author@text",
      "coverUrl": ".cover@src",
      "init": "",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": "h1@text",
      "tocUrl": ""
    },
    "ruleContent": {
      "content": "#content@html",
      "webJs": "window.scrollTo(0,document.body.scrollHeight);"
    },
    "ruleExplore": {},
    "ruleSearch": {
      "author": ".author@text",
      "bookList": ".book-list .item",
      "bookUrl": "a@href##$##,{\"webView\":true}",
      "checkKeyWord": "",
      "coverUrl": "img@src",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": "",
      "name": ".title@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#chapter-list a",
      "chapterName": "text",
      "chapterUrl": "href##$##,{\"webView\":true}",
      "nextTocUrl": ""
    },
    "searchUrl": "/search?q={{key}},{\"webView\":true}",
    "weight": 0
  }
]
```

**关键特点：**
- 在URL后添加 `,{"webView":true}` 参数
- `webJs` 字段注入JavaScript
- 适用于内容动态加载的网站

## Template 8: 漫画站

适用于漫画网站，包含图片章节。

```json
[
  {
    "bookSourceComment": "漫画站模板",
    "bookSourceGroup": "漫画",
    "bookSourceName": "漫画示例",
    "bookSourceType": 2,
    "bookSourceUrl": "https://example.com",
    "enabled": true,
    "enabledCookieJar": true,
    "header": "{\"User-Agent\":\"Mozilla/5.0\",\"Referer\":\"https://example.com\"}",
    "lastUpdateTime": 1709833881234,
    "respondTime": 180000,
    "ruleBookInfo": {
      "author": ".author@text",
      "coverUrl": ".cover@src",
      "init": "",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": "h1@text",
      "tocUrl": ""
    },
    "ruleContent": {
      "content": "#images img@src##\\?.*##"
    },
    "ruleExplore": {},
    "ruleSearch": {
      "author": ".author@text",
      "bookList": ".comic-list .item",
      "bookUrl": "a@href",
      "checkKeyWord": "",
      "coverUrl": "img@src",
      "intro": ".intro@text",
      "kind": ".category@text",
      "lastChapter": ".last-chapter@text",
      "name": ".title@text",
      "wordCount": ""
    },
    "ruleToc": {
      "chapterList": "#chapter-list a",
      "chapterName": "text",
      "chapterUrl": "href",
      "nextTocUrl": ""
    },
    "searchUrl": "/search?q={{key}}",
    "weight": 0
  }
]
```

**关键特点：**
- `bookSourceType: 2` - 图片类型
- `content: "#images img@src"` - 提取所有图片URL
- 正则清理URL参数：`\\?.*##`

## 使用指南

### 1. 选择合适的模板

根据网站特征选择模板：
- 有封面完整信息 → Template 1
- 无封面信息合并 → Template 2
- POST请求GBK编码 → Template 3
- 懒加载图片 → Template 4
- 目录分页 → Template 5
- JSON API → Template 6
- 动态加载 → Template 7
- 漫画网站 → Template 8

### 2. 修改必需字段

**bookSource级别：**
```json
{
  "bookSourceUrl": "https://your-site.com",
  "bookSourceName": "你的书源名称",
  "searchUrl": "/search?q={{key}}"  // 根据实际修改
}
```

**ruleSearch级别：**
```json
{
  "ruleSearch": {
    "bookList": ".your-book-list-class",
    "name": ".your-title-class@text",
    "bookUrl": ".your-link-class@href"
  }
}
```

### 3. 根据HTML结构调整

使用浏览器开发者工具（F12）检查：
- 书籍列表容器选择器
- 书名、作者、封面等元素选择器
- 是否有特殊属性（lazy loading）
- 信息是否合并需要正则拆分

### 4. 测试和调试

1. 导入Legado APP
2. 搜索测试
3. 查看调试日志
4. 逐项验证规则

### 5. 常见修改

**修改列表选择器：**
```json
"bookList": ".book-list .item"  // 改为你的选择器
```

**添加封面：**
```json
"coverUrl": "img@src"  // 改为 img@src 或 img@data-original
```

**处理合并信息：**
```json
"author": ".author.0@text##.*\\| |作者：##",
"kind": ".author.0@text##\\|.*##"
```

**添加下一章：**
```json
"nextContentUrl": "text.下一章@href"
```

## 注意事项

1. **必须验证选择器**：在真实HTML上测试
2. **处理特殊编码**：GBK网站需添加 `charset:"gbk"`
3. **避免错误字段**：不要使用 `prevContentUrl`、`:contains()`
4. **清理广告内容**：使用正则表达式清理
5. **检查懒加载**：优先使用 `data-original`
6. **正确配置POST**：严格按照格式配置

## 模板对比

| 模板 | 封面 | 编码 | 请求方式 | 适用场景 |
|------|------|------|----------|----------|
| Template 1 | 有 | UTF-8 | GET | 标准小说站 |
| Template 2 | 无 | UTF-8 | GET | 笔趣阁类 |
| Template 3 | 有 | GBK | POST | 中文老站 |
| Template 4 | 懒加载 | UTF-8 | GET | 图片懒加载 |
| Template 5 | 有 | UTF-8 | GET | 分页目录 |
| Template 6 | 有 | UTF-8 | GET | API聚合 |
| Template 7 | 有 | UTF-8 | GET + webView | 动态加载 |
| Template 8 | 有 | UTF-8 | GET | 漫画网站 |
