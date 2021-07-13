import re
import urllib.request
import os.path
import os
import io
from PIL import Image

SEPARATOR = '-'
DOT = '.'
IMAGE_FORMAT = 'webp'

input_path = input('请输入Markdown文件名：').strip()
input_file_name = os.path.basename(input_path).split(DOT)[0]
if os.path.dirname(input_path) == '':
    input_path = os.path.join(os.getcwd(), 'content', 'post', input_path)

with open(input_path) as input_file:
    lines = input_file.read()
    img_urls = re.findall(r'(https?:\/\/.*\.(?:png|jpg))', lines, re.IGNORECASE)
    print('发现以下图片：')
    for img_url in img_urls:
        print('\t' + img_url)
    output_path = os.path.join(os.getcwd(), input_file_name)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    print('图片将保存到{}'.format(output_path))
    for (i, img_url) in enumerate(img_urls):
        output_postfix = img_url.split(DOT)[-1]
        output_base_name = input_file_name + SEPARATOR + str(i) + DOT + IMAGE_FORMAT
        output_file_name = os.path.join(output_path, output_base_name)
        img_data = urllib.request.urlopen(img_url).read()
        img = Image.open(io.BytesIO(img_data))
        img.save(output_file_name, IMAGE_FORMAT, optimize=True)

        print('进度: {:.2f}%'.format(i/len(img_urls) * 100), end='\r')
    print('下载完成！', end='\r')

# def download_and_compress():
#     img_data = urllib.request.urlopen(img_url).read()
#     img = Image.open(io.BytesIO(img_data))
#     img.save(output_file_name, IMAGE_FORMAT, optimize=True,quality=80)
