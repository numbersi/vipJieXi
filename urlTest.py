import requests
import re
def getDoubanID(name):
    url  ="https://www.douban.com/search?q="+name
    html  =  requests.get(url).content.decode()
    obj = BeautifulSoup(html, 'xml')
    a = str(obj.find('a',['class','nbg']))
    if re.search(r'sid: ([0-9]*),' ,a):

        movieId = re.search(r'sid: ([0-9]*),' ,a).group(1)
        return movieId
    pass
from bs4 import BeautifulSoup

def getDataByname(name,page=1):
    # 采集 搜索名字
    url = "http://cj2.tv6.com/mox/inc/api.php?ac=list&pg={}&wd={}".format(page,name)
    # url = 'http://cj2.tv6.com/mox/inc/api.php?ac=videolist&pg=&ids=49263'
    html = requests.get(url).content.decode()
    obj = BeautifulSoup(html,'xml')
    print(obj)
    videos = obj.find_all('video')
    for video in videos:
        print(video.id.text)
        last = video.last
        print(last.text,end='\n')
        name = video.find('name').text
        print('#'*100)
        # movieId = getDoubanID(name)
        print(name)
    return 
if __name__ == '__main__':
    kword= '天才'
    getDataByname(kword)
