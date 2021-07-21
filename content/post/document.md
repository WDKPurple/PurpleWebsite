---
title: "文档"
date: 2021-07-12
draft: true
tags: ["文档"]
ShowToc: true
---

# 图床使用指南

当你需要在文章中插入静态资源 *（包括但不限于图像、css等）* 时，你就需要使用图床。

目前，我们的图床托管在GitHub，并使用著名的jsDelivr项目进行分发。速度与稳定性有保障。

## 网页直接上传

以下是使用网页直接上传方式的流程指引：

1. 请确保你拥有一个GitHub账户 *（没有请注册）* ，并已告诉了时远你的用户名，以此获得图床的编辑权限。然后，让我们访问[WDKPurple/StaticResources](https://github.com/WDKPurple/StaticResources)，我们可以看到一个这样的界面：<br>![image-20210708103137821](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/userguide/image-20210708103137821.png)
2. 点击进入你需要上传的静态资源的对应目录，如图像的对应目录[images](https://github.com/WDKPurple/StaticResources/tree/main/images)，并点击Add file、Upload files，如图所示：<br>![image-20210708103624567](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/userguide/image-20210708103624567.png)
3. 进入上传界面后，选择你需要上传的文件，并在下方的 *Commit changes* 中简要描述本次上传的文件内容，如简要描述这些图片与哪些文章相关联，建议在描述中使用英文，如图所示：<br>![image-20210708104139904](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/userguide/image-20210708104139904.png)
4. 点击Commit changes以完成上传，而后你可以就可以通过jsDelivr访问你上传的静态资源，其地址格式为：`https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/目录名/文件名`

## 使用Typora配合PicGo使用

*本方式需要一些基础的计算机知识。*

本方式对于使用Typora进行编辑的同学比在网页上手动上传更加方便。

本方式建议直接参考知乎专栏文章[Typora+PicGo+Github+Jsdelivr实现高效图文写作](https://zhuanlan.zhihu.com/p/144053393)。但请注意：

1. 图床设置 > GitHub图床中，仓库名为 `WDKPurple/StaticResources` ，分支名为 `main` ，指定存储路径为 `images/` ，设定自定义域名为 `https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/` 。
2. Typora设置中请勾选“对本地位置的图片应用上述规则“，而不是如上文所描述取消勾选。
3. **注意！请勿使用任何其他图床！**

**如有任何问题，请直接联系时远！**

# Hugo 本地预览页面方法

## 下载 Hugo 二进制包 (以 Windows 为例)

下载地址为 <https://github.com/gohugoio/hugo/releases/latest>，打开页面后往下翻，找到 `hugo_extended_0.85.0_Windows-64bit.zip` (举例)，下载并解压，你将会看到 `hugo.exe` 文件。

## 本地预览页面 (以 Windows 为例)

1. clone repository <https://github.com/WDKPurple/PurpleWebsite>，或者点击页面右上角绿色 Code 按钮，选择 Download ZIP 并解压缩。
2. 打开命令提示符，cd 到页面文件根目录，或者在资源管理器里定位到页面文件根目录，并在地址栏里输入 `cmd` 并回车，如图所示：<br>![image](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/userguide/image-20210713052247.png)
3. 输入`<hugo.exe所在路径>\huge.exe server -D`并回车 (简单起见，可以将 `hugo.exe` 解压缩在页面文件根目录，这样在命令提示符里直接输入 `hugo.exe server -D` 并回车即可)，这时应该显示如下图类似界面：<br>![image](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/userguide/image-20210713053647.png)
4. 在浏览器中打开网址 `http://127.0.0.1:1313/` 即可本地预览页面。
5. 这时可以实时修改本地页面代码，浏览器中显示内容会自动更新。
6. 在命令提示符中按下 `Ctrl+C` 退出 Hugo。有时候页面自动更新会失效，可能需要重新启动 Hugo 或者重新打开浏览器才能查看更新的页面。

# Markdown 基本语法 (删减了表格和代码的部分) 及部分模板介绍

## 文本

```
Text can be **bold**, _italic_, ***bold and italic*** or ~~strikethrough~~.
[Links](https://github.com) should be blue with no underlines (unless hovered over).
```

Text can be **bold**, _italic_, ***bold and italic*** or ~~strikethrough~~.
[Links](https://github.com) should be blue with no underlines (unless hovered over).

```
<small>small</small> text
```

<small>small</small> text

### 插入到网站内部页面的超链接

语法：

```
[链接文本]({{</* ref "md源文件地址(例如post/xxx.md)" */>}})
```

例子：

```
[第一讲 · 社会性别与性别的描述学]({{</* ref "post/2019-06-17-six-lectures-1.md" */>}})
```

[第一讲 · 社会性别与性别的描述学]({{< ref "post/2019-06-17-six-lectures-1.md" >}})

## 段落

```
There should be whitespace between paragraphs.
There should be whitespace between paragraphs.
There should be whitespace between paragraphs.
There should be whitespace between paragraphs.

There should be whitespace between paragraphs. There should be whitespace between paragraphs. There should be whitespace between paragraphs. There should be whitespace between paragraphs.
```

There should be whitespace between paragraphs.
There should be whitespace between paragraphs.
There should be whitespace between paragraphs.
There should be whitespace between paragraphs.

There should be whitespace between paragraphs. There should be whitespace between paragraphs. There should be whitespace between paragraphs. There should be whitespace between paragraphs.

### 强制换行

```
There should be whitespace<br>
between paragraphs.
```

There should be whitespace<br>
between paragraphs.

### 居中

```
{{%/* center */%}}
Center
{{%/* /center */%}}
```

{{% center %}}
Center
{{% /center %}}

## 引用

```
> There should be no margin above this first sentence.
>
> Blockquotes should be a lighter gray with a gray border along the left side.
>
> > Nested blockquote
> >
> > Nested blockquote
> 
> There should be no margin below this final sentence.
```

> There should be no margin above this first sentence.
>
> Blockquotes should be a lighter gray with a gray border along the left side.
>
> > Nested blockquote
> >
> > Nested blockquote
> 
> There should be no margin below this final sentence.

### Purple 型自定义引用模板

#### 语法

```
{{%/* quote_purple
center="是否居中(默认为否)"
align="文字对齐方式(默认左对齐)"
minwidth="最小宽度(默认10%)"
maxwidth="最大宽度(默认100%)"
*/%}}
引用内容
{{%/* /quote_purple */%}}
```

#### 例子

```
{{%/* quote_purple */%}}
引用内容
{{%/* /quote_purple */%}}

{{%/* quote_purple */%}}
引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容
{{%/* /quote_purple */%}}

{{%/* quote_purple minwidth="50%"*/%}}
引用内容
{{%/* /quote_purple */%}}

{{%/* quote_purple minwidth="100%"*/%}}
引用内容
{{%/* /quote_purple */%}}

{{%/* quote_purple center="true" minwidth="50%"*/%}}
居中，文字左对齐
{{%/* /quote_purple */%}}

{{%/* quote_purple align="center" minwidth="50%"*/%}}
左对齐，文字居中
{{%/* /quote_purple */%}}

{{%/* quote_purple center="true" align="center" */%}}
***第一讲***<br>
*<small>社会性别与性别的描述学</small>*
{{%/* /quote_purple */%}}
```

{{% quote_purple %}}
引用内容
{{% /quote_purple %}}

{{% quote_purple %}}
引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容引用内容
{{% /quote_purple %}}

{{% quote_purple minwidth="50%" %}}
引用内容
{{% /quote_purple %}}

{{% quote_purple minwidth="100%"%}}
引用内容
{{% /quote_purple %}}

{{% quote_purple center="true" minwidth="50%"%}}
居中，文字左对齐
{{% /quote_purple %}}

{{% quote_purple align="center" minwidth="50%"%}}
左对齐，文字居中
{{% /quote_purple %}}

{{% quote_purple center="true" align="center" %}}
***第一讲***<br>
*<small>社会性别与性别的描述学</small>*
{{% /quote_purple %}}

## 标题

```
# Header 1

This is a normal paragraph following a header. Bacon ipsum dolor sit amet t-bone doner shank drumstick, pork belly porchetta chuck sausage brisket ham hock rump pig. Chuck kielbasa leberkas, pork bresaola ham hock filet mignon cow shoulder short ribs biltong.

## Header 2

> This is a blockquote following a header. Bacon ipsum dolor sit amet t-bone doner shank drumstick, pork belly porchetta chuck sausage brisket ham hock rump pig. Chuck kielbasa leberkas, pork bresaola ham hock filet mignon cow shoulder short ribs biltong.

### Header 3

#### Header 4

- This is an unordered list following a header.
- This is an unordered list following a header.
- This is an unordered list following a header.

##### Header 5

1. This is an ordered list following a header.
1. This is an ordered list following a header.
1. This is an ordered list following a header.

###### Header 6

```

# Header 1

This is a normal paragraph following a header. Bacon ipsum dolor sit amet t-bone doner shank drumstick, pork belly porchetta chuck sausage brisket ham hock rump pig. Chuck kielbasa leberkas, pork bresaola ham hock filet mignon cow shoulder short ribs biltong.

## Header 2

> This is a blockquote following a header. Bacon ipsum dolor sit amet t-bone doner shank drumstick, pork belly porchetta chuck sausage brisket ham hock rump pig. Chuck kielbasa leberkas, pork bresaola ham hock filet mignon cow shoulder short ribs biltong.

### Header 3

#### Header 4

- This is an unordered list following a header.
- This is an unordered list following a header.
- This is an unordered list following a header.

##### Header 5

1. This is an ordered list following a header.
1. This is an ordered list following a header.
1. This is an ordered list following a header.

###### Header 6

## 水平线

```
---

There's a horizontal rule above and below this.

---
```

---

There's a horizontal rule above and below this.

---

## 列表

```
Here is an unordered list:

- Salt-n-Pepa
- Bel Biv DeVoe
- Kid 'N Play

And an ordered list:

1. Michael Jackson
1. Michael Bolton
1. Michael Bublé

And an unordered task list:

- [x] Create a sample markdown document
- [x] Add task lists to it
- [ ] Take a vacation

And a "mixed" task list:

- [ ] Steal underpants
- ?
- [ ] Profit!

And a nested list:

- Jackson 5
    - Michael
    - Tito
    - Jackie
    - Marlon
    - Jermaine
- TMNT
    - Leonardo
    - Michelangelo
    - Donatello
    - Raphael

Definition lists can be used with HTML syntax. Definition terms are bold and italic.

<dl>
  <dt>Name</dt>
  <dd>Godzilla</dd>
  <dt>Born</dt>
  <dd>1952</dd>
  <dt>Birthplace</dt>
  <dd>Japan</dd>
  <dt>Color</dt>
  <dd>Green</dd>
</dl>
```

Here is an unordered list:

- Salt-n-Pepa
- Bel Biv DeVoe
- Kid 'N Play

And an ordered list:

1. Michael Jackson
1. Michael Bolton
1. Michael Bublé

And an unordered task list:

- [x] Create a sample markdown document
- [x] Add task lists to it
- [ ] Take a vacation

And a "mixed" task list:

- [ ] Steal underpants
- ?
- [ ] Profit!

And a nested list:

- Jackson 5
    - Michael
    - Tito
    - Jackie
    - Marlon
    - Jermaine
- TMNT
    - Leonardo
    - Michelangelo
    - Donatello
    - Raphael

Definition lists can be used with HTML syntax. Definition terms are bold and italic.

<dl>
  <dt>Name</dt>
  <dd>Godzilla</dd>
  <dt>Born</dt>
  <dd>1952</dd>
  <dt>Birthplace</dt>
  <dd>Japan</dd>
  <dt>Color</dt>
  <dd>Green</dd>
</dl>

## 图像

```
Small images should be shown at their actual size.

![](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png)

Large images should always scale down and fit in the content container.

![](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_banner.png)
```

Small images should be shown at their actual size.

![](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png)

Large images should always scale down and fit in the content container.

![](https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_banner.png)

### 内置 figure 模板 (以及模板中使用多行文本的方法)

#### 不完全语法

```
{{</* figure
align="对齐方式(默认左对齐)"
src="图片地址"
title="标题(可选)"
caption="描述(可选,支持markdown语法)"
*/>}}
```

#### 例子

~~~
若你只想放置一个居中图片，一般使用如下代码 (注意，放置 purple logo 有专用模板)：

{{</* figure
align="center"
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
*/>}}

下面是别的例子：

{{</* figure
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption="**Purple**是一个位于~~五棵松~~五道口的_学生组织_"
*/>}}

{{</* figure
align="center"
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo (居中)"
caption="**Purple**是一个位于~~五棵松~~五道口的_学生组织_"
*/>}}

{{</* figure
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption=`多行文本示例：

**Purple**是一个

位于~~五棵松~~五道口的

_学生组织_`
*/>}}
~~~

若你只想放置一个居中图片，一般使用如下代码 (注意，放置 purple logo 有专用模板)：

{{< figure
align="center"
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
>}}

下面是别的例子：

{{< figure
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption="**Purple**是一个位于~~五棵松~~五道口的_学生组织_"
>}}

{{< figure
align="center"
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo (居中)"
caption="**Purple**是一个位于~~五棵松~~五道口的_学生组织_"
>}}

{{< figure
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption=`多行文本示例：

**Purple**是一个

位于~~五棵松~~五道口的

_学生组织_`
>}}

### 自定义 figure 模板 (以及模板中使用多行文本的方法)

- 总是居中并且占满屏幕宽度
- 可以指定多个图片，水平滚屏

#### 语法

```
{{</* figure_purple
prefix="图片地址前缀" (可选)
src="图片地址" (可以指定多个图片水平滚屏,用";"分隔)
aspect="可选，在多个图片水平滚屏时强制指定高度为宽度一定百分比，例如120%，若不指定则图片高度参差不齐"
title="标题(可选)"
caption="描述(可选,支持markdown语法)"
*/>}}
```

#### 例子

~~~
{{</* figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption="**Purple**是一个位于~~五棵松~~五道口的_学生组织_"
*/>}}

{{</* figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption=`多行文本示例：

**Purple**是一个

位于~~五棵松~~五道口的

_学生组织_`
*/>}}

{{</* figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_001.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_002.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_003.webp"
title="从左到右：雅克·拉康（Jacques Lacan）、路易·阿尔都塞（Louis Althusser）、朱迪斯·巴特勒（Judith Butler）"
*/>}}

{{</* figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_001.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_002.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_003.webp"
aspect="112%"
title="从左到右：雅克·拉康（Jacques Lacan）、路易·阿尔都塞（Louis Althusser）、朱迪斯·巴特勒（Judith Butler）"
*/>}}

使用前缀可以减小插入多个图片的工作量：

{{</* figure_purple
prefix="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_00"
src="1.webp;2.webp;3.webp"
aspect="112%"
title="从左到右：雅克·拉康（Jacques Lacan）、路易·阿尔都塞（Louis Althusser）、朱迪斯·巴特勒（Judith Butler）"
*/>}}
~~~

{{< figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption="**Purple**是一个位于~~五棵松~~五道口的_学生组织_"
>}}

{{< figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
title="Purple logo"
caption=`多行文本示例：

**Purple**是一个

位于~~五棵松~~五道口的

_学生组织_`
>}}

{{< figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_001.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_002.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_003.webp"
title="从左到右：雅克·拉康（Jacques Lacan）、路易·阿尔都塞（Louis Althusser）、朱迪斯·巴特勒（Judith Butler）"
>}}

{{< figure_purple
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_001.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_002.webp;https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_003.webp"
aspect="112%"
title="从左到右：雅克·拉康（Jacques Lacan）、路易·阿尔都塞（Louis Althusser）、朱迪斯·巴特勒（Judith Butler）"
>}}

使用前缀可以减小插入多个图片的工作量：

{{< figure_purple
prefix="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/2019-09-15-six-lectures-3/20190915_00"
src="1.webp;2.webp;3.webp"
aspect="112%"
title="从左到右：雅克·拉康（Jacques Lacan）、路易·阿尔都塞（Louis Althusser）、朱迪斯·巴特勒（Judith Butler）"
>}}

## 参考文献

### 语法

~~~
{{%/* bibitem id="名称(默认为[1],[2],[3]……自动增长)" */%}}
内容
{{%/* /bibitem */%}}
~~~

### 例子

~~~
{{%/* bibitem */%}}
内容
{{%/* /bibitem */%}}
{{%/* bibitem id="[9]" */%}}
多行<br>
内容

内容
{{%/* /bibitem */%}}
{{%/* bibitem id="[Fox21a]" */%}}
内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容
{{%/* /bibitem */%}}

放在引用环境会更好看一些 (这时多行内容有 bug)：

> {{%/* bibitem */%}}
内容
{{%/* /bibitem */%}}
> {{%/* bibitem */%}}
多行<br>
内容
{{%/* /bibitem */%}}
> {{%/* bibitem id="[Fox21b]" */%}}
内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容
{{%/* /bibitem */%}}
~~~

{{% bibitem %}}
内容
{{% /bibitem %}}
{{% bibitem id="[9]" %}}
多行<br>
内容

内容
{{% /bibitem %}}
{{% bibitem id="[Fox21a]" %}}
内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容
{{% /bibitem %}}

放在引用环境会更好看一些 (这时多行内容有 bug)：

> {{% bibitem %}}
内容
{{% /bibitem %}}
> {{% bibitem %}}
多行<br>
内容
{{% /bibitem %}}
> {{% bibitem id="[Fox21b]" %}}
内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容内容
{{% /bibitem %}}

.

## 文章卡片

### 语法

~~~
说明：需要放在
{{%/* quit_post_content */%}}
和
{{%/* /quit_post_content */%}}
之间，否则行距太大很难看

{{</* article_card
src="图片地址(可选,若未指定并且设置了page则会自动抓取)"
title="标题(可选,若未指定并且设置了page则会自动抓取)"
caption="描述(可选,支持markdown语法,若未指定并且设置了page则会自动抓取)"
size="big(大图片)或small(小图片),默认small"
href="链接地址(仅当page未设置时有效)"
page="链接到网站内部页面时,填写md源文件地址(例如post/xxx.md)"
height="强制指定封面图片的高度为宽度的一定比例，例如55%" (可选,仅在size为big时有效,会自动从page中抓取)
*/>}}
~~~

### 例子

~~~
{{%/* quit_post_content */%}}

{{</* article_card
src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
title="GitHub"
caption="Where the world builds software"
href="https://github.com"
*/>}}

{{</* article_card
title="第一讲 · 社会性别与性别的描述学"
caption="二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念"
*/>}}

{{</* article_card
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20190512_banner.webp"
title="第一讲 · 社会性别与性别的描述学"
caption="二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念"
size="big"
*/>}}

{{</* article_card
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20190512_banner_small.webp"
title="第一讲 · 社会性别与性别的描述学"
caption="二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念"
*/>}}

自动抓取示例：

{{</* article_card
page="post/2019-06-17-six-lectures-1.md"
size="big"
*/>}}

{{</* article_card
page="post/2019-06-17-six-lectures-1.md"
*/>}}

{{%/* /quit_post_content */%}}
~~~

{{% quit_post_content %}}

{{< article_card
src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
title="GitHub"
caption="Where the world builds software"
href="https://github.com"
>}}

{{< article_card
title="第一讲 · 社会性别与性别的描述学"
caption="二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念"
>}}

{{< article_card
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20190512_banner.webp"
title="第一讲 · 社会性别与性别的描述学"
caption="二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念"
size="big"
>}}

{{< article_card
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20190512_banner_small.webp"
title="第一讲 · 社会性别与性别的描述学"
caption="二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念"
>}}

自动抓取示例：

{{< article_card
page="post/2019-06-17-six-lectures-1.md"
size="big"
>}}

{{< article_card
page="post/2019-06-17-six-lectures-1.md"
>}}

{{% /quit_post_content %}}

## 山寨朋友圈

### 语法

~~~
{{%/* fake_pyq
avatar="头像图片地址"
image0="只发一个大图的图片地址(可选,若设置则忽略image1-image9属性)"
image1="第一行第一列图片地址(可选)"
image2="第一行第二列图片地址(可选)"
image3="第一行第三列图片地址(可选)"
...
image9="第三行第三列图片地址(可选)"
time="时间(默认26分钟前)"
*/%}}
文字内容
{{%/* /fake_pyq */%}}
~~~

### 例子

~~~
{{%/* fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
image1="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_101.webp"
image2="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_102.webp"
image3="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_103.webp"
image4="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_104.webp"
image5="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_105.webp"
image6="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_106.webp"
image7="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_107.webp"
image8="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_108.webp"
image9="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_109.webp"
*/%}}
**purple**

**#紫色校园日 #spiritday**<br>
LET'S GO PURPLE ！
{{%/* /fake_pyq */%}}

{{%/* fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
image1="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_101.webp"
image2="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_102.webp"
image4="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_103.webp"
image5="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_104.webp"
*/%}}
**purple**

**#紫色校园日 #spiritday**<br>
LET'S GO PURPLE ！
{{%/* /fake_pyq */%}}

{{%/* fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
image0="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20190512_banner.webp"
*/%}}
**purple**

第一讲 · 社会性别与性别的描述学<br>
二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念
{{%/* /fake_pyq */%}}

{{%/* fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
time="800年前"
*/%}}
**purple**

只有**文字**的_朋友圈_
{{%/* /fake_pyq */%}}
~~~

{{% fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
image1="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_101.webp"
image2="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_102.webp"
image3="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_103.webp"
image4="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_104.webp"
image5="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_105.webp"
image6="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_106.webp"
image7="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_107.webp"
image8="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_108.webp"
image9="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_109.webp"
%}}
**purple**

**#紫色校园日 #spiritday**<br>
LET'S GO PURPLE ！
{{% /fake_pyq %}}

{{% fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
image1="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_101.webp"
image2="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_102.webp"
image4="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_103.webp"
image5="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_104.webp"
%}}
**purple**

**#紫色校园日 #spiritday**<br>
LET'S GO PURPLE ！
{{% /fake_pyq %}}

{{% fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
image0="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20190512_banner.webp"
%}}
**purple**

第一讲 · 社会性别与性别的描述学<br>
二元社会性别的假定隐隐地保留了社会性别与生理性别是某种模拟关系的信念
{{% /fake_pyq %}}

{{% fake_pyq
avatar="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/purple_logo_256px.png"
time="800年前"
%}}
**purple**

只有**文字**的_朋友圈_
{{% /fake_pyq %}}

## 点击图片伸缩动画

### 语法

~~~
{{</* svg_animation_enlarge_image
src="图片地址"
width="宽度"
height="开始高度"
height2="结束高度"
dur="时间(默认1秒)"
*/>}}
~~~

### 例子

~~~
{{</* svg_animation_enlarge_image
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_001.webp"
width="343"
height="686"
height2="1044"
*/>}}

{{</* svg_animation_enlarge_image
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_002.webp"
width="343"
height="1044"
height2="686"
dur="10s"
*/>}}
~~~

{{< svg_animation_enlarge_image
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_001.webp"
width="343"
height="686"
height2="1044"
>}}

{{< svg_animation_enlarge_image
src="https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/20201015_002.webp"
width="343"
height="1044"
height2="686"
dur="10s"
>}}

## 折叠的内容 (Hugo 内置)

### 语法

~~~
{{%/* collapse
summary="标题,支持markdown语法"
openByDefault=初始时是否打开,默认为false(注意没有双引号!)
*/%}}
内容,支持markdown语法
{{%/* /collapse */%}}
~~~

### 例子

~~~
{{%/* collapse summary="标题,支持 **markdown** *语法*" */%}}
内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法

内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法

{{%/* collapse summary="我是嵌套" */%}}
内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法
{{%/* /collapse */%}}
{{%/* /collapse */%}}

{{%/* collapse summary="标题,支持 **markdown** *语法*" openByDefault=true */%}}
内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法
{{%/* /collapse */%}}
~~~

{{% collapse summary="标题,支持 **markdown** *语法*" %}}
内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法

内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法

{{% collapse summary="我是嵌套" %}}
内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法
{{% /collapse %}}
{{% /collapse %}}

{{% collapse summary="标题,支持 **markdown** *语法*" openByDefault=true %}}
内容,支持markdown语法 **内容,支持markdown语法** *内容,支持markdown语法* 内容,支持markdown语法
{{% /collapse %}}

## 插入目录 (过时)

~~~
{{</* toc */>}}
~~~

注：要插入目录，在文章头部设置 `ShowToc: true` 即可。

## purple 居中 logo

~~~
{{</* purple_logo_center */>}}
~~~

{{< purple_logo_center >}}

## 需要更多的声音！

~~~
{{</* need_more_voices */>}}
~~~

{{< need_more_voices >}}

# 文章头部格式

~~~~
---
title: "文章标题"
date: 文章日期 (若晚于当前日期则该文章不会显示)，格式 yyyy-mm-dd，示例: 2021-05-28
draft: 可选，false或true，表示是否草稿，草稿文章仅在本地预览可见，默认false
authors: 可选，格式 ["作者1", "作者2", ……]
cover:
  image: "封面图片地址" (可选，若指定则在文章最前面以及文章列表中显示封面图片，若不指定，请将 cover 和 image 都删掉)
  small: "封面小图片地址" (可选)
  hidden: true或false，若为true则仅在文章列表中显示封面图片，在文章最前面不显示 (可选，默认false)
  height: "强制指定封面图片在文章列表中显示的高度为宽度的一定比例，例如55%" (可选)
ShowToc: 可选，false或true，表示是否显示目录，默认false
tags: 可选，格式 ["标签1", "标签2", ……]
---
~~~~
