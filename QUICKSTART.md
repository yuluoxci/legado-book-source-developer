# Legado 书源开发 - 快速开始指南

## 5 分钟上手

如果你已经熟悉 HTML 和 CSS，可以快速开始创建书源。

### 场景 1：标准小说站（最简单）

```json
[
  {
    "bookSourceName": "示例小说站",
    "bookSourceUrl": "https://example.com",
    "searchUrl": "/search?q={{key}}",
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
      "intro": ".intro@text",
      "coverUrl": ".cover img@src"
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

### 场景 2：笔趣阁类（无封面）

```json
[
  {
    "bookSourceName": "示例笔趣阁",
    "bookSourceUrl": "https://bqg.example.com",
    "searchUrl": "/search.php?searchkey={{key}}",
    "ruleSearch": {
      "bookList": ".result-list tr",
      "name": "td.0@text",
      "author": "td.2@text##作者：##",
      "bookUrl": "a.0@href",
      "coverUrl": ""
    },
    "ruleBookInfo": {
      "name": "h1@text",
      "author": "#info p.1@text##作者：##",
      "intro": "#intro@text"
    },
    "ruleToc": {
      "chapterList": "#list dd a",
      "chapterName": "@text",
      "chapterUrl": "@href"
    },
    "ruleContent": {
      "content": "#content@html",
      "nextContentUrl": "text.下一章@href"
    }
  }
]
```

### 场景 3：POST 请求 + GBK 编码

```json
[
  {
    "bookSourceName": "示例 GBK 站",
    "bookSourceUrl": "https://gbk.example.com",
    "searchUrl": "/search,{\"method\":\"POST\",\"body\":\"key={{key}}\",\"charset\":\"gbk\"}",
    "ruleSearch": {
      "bookList": ".book-item",
      "name": ".title@text",
      "bookUrl": "a@href"
    },
    "ruleToc": {
      "chapterList": ".chapter-list a",
      "chapterName": "@text",
      "chapterUrl": "@href"
    },
    "ruleContent": {
      "content": ".content@text"
    }
  }
]
```

## 常用选择器速查表

| 选择器 | 说明 | 示例 |
|--------|------|------|
| `.class` | 类选择器 | `.title@text` |
| `#id` | ID 选择器 | `#content@html` |
| `element` | 元素选择器 | `img@src` |
| `.parent .child` | 后代选择器 | `.book .title@text` |
| `.class.0` | 第一个元素 | `.item.0@text` |
| `.class.-1` | 最后一个元素 | `.item.-1@text` |
| `text.文本` | 文本选择器 | `text.下一章@href` |
| `[@attr]` | 属性选择器 | `[data-src]@data-src` |

## 常用提取类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| `@text` | 完整文本 | 书名、作者、章节名 |
| `@html` | HTML 结构 | 正文内容（保留格式） |
| `@ownText` | 仅元素文本 | 去除广告 |
| `@href` | 链接地址 | 书籍链接、章节链接 |
| `@src` | 图片地址 | 封面图片 |

## 常用正则表达式

```
删除前缀：
  ##^作者：           # 删除开头的"作者："
  ##^《               # 删除开头的"《"

删除后缀：
  ##（.*）$           # 删除括号及内容
  ##》$               # 删除结尾的"》"

提取内容：
  ##作者：(.*)##$1    # 提取"作者："后的内容
  ##第(\d+)章##$1     # 提取章节号

清理广告：
  ##请收藏本站        # 删除提示文本
  ##本章完|继续阅读    # 删除多个提示
```

## 快速调试技巧

### 1. 使用浏览器开发者工具

1. 按 F12 打开开发者工具
2. 使用 Ctrl+Shift+C 选择元素
3. 右键 → Copy → Copy selector

### 2. 验证选择器

在控制台输入：
```javascript
document.querySelectorAll('.book-list .item')
```

### 3. 测试提取结果

```javascript
document.querySelector('.title').textContent
document.querySelector('.title').href
document.querySelector('img').src
```

## 常见问题快速解决

### 搜索无结果

- 检查 CSS 选择器是否正确
- 确认网站结构没有变化
- 添加必要的 headers

### 内容缺失

- 检查是否动态加载
- 设置正确的 cookies
- 可能需要 webView

### 编码乱码

- 添加 charset="gbk" 到 searchUrl
- UTF-8 不需要指定（默认）

### 目录顺序错误

- 在列表选择器前加 `-` 符号：`-ul.chapter-list li`

### 图片不显示

- 检查是否懒加载：`img@data-original||img@src`
- 添加 Referer 请求头

## 下一步

- 阅读 [WORKFLOW.md](WORKFLOW.md) 了解完整工作流程
- 查看 [references/book_source_templates.md](references/book_source_templates.md) 获取更多模板
- 参考 [references/real_book_source_examples.md](references/real_book_source_examples.md) 学习真实案例
- 使用 [tools/analyze_fhysc.py](tools/analyze_fhysc.py) 分析网站
