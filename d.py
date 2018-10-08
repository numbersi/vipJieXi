import requests


# h = requests.get('https://206dy.com/vip.php?url=https://v.qq.com/x/cover/pkj1a9xu2mdwphn.html').content.decode()
# h = requests.get('https://le.206dy.com/vip.php?url=https://v.qq.com/x/cover/pkj1a9xu2mdwphn.html').content.decode()
url ='https://le.206dy.com/v.php/?url=https://v.qq.com/x/cover/pkj1a9xu2mdwphn.html'
url = 'http://yun.baiyug.cn/vip/api.php?url=V1ZWb1UwMUhUa1ZpTTFwTlRUSlJlbHBJYXpGa1JtOTZWV3BLVFdKVk5USlpiRTAxWVZWNE5sUlliRTVTUmxZMFZERk5ORTFGTlhGU1ZFSlFVa1ZHTkZSSE1XOU5SMHBZWkhvd1BRPT0='
h = requests.get(url,allow_redirects=False).content.decode()


print(h)
