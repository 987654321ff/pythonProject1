# @Time:2022/1/1312:04
# @Author:中意灬
# @File:斗破2.py
# @ps:tutu qqnum:2117472285
import time
import requests
from lxml import etree
def download(url,title):#下载内容
    resp=requests.get(url)
    resp.encoding='utf-8'
    html=resp.text
    tree=etree.HTML(html)
    body = tree.xpath("/html/body/div/div/div[4]/p/text()")
    body = '\n'.join(body)
    with open(f'斗破2/{title}.txt',mode='w',encoding='utf-8')as f:
        f.write(body)


def geturl(url):#获取子链接
    resp=requests.get(url)
    resp.encoding='utf-8'
    html=resp.text
    tree=etree.HTML(html)
    lis=tree.xpath("/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/ul/li")
    for li in lis:
        href=li.xpath("./a/@href")[0].strip('//')
        href="http://"+href
        title=li.xpath("./a/text()")[0]
        download(href,title)


if __name__ == '__main__':
    url="http://www.doupo321.com/doupocangqiong/"
    t1=time.time()
    geturl(url)
    t2=time.time()
    print("耗时：",t2-t1)
