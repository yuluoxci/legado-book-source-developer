# Legado Knowledge Base - CSS Selector Rules

## CSS选择器语法格式

### 基本格式
```
CSS选择器@提取类型##正则表达式##替换内容
```

### 提取类型详解

#### @text - 提取所有文本
- 提取元素及其所有子元素的文本内容
- 包含子元素的文本
- 示例：`.title@text` 提取标题及其子元素的所有文本

#### @ownText - 只提取当前元素的文本
- 只提取当前元素的文本
- 不包含子元素
- 适用于需要排除子元素文本的场景
- 示例：`.content@ownText` 只提取当前div的文本

#### @html - 提取完整HTML结构
- 提取元素及其子元素的完整HTML
- 保留所有标签和属性
- 适用于需要保留格式和图片的场景
- 示例：`.content@html` 提取包括p、span等标签的完整HTML

#### @textNode - 提取文本节点
- 提取所有文本节点
- 分段返回多个结果
- 适用于需要逐个处理文本节点的场景
- 示例：`.content@textNode` 返回多个文本节点数组

#### @属性名 - 提取属性值
- 提取指定属性的值
- 常用属性：href、src、class、id、value、data-* 等
- 示例：`a@href` 提取链接地址，`img@src` 提取图片地址

## CSS选择器类型

### 元素选择器
```css
div@text
p@text
h1@text
a@href
img@src
```

### 类选择器
```css
.book-name@text
.author@text
.intro@text
```

### ID选择器
```css
#content@text
#main@html
```

### 属性选择器
```css
[href]@href
[class*=book]@text
[data-id="123"]@text
[href^="https://"]@href
[href$=".html"]@href
```

### 组合选择器

#### 后代选择器
```css
.container .item@text
.book-list .book-name@text
#main .content p@text
```

#### 子元素选择器
```css
ul > li@text
.book-info > h1@text
.content > p@text
```

#### 相邻兄弟选择器
```css
h1 + p@text
.title + .author@text
```

#### 通用兄弟选择器
```css
.chapter ~ .notes@text
.name ~ .author@text
```

### 伪类选择器（Legado不支持的）

**⚠️ 重要：Legado不支持以下伪类选择器**
- ❌ `:first-child` - 应使用 `.0`
- ❌ `:last-child` - 应使用 `.-1`
- ❌ `:nth-child(n)` - 应使用 `.n`
- ❌ `:contains(text)` - 应使用 `text.文本`

### 数字索引选择器（推荐）

#### 正数索引
```css
class.item.0@text    # 第一个
class.item.1@text    # 第二个
class.item.2@text    # 第三个
```

#### 负数索引
```css
class.item.-1@text   # 倒数第一个
class.item.-2@text   # 倒数第二个
class.item.-3@text   # 倒数第三个
```

#### 排除索引
```css
class.item.0!1@text   # 排除第1个
class.item.0!1!2@text # 排除第1和第2个
```

#### 区间索引
```css
class.item.[0:5]@text     # 第0到第5个
class.item.[1:3]@text     # 第1到第3个
class.item.[0:-1]@text    # 第0到倒数第1个
```

#### 步长索引
```css
class.item.[0:10:2]@text  # 第0到第10个，每2个取一个
class.item.[0:10:3]@text  # 第0到第10个，每3个取一个
```

## 文本选择器（text.文本）

### 基本用法
```css
text.下一章@href      # 提取包含"下一章"文本的元素的href属性
text.作者@text        # 提取包含"作者"文本的元素的文本
text.下一页@href      # 提取包含"下一页"文本的元素的href属性
```

### 应用场景
- 替代 `:contains()` 伪类选择器
- 用于 nextContentUrl 的选择
- 用于包含特定文本的元素定位

### 示例
```json
{
  "ruleContent": {
    "nextContentUrl": "text.下一章@href"
  }
}
```

## 正则表达式

### 基本格式

#### 格式1：删除匹配的内容
```
选择器@提取类型##正则表达式
```
示例：`.author@text##^作者：` 删除"作者："前缀

#### 格式2：替换匹配的内容
```
选择器@提取类型##正则表达式##替换内容
```
示例：`.price@text##\\$(\\d+)##￥$1` 将$替换为￥

#### 格式3：使用捕获组提取
```
选择器@提取类型##正则表达式(捕获组)##$1
```
示例：`.author@text##.*作者：(.*)##$1` 提取"作者："后面的内容

### 正则表达式元字符

#### 字符类
```
[abc]       匹配a、b、c中的任意一个
[^abc]      匹配除a、b、c之外的字符
[a-z]       匹配小写字母
[0-9]       匹配数字
\\d         匹配数字（等同于[0-9]）
\\w         匹配字母、数字、下划线
\\s         匹配空白字符
```

#### 量词
```
*           匹配0次或多次
+           匹配1次或多次
?           匹配0次或1次
{n}         匹配n次
{n,}        匹配n次或更多
{n,m}       匹配n到m次
```

#### 特殊字符
```
.           匹配任意字符（除换行）
^           匹配行首
$           匹配行尾
|           或运算符
```

### 常用正则表达式

#### 清理前缀
```
##^作者：       # 删除开头的"作者："
##^《           # 删除开头的"《"
##^[^|]*\\|     # 删除第一个"|"及其前面的内容
```

#### 清理后缀
```
##（.*）$       # 删除括号及其内容
##》$          # 删除结尾的"》"
##\\s+$         # 删除结尾的空白
```

#### 提取特定内容
```
##.*作者：(.*)##$1      # 提取"作者："后面的内容
##第(\\d+)章##$1         # 提取章节号
##(\\d{4})-(\\d{2})-(\\d{2})##$1年$2月$3日  # 格式化日期
```

#### 清理广告和提示
```
##<div id="ad">[\\s\\S]*?</div>         # 删除广告div
##请收藏本站|本章完|继续阅读##         # 删除常见提示文本
##免费小说就上.*##                    # 删除网站推广文本
```

### 多个清理规则
使用 `|` 分隔多个规则：
```
选择器@提取类型##规则1|规则2|规则3##
```

示例：
```json
{
  "content": "#chaptercontent@html##<div id=\"ad\">[\\s\\S]*?</div>|请收藏本站|本章完##"
}
```

## 实战案例

### 案例1：提取书名和作者
```html
<div class="book-info">
  <h1 class="title">斗破苍穹</h1>
  <p class="author">作者：天蚕土豆</p>
</div>
```

规则：
```json
{
  "ruleSearch": {
    "bookList": ".book-info",
    "name": ".title@text",
    "author": ".author@text##^作者："
  }
}
```

### 案例2：处理合并信息
```html
<div class="item">
  <a href="/book/123">
    <p class="title">斗破苍穹</p>
    <p class="author">科幻灵异 | 作者：天蚕土豆</p>
    <p class="author">连载 | 更新：第100章</p>
  </a>
</div>
```

规则：
```json
{
  "ruleSearch": {
    "bookList": ".item",
    "name": ".title@text",
    "author": ".author.0@text##.*\\| |作者：##",
    "kind": ".author.0@text##\\|.*##",
    "lastChapter": ".author.1@text##.*更新：##",
    "bookUrl": "a@href"
  }
}
```

### 案例3：懒加载图片
```html
<img class="lazy" data-original="http://example.com/cover.jpg" src="placeholder.jpg"/>
```

规则：
```json
{
  "coverUrl": "img.lazy@data-original||img@src"
}
```

### 案例4：清理正文广告
```html
<div id="chaptercontent">
  <p>正文内容...</p>
  <div id="ad">广告内容</div>
  <p>更多内容...</p>
  <p>请收藏本站</p>
</div>
```

规则：
```json
{
  "ruleContent": {
    "content": "#chaptercontent@html##<div id=\"ad\">[\\s\\S]*?</div>|请收藏本站##"
  }
}
```

### 案例5：选择特定元素
```html
<div class="chapter-list">
  <p><a href="/chapter/1">第1章</a></p>
  <p><a href="/chapter/2">第2章</a></p>
  <p><a href="/chapter/3">第3章</a></p>
</div>
```

规则：
```json
{
  "ruleToc": {
    "chapterList": ".chapter-list p",
    "chapterName": "a@text",
    "chapterUrl": "a@href"
  }
}
```

提取特定章节：
```json
{
  "ruleToc": {
    "chapterList": ".chapter-list p.[0:5]",  # 只提取前5章
    "chapterName": "a@text",
    "chapterUrl": "a@href"
  }
}
```

### 案例6：处理分页
```html
<select onchange="location.href=this.value">
  <option value="/book/123/toc.html">第1页</option>
  <option value="/book/123/toc_2.html">第2页</option>
  <option value="/book/123/toc_3.html">第3页</option>
</select>
```

规则：
```json
{
  "ruleToc": {
    "chapterList": "#chapter-list a",
    "chapterName": "text",
    "chapterUrl": "href",
    "nextTocUrl": "option@value"
  }
}
```

## 常见问题

### Q1: 如何区分 @text 和 @ownText？
- @text: 提取元素及其所有子元素的文本
- @ownText: 只提取当前元素的文本，不包含子元素
- 需要去广告时使用 @ownText

### Q2: 如何处理多个同名标签？
- 使用数字索引：`.0` 第一个、`.1` 第二个、`.-1` 倒数第一个
- 示例：`.author.0@text` 提取第一个author标签

### Q3: 如何判断是否设置 nextContentUrl？
- 查看按钮链接是否到真正的下一章节
- URL中章节号变化 → 设置 nextContentUrl
- URL中只是页码变化 → 留空

### Q4: 正则表达式如何编写？
- 使用 ## 作为分隔符
- 多个规则用 | 分隔
- 捕获组用 ()，引用用 $1, $2

### Q5: 为什么不能用 :contains()？
- Legado不支持 :contains() 伪类选择器
- 应使用 text.文本 格式
- 示例：`text.下一章@href` 替代 `a:contains(下一章)@href`

## 最佳实践

1. **优先使用类选择器**：`.class-name` 简单可靠
2. **使用ID选择器**：`#id-name` 更精准
3. **避免过深嵌套**：最多3-4层
4. **使用数字索引**：`.0`, `.-1` 替代伪类
5. **合理使用正则**：清理广告和提示
6. **提取类型要准确**：@text, @html, @ownText
7. **检查特殊属性**：data-original for lazy loading
8. **验证选择器**：在开发者工具中测试

## 调试技巧

1. **使用浏览器开发者工具**
   - F12 打开开发者工具
   - Elements 面板查看HTML结构
   - Console 面板测试选择器

2. **逐步验证**
   - 先测试 bookList 是否正确
   - 再测试各个字段提取
   - 最后验证正则表达式

3. **查看网页源代码**
   - 右键 → 查看网页源代码
   - Ctrl+F 搜索关键文本
   - 确认元素位置

4. **使用 Legado 调试功能**
   - 导入书源
   - 使用调试功能测试
   - 查看详细日志
