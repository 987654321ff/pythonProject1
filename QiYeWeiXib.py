import requests
import json

class WXWork_SMS :

    # 文本类型消息
    def send_msg_txt(self) :
        headers = {"Content-Type" : "text/plain"}
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=69e3bed5-a20e-45be-9999-e30c0398c16c"
        send_data = {
            "msgtype": "text",  # 消息类型，此时固定为text
            "text": {
                "content": "上海今日天气：32度，大部分多云，降雨概率：10%",  # 文本内容，最长不超过2048个字节，必须是utf8编码
                "mentioned_list":["@all"],  # userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
                "mentioned_mobile_list":["@all"]  # 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
            }
        }

        res = requests.post(url = send_url, headers = headers, json = send_data)
        print(res.text)

if __name__ == '__main__' :
    sms = WXWork_SMS()
    sms.send_msg_txt()
