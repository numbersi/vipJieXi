import json
import re

import requests
from bs4 import BeautifulSoup
url = 'http://api.xcq91.top/?url=https://v.youku.com/v_show/id_XMzgwMzg4MzIzNg==.html'
url ='http://vip.xcq91.top/player/index.php?url=https://v.youku.com/v_show/id_XMzgwMzg4MzIzNg==.html'
headers = {
'Host': 'vip.xcq91.top',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://api.xcq91.top/?url=https://v.youku.com/v_show/id_XMzgwMzg4MzIzNg==.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
}

a ='''Host: vip.xcq91.top
Connection: keep-alive
Content-Length: 604
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://vip.xcq91.top
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9'''

html = requests.get(url,headers=headers).content.decode()
obj = BeautifulSoup(html, 'lxml')
params = re.search(r'\.php",(\{.*?\}),',html).group(1)
url = 'http://vip.xcq91.top/player/api.php'
print(params)
print(json.loads(params))
html = requests.post(url,data=params,headers={'Host': 'vip.xcq91.top', 'Connection': 'keep-alive', 'Content-Length': '604', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://vip.xcq91.top', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}).content.decode()
print(html)
