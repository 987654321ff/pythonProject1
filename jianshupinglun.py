import json

import  requests
from lxml import etree
from time import sleep


url = "https://www.jianshu.com/shakespeare/notes/60479187/comments?page=1&count=100&author_only=false&order_by=desc"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Refer":"https://www.jianshu.com"
}

resp = requests.get(url,headers=headers)
content = resp.content.decode('utf-8')
res = json.loads(content)
data = res['comments']
print(data)
