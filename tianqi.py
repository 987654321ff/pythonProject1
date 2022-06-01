# 获取天气的方法
import requests
from lxml import etree


def get_weather(city):
    # 天气的网站网址  字符串
    url = 'https://www.tianqi.com/' + city + '/'

    # 伪装浏览器的马甲
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'
    }

    # 发起网络请求并获取网页代码
    website = requests.get(url=url, headers=headers)

    data = etree.HTML(website.text)     # 数据预处理
    #xpath解析页面天气数据
    weather_list = data.xpath('//dl[@class="weather_info"]//text()')


    weather_text = '欢迎使用天气播报助手，以下是你想要了解的城市天气:\n'

    for text in weather_list:
        weather_text += text
        if weather_text.find('[切换城市]'):
            weather_text = weather_text.strip('[切换城市]')

    print(weather_text)
    return weather_text


if __name__ == '__main__':
    city = input('请输入您的城市,例如长沙:changsha-->').strip()
    weather_info = get_weather(city)        # weather_info来获取抓取到的天气文字
    # weather = pyttsx3.init()            # 初始化说话的对象
    # weather.say(weather_info)           # 设置说话内容
    # weather.runAndWait()                # 开始执行说话的操作
