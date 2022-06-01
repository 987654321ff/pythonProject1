
import requests
from bs4 import BeautifulSoup

def douban_Movie_Notion(moive_id):
    headers={'user-agent': '23'}
    output = {}
    url_head='https://movie.douban.com/subject/'
    url = url_head+moive_id
    res=requests.get(url, headers=headers)
    bstitle=BeautifulSoup(res.text, 'html.parser')

    moive_content = bstitle.find_all('div', id='content')[0]

    # 电影名称与年份
    title = moive_content.find('h1')
    title = title.find_all('span')
    title = title[0].text+title[1].text

    # 评分
    Rating = moive_content.find('div',id='interest_sectl')
    Rating1 = Rating.find('div',class_='rating_self clearfix')
    rating_num = Rating1.find('strong',class_='ll rating_num').text.replace(" ", "")
    rating_sum = Rating1.find('div',class_='rating_sum').text.replace(" ", "").replace("\n", "")

    rating_betterthan = Rating.find('div',class_='rating_betterthan').text.replace(" ", "").replace("\n", "")

    # 图片连接
    base_information = moive_content.find('div',class_='subject clearfix')
    mianpic = base_information.find('div',id='mainpic')
    mianpic_id = mianpic.find('img')['src']

    # 基本信息
    info = base_information.find('div',id='info').text.split('\n')
    Info = {}
    for i in info:
        if len(i)>1:
            iifo = i.split(':')
            Info[iifo[0]] = iifo[1]

    # 剧情简介
    sim_intro = moive_content.find('div',class_='related-info').text.replace(" ", "").replace("\n", "").replace("　", "").split('······')

    output['电影名称与年份'] = title
    output['评分分数'] = rating_num
    output['评分人数'] = rating_sum
    output['评分好于'] = rating_betterthan
    output['图片连接'] = mianpic_id
    output['基本信息'] = Info
    output['简介'] = sim_intro[1]

    return output


# content = douban_Movie_Notion("35008440")
# print(content)


