import requests
from lxml import etree

url="https://www.jianshu.com/c/qqfxgN?utm_campaign=haruki&utm_content=note&utm_medium=reader_share&utm_source=qq"

def getHtml(url):
    '''
    获取网页源码
    return html
    '''
    headers = {
        "Host": "www.jianshu.com",
        "Referer": "https://www.jianshu.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    req = requests.get(url, headers=headers)

    html = etree.HTML(req.text)

    return html

def parse(html):
    '''
    解析网页
    '''
    nodes = html.xpath("//ul[@class='note-list']/li//div[@class='content']")

    for node in nodes:

        title = node.xpath(".//a[@class='title']/text()")[0]
        nickname = node.xpath(".//div[@class='meta']/a/text()")[0]
        comment = node.xpath(".//div[@class='meta']/a//text()")[2].strip()
        like = node.xpath(".//div[@class='meta']/span/text()")[0].strip()

        essay = {
            "title" : title,
            "nickname" : nickname,
            "comment" : comment,
            "like" : like
        }

        print("文章信息：{}".format(essay))

def main():
    html = getHtml(url)
    parse(html)

if __name__ == '__main__':
    main()
