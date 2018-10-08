import requests
url ='https://v.tt-hk.cn/jx.php?url=http://v.youku.com/v_show/id_XMzgzNzEyNDg5Mg==.html'
headersStr = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
pragma: no-cache
referer: http://api.bbbbbb.me/yunjx/?url=http://v.youku.com/v_show/id_XMzgzNzEyNDg5Mg==.html
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'''
headers = {}
for item in  headersStr.split('\n'):
    c= item.split(': ')
    print(c)
    headers.update({c[0]:c[1]})
print(headers)
html = requests.get(url,headers=headers)
