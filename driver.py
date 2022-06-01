import requests
from lxml import etree
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
for i in range(1,4):
    url_ = 'https://www.jianshu.com/u/05f416aefbe1?order_by=shared_at&page={}'.format(i)
    res = requests.get(url_,headers=headers)
    res = etree.HTML(res.content.decode())
    nodes = res.xpath('//ul[@class="note-list"]/li')
    for node in nodes:
        item = {}
        title = node.xpath('.//a[@class="title"]/text()')
        time = node.xpath('.//span[@class="time"]/@data-shared-at')[0]
        abstract = node.xpath('.//p[@class="abstract"]/text()')[0]
        img = node.xpath('.//img[@class="  img-blur-done"]')
        url = 'https://www.jianshu.com'+node.xpath('.//a/@href')[0]
        item['title'] = title
        item['time'] = time
        item['url'] = url
        item['abstract'] = title
        item['img'] = time
        print(item)
