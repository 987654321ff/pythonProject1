import requests
from bs4 import BeautifulSoup
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}


def down4(image):
    print(time.time())
    filename = "./image11/" + str(int(time.time() * 1000)) + ".jpg"
    r = requests.get(image,headers= headers)
    f = open(filename,"wb")
    f.write(r.content)
    f.close()


def down3(text):
 soup = BeautifulSoup(text,"html.parser")
 tags = soup.find_all("img",class_="lazy")
 print(len(tags))
 for tag in tags:
     image = "https:" + tag['data-original']
     print(image)
     down4(image)





def down2(url):
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    print(r.status_code)
    down3(r.text)


def down1():
    for i in range(1, 3):
        url = "https://699pic.com/originality-0-176-" + str(i) + ".html"
        down2(url)


down1()
