# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import bs4

# url = "http://httpbin.org/get"
# response = requests.get(url)
# print(response.headers)
# print(response.content)

#!/usr/bin/env python

# -*- coding: utf-8 -*-

_author_ = 'GavinHsueh'

#要抓取的目标页码地址
url = 'http://www.ranzhi.org/book/ranzhi/about-ranzhi-4.html'
#抓取页码内容，返回响应对象
response = requests.get(url)
#查看响应状态码
status_code = response.status_code
#使用BeautifulSoup解析代码,并锁定页码指定标签内容
# content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
# element = content.find_all(id='book')
print(status_code)
# print(element)




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('hello word')


def test(word):
    print(1111,"sdfasdfsadfsadf")


    #!/usr/bin/python3

# 第一个注释
print ("Hello, Python!") # 第二个注释


print('hello','wordddddd')


if True:
    print("True")
    print("我是来测试的")
else:
    print("False")
print ("Answer")


total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

print (total)


str='123456789'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
#这里的 r 指 raw，即 raw string，会自动将反斜杠转义，例如：
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


print('\n')



print(r'\n')

# input("\n\n按下 enter 键后退出。")

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x="aa"
y="bb"
print(x)
print(y)
print("===================")
print(x,end=" ")
print(y,end=" ")


# if __name__ == '__main__':
#     base_url = "https://api.notion.com/v1/"
#     token = "XXXXXXXXXXXXXXXXXXXXXXXXX"
#     pageID = "9815fe09-cb27-46ee-9417-1d9131b7d53f"
#     databaseID = create_database(base_url, pageID, token)
#     create_page(base_url, databaseID, token


