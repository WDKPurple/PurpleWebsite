# image-download-utils.py 使用方法

1. 下载Python（[链接](https://www.python.org/downloads/)）
2. 使用 Python 运行文件：`python image-download-utils.py` 或者 `python3 image-download-utils.py`
3. 输入包含图片链接的文档名（我一般首先将mhtml文件拷贝到Typora中转成Markdown格式文件，并把不需要下载的图片，比如Purple logo等删掉），如果文件不在 `.../PurpleWebsite/content/post` 文件夹下，请输入整个文件路径
4. 图片会下载，压缩成webp格式并保存到 `.../PurpleWebsite/<文档名>/<文档名>-<编号>.webp`
5. 可以将整个文件夹上传到StaticResource里，即可通过 `https://cdn.jsdelivr.net/gh/WDKPurple/StaticResources/images/...` 来在文档中引用图片

