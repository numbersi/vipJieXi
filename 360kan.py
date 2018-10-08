import requests
from bs4 import BeautifulSoup
def getList(cat,pageno):
    url =  'https://www.360kan.com/{}/list?cat=all&act=all&area=all&rank=rankhot&{}=1'.format(cat,pageno)
    html = requests.get(url).content.decode()
    obj = BeautifulSoup(html, 'lxml')
    items = obj.find_all('li', ['class', 'item'])
    for item in items:
        print(item.find('span', ['ckass', 's1']).text)

if __name__ == '__main__':
    getList('zongyi',1)
