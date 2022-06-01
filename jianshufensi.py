import urllib.request,urllib.error
import re

# 网页中的粉丝数据如下：
from bs4 import BeautifulSoup

'''
<div class="info">
    <a class="name" href="/u/f945188c5987">燕小七_99d5</a>
      <i class="iconfont ic-woman"></i>
    <div class="meta">
      <span>关注 10</span><span>粉丝 0</span><span>文章 0</span>
    </div>
    <div class="meta">
      写了 0 字，获得了 0 个喜欢
    </div>
  </div>
'''

# 创建正则匹配
reList = []
reList.append(re.compile(r'<a class="name" href="/u/.*?">(.*?)</a>')) #匹配昵称
reList.append(re.compile(r'关注 (\d+)'))#关注
reList.append(re.compile(r'粉丝 (\d+)'))#粉丝
reList.append(re.compile(r'文章 (\d+)'))#文章


def GetUrl(Url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
    request = urllib.request.Request(Url,headers=head) #创建请求头对象
    html = ""
    try:
        response = urllib.request.urlopen(request)#访问
        html = response.read().decode("utf-8")#读取
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

# GetUrl("https://www.jianshu.com/users/e8f0defa170a/followers")

# 创建一个函数
def UserData(html):
    UserInfo = []
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="info"):
        item = str(item)
        row = [];
        for i in reList:
            info = re.findall(i, item)
            row.append(info)
        if row[0]:
            UserInfo.append(row)
    return UserInfo

x  = input("请输入要爬取的页数:")
for i  in range(1,int(x)):
    text  =  GetUrl("https://www.jianshu.com/users/e8f0defa170a/followers?page="+str(i))
    UserInfo = UserData(text)
    print('-------------第' + str(i) + "页-------------")
    # print(text)
    for row in UserInfo:
        for lies in row:
            print(lies,end=' ')

        print('')
