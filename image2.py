# _*_coding:utf-8_*_
# 下载图片,注意需要判断图片的格式，某些地方需要特殊处理
# https://blog.51cto.com/u_15315508/3206431
from urllib.parse import urljoin
import requests
import re
import os


class GetImage(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.path = self.dir_path + '/imgs1'
        isExists = os.path.exists(self.dir_path + '/imgs1')
        # 创建目录
        if not isExists:
            os.makedirs(self.path)

    def download(self, url):
        try:
            res = requests.get(url, headers=self.headers)
            return res
        except Exception as E:
            print(url + '下载失败,原因:' + E)

    def parse(self, res):
        content = res.content.decode()
        # print(content)
        img_list = re.findall(r'<img.*?src="(.*?)"', content, re.S)
        img_list = [urljoin(self.url, url) for url in img_list]
        return img_list

    def save(self, res_img, file_name):
        if (file_name.endswith('jpg')) or (file_name.endswith('png')):
            file_name = file_name
        else:
            file_name = file_name + '.jpg'

        if res_img:
            with open(file_name, 'wb') as f:
                f.write(res_img.content)
            print(url + '下载成功')

    def run(self):
        # 下载
        res = self.download(self.url)
        # 解析
        url_list = self.parse(res)
        # 如果是以下链接，那么下载不成功，跳过
        breakUrl = 'data:image/png;base64,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'
        # 下载图片
        for url in url_list:
            # if url.__eq__(breakUrl):
            if url.__contains__('data:image/png;'):
                continue
            else:
                res_img = self.download(url)
                name = url.strip().split('/').pop()
                file_name = self.path + '/' + name
                # 保存
                self.save(res_img, file_name)


if __name__ == '__main__':
    url_list = ['https://www.jianshu.com/p/8a11293ab640']

    for url in url_list:
        text = GetImage(url)
        text.run()
