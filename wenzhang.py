import requests
from re import findall
from bs4 import BeautifulSoup
import time
import os

weixin_title=""
weixin_time=""

#获取微信公众号内容,保存标题和时间
def get_weixin_html(url):
    global weixin_time,weixin_title
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")

    #获取标题
    temp=soup.find('h1')
    weixin_title=temp.string.strip()

    #使用正则表达式获取时间
    result=findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}.+:[0-9]{2}',res.text)
    weixin_time=result[0]

    #获取正文html并修改
    content=soup.find(id='js_content')
    soup2=BeautifulSoup((str(content)),"html.parser")
    soup2.div['style']='visibility: visible;'
    html=str(soup2)
    pattern=r'http[s]?:\/\/[a-z.A-Z_0-9\/\?=-_-]+'
    result = findall(pattern, html)

    #将data-src修改为src
    for url in result:
        html=html.replace('data-src="'+url+'"','src="'+url+'"')

    return html

#上传图片至服务器
def download_pic(content):

    pic_path='pic/'
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)

    #使用正则表达式查找所有需要下载的图片链接
    pattern=r'http[s]?:\/\/[a-z.A-Z_0-9\/\?=-_-]+'
    pic_list = findall(pattern, content)

    for index, item in enumerate(pic_list,1):
        count=1
        flag=True
        pic_url=str(item)

        while flag and count<=10:
            try:
                 data=requests.get(pic_url);

                 if pic_url.find('png')>0:
                     file_name = str(index)+'.png'

                 elif pic_url.find('gif')>0:
                     file_name=str(index)+'.gif'

                 else:
                     file_name=str(index)+'.jpg'

                 with open( pic_path + file_name,"wb") as f:
                     f.write(data.content)

                 #将图片链接替换为本地链接
                 content = content.replace(pic_url, pic_path + file_name)

                 flag = False
                 print('已下载第' + str(index) +'张图片.')
                 count += 1
                 time.sleep(1)

            except:
                 count+=1
                 time.sleep(1)

        if count>10:
            print("下载出错：",pic_url)
    return content

if __name__ == "__main__":

    #获取html
    # input_flag=True
    # while input_flag:
    #    weixin_url=input('请输入微信文章链接后按Enter：')
    #    re=findall(r'http[s]?:\/\/mp.weixin.qq.com\/s\/[0-9a-zA-Z_]+',weixin_url)
    #    if len(re)<=0:
    #         print("链接有误，请重新输入!")
    #    else:
    #        input_flag=False

    content=get_weixin_html("http://mp.weixin.qq.com/s?__biz=Mzg2NjY3NzgxOQ==&mid=2247484488&idx=1&sn=2636c2c57bf2c091275b7b8a334ce7d5&chksm=ce46611cf931e80a485f8aa4e121c500eba58d12b6cd0dd924ed75b9803da4faef07a0ba52b5&mpshare=1&scene=24&srcid=0427mDKBi64YyPbHj8UaPDcM&sharer_sharetime=1651021396690&sharer_shareid=966feb236040cc28ee06487b1bd98188#rd")
    content=download_pic(content)
    #保存至本地
    with open(weixin_title+'.txt','w+',encoding="utf-8") as f:
        f.write(content)
    with open(weixin_title+'.html','w+',encoding="utf-8") as f:
        f.write(content)

    print()
    print("标题：《"+weixin_title+"》")
    print("发布时间："+weixin_time)
