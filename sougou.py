import requests
from lxml import etree
# 引入random是为了可以随机的从代理IP中抽取一个IP
import random
# punctuation为标点符号集,为了删除文章题目中的标点符号
from string import punctuation
import re
import time


def download(url):
    """
    下载网址内容，返回选择器
    :param url: 网址
    :return: 对应网址选择器
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    # 定义代理IP列表
    time.sleep(2)
    proxies = [
        {"HTTPS": "https://117.69.201.218:24907"},
        {"HTTPS": "https://117.57.91.57:46149"},
        {"HTTPS": "https://117.91.133.18:9999"},
        {"HTTPS": "https://183.129.207.78:18118"}
    ]
    # random.choice 从列表中随机选取一个
    r = requests.get(url, proxies=random.choice(proxies), headers=headers)
    # r = requests.get(url, headers=headers)
    # 设置编码方式
    r.encoding = 'utf-8'
    return etree.HTML(r.text)


def spider_detail(article_url):
    """
    爬取某一篇文章的标题和内容,并写文件
    :param article_url: 文章URL
    """
    selector = download(article_url)
    title = selector.xpath('//h2[@class="rich_media_title"]/text()')[0].strip()
    content = selector.xpath('string(//*[@class="rich_media_content "])').strip()
    data_write(content, title)


def data_write(content, title):
    """
    保存文章的题目和内容
    # 在字符串前面加上一个r表示原生字符串
    # 不转义字符不需要再次被转义
    # 即字符串均为显示内容,无任何转义内容
    :param content: 内容
    :param title: 题目
    """
    title = re.sub(r'[{}]+'.format(punctuation), '', title)
    with open('./wenzhang/' + title + '.txt', 'wt', encoding='utf-8') as f:
        f.write(content)
        print('正在下载：', title)


def spider(num):
    for i in range(1, num+1):
        url = 'https://weixin.sogou.com/pcindex/pc/pc_0/{}.html'.format(i)
        selector = download(url)
        all_article = selector.xpath('/html/body/li')
        for article in all_article:
            article_url = article.xpath('div[2]/h3/a/@href')[0]
            spider_detail(article_url)

page_count = input("请输入您想爬取的页数：")
spider(page_count)
