# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import 记账
from bs4 import BeautifulSoup

# url = "https://www.baidu.com/s?"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
# }
# data = {
#     'wd': '北京'
# }
# # url请求路径 params参数 kwargs字典
# response = requests.get(url=url, params=data, headers=headers)
# # 参数使用params传递，且参数无需url encode编码 ，且参数也不需要对象定制，请求资源路径中的?可加可不加
# print(response.text)


# url = "https://api.notion.com/v1/pages/4a2c9f40c27e478fba4de58af0787a69"
# headers = {"Authorization": "Bearer " + "3398c6a7d7e74c41b8bf42bb19ccfac4", "Notion-Version": "2021-05-13"}
#
# # url请求路径 params参数 kwargs字典
# response = requests.get(url=url, headers=headers)
# # 参数使用params传递，且参数无需url encode编码 ，且参数也不需要对象定制，请求资源路径中的?可加可不加
# print(response.text)


# 通过 Notion API 拉取数据
# NotionData = requests.request(
#     # POST 提交，GET 拉取
#     "GET",
#     # API 链接，不同操作类型的 API 链接不同
#     # 在前文由于我们要创建的是数据库中的记录即页面，因此在这里我们拉取的也是页面类型 pages
#     # 后面需要指明所拉取的页面 ID
#     "https://imminent-skunk-294.notion.site/day1-31c6805a8fe24d21bb0358536476d9c4",
#     # 前文已介绍过
#     headers={
#         "Authorization": "31c6805a8fe24d21bb0358536476d9c4",
#         "Notion-Version": "2021-05-13"
#         },
#     )
#
# print(NotionData.content)
# 创建机器人的token
token = "secret_39U6k89PZo9SD8qOCjHLa3HIdrLtQH85kbP3Ut6mVN3"
# 某个界面的id,
# 由以上数据可请求出最终界面的database_id
page_id = "09752c1e9fc4444b93dbf0b818b0a4c2"
r = requests.request(
    "GET",
    "https://api.notion.com/v1/pages/" + page_id,
    headers={"Authorization": "Bearer " + token, "Notion-Version": "2021-05-13"},
)
print(r.text)

# 测试记账数据
conte = 记账.wechat("C:/Users/valuechaintech/Desktop/微信支付账单(20220430-20220530).csv")


# body = {
#     "parent": {"type": "database_id", "database_id": "e13ff198-10f8-454f-8fef-7917a17b63e8"},
#     "properties": {
#         "价格": {"rich_text": [{"text": {"content": "sdffsdsdff"}}]},
#         "时间": {"rich_text": [{"text": {"content": "2022:05:30"}}]},
#         "标签": {"rich_text": [{"text": {"content": "事的发生地方撒"}}]},
#         "内容": {"rich_text": [{"text": {"content": "发的是按多少分"}}]},
#         "来源": {"rich_text": [{"text": {"content": "撒干啥啊噶啥都发"}}]},
#         "Name": {"title": [{"text": {"content": "112噶大事发生的方式的发生131"}}]},
#     },
# }
#
# result = requests.request(
#     "POST",
#     "https://api.notion.com/v1/pages",
#     json=body,
#     headers={"Authorization": "Bearer " + "secret_39U6k89PZo9SD8qOCjHLa3HIdrLtQH85kbP3Ut6mVN3", "Notion-Version": "2021-05-13"},
# )
# print(result.status_code)
# print(result.text)
# print(result.headers)






