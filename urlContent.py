import requests

# 请求网页
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'cookie': 'pgv_pvi=2389011456; RK=x4Sdy3WsT4; ptcz=4a2fe0ffda6742a230c94f168291afcce2bd001e5d6615132b55da90559cd463; pgv_pvid=6989331736; _ga=GA1.2.735850052.1585832762; ptui_loginuin=1207020736; ua_id=iJuK7hnHjcUE0e2dAAAAAHzCRcatCWOiHc-hdkhSDL4=; __guid=166713058.1972731636944397800.1590316882436.5461; openid2ticket_oY8wqwesgvgkdQ69wUeM5UxhOV5c=ION52/k2w4M3o44iht5BRt5yCyxP/3IaRXJ84RIpRZA=; mm_lang=zh_CN; pac_uid=0_5ecd1592971c3; uin=o1240069166; skey=@YLtvDuKyj; pgv_info=ssid=s4875389884; pgv_si=s8410697728; uuid=62839906b2a77b5f098cd91979af8b33; rand_info=CAESIC53TQFCwjIe4ZsrTRKvSs+ocfs4UTsj9swrrNwosjCd; slave_bizuin=3240807523; data_bizuin=3240807523; bizuin=3240807523; data_ticket=AiTk/OFWXCKxhaenCvEuP06mwWTI6YqCyt+74hoaXaNtKBbcnq//ZTXHzqByMhK6; slave_sid=YndxeFhCSkU5OUJtdFYycW9zN29FcG51NU5GNElBM3I2RF9wVjJBRGx2bWxrTXdiMDZFYzllUWNaMlN4N0RsOTlVMDRxZFZEMjJXdlRZcXBVOGptQ2ZDSVZiOEJlQW5BZDVCWlkzSnJ6WWNPWVRiN1J0cldCd0pvbTc3RGRiMm9pZ3ZISTl6WWhDUmNCZ2s3; slave_user=gh_5d822fe7fd08; xid=9794daa60db66fcf7a65c4054e3d68ce; mmad_session=43d4e5247a6b025b67ba3abd48d27a309ec4713911b6ef6f23cddb4b9953e771354ad1572fbc3fa895051725e95abb887cf2d03e9864084974db75c8588189699ea5b20b8fe35073831446ef98d24de600f107fe69d79646a3dd2907ab712e1f11de1c56c245721266e7088080fefde3; ts_last=mp.weixin.qq.com/cgi-bin/frame; ts_uid=1963034896; monitor_count=15'
}#请求头信息，这里cookie信息必须添加，否则得不到网页信息
url='https://www.freesion.com/article/23781297259/'
# url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MjM5MjAxMDM4MA==&type=9&query=&token=59293242&lang=zh_CN&f=json&ajax=1'

response=requests.get(url,headers=headers)#得到响应内容
response.encoding='utf-8'#设置响应内容为utf-8格式
html = response.text#得到网页的文本形式
print(html)


