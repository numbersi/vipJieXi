import  requests


html = requests.get('https://zuidajiexi.net/m3u8.html?url=http://cn2.zuidadianying.com/20180811/FjyjdED7/index.m3u8').content.decode()
print(html)