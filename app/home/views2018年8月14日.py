#coding:utf8
import json
import re
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify, render_template, make_response, url_for
from . import home
@home.route('/', methods=['GET', 'POST'])
def hello_world():
    url = request.args.get("url") or "args没有参数"
    apiUrl = 'http://206dy.com/vip.php?url='
    url = apiUrl + url
    data  =getUrl_206dy(url)
    print(data)
    return  render_template('home/player.html',data=data)

@home.route('/js', methods=['GET', 'POST'])
def js():
    return  '<script src="js/.js" type="text/javascript"></script>'
def getUrl_206dy (url,Referer=''):
    headers = { "Referer":Referer}
    host = url.split('/')[2]

    if   url.startswith('/') :
        if url.startswith('//'):
            url ='http:'+ url
        else:
            url = 'http://'+host + url
    print(url)
    obj = requests.get(url,
                       # allow_redirects=False,
                       headers =headers)
    html = obj.content.decode('utf-8')
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        print( 'have ifarme')
        return getUrl_206dy( iframes['src'],url)
    else:
        if '<iframe' in html:
            print( 'have <iframe')
            res = re.search(r'<iframe name ="iframe-player" src="(.*)" width="100%"', html)
            return getUrl_206dy(res.group(1),url)
        print('no ifarme')
        if 'domain' in html:
            domain = re.search(r'var domain = "?(.*)"/?;', html).group(1)
            url = re.search(r'var url = "?(.*)"/?;',html).group(1)
            tm = re.search(r'var tm = "?(.*)"?;',html).group(1)
            vuid = re.search(r'var vuid = "?(.*)"?;',html).group(1)
            key = re.search(r'var key = "?(.*)"/?;',html).group(1)
            URL = domain + '/parse.php?url=' + url + '&tm=' + tm + '&vuid=' + vuid + '&key=' + key
            res = requests.get(
                URL,
                allow_redirects=False,
            )
            jsonStr =res.content.decode('utf8')
            return json.loads(jsonStr)
        if '27pan' in html:
            d = re.search(r'"/(.+m3u8)', html).group(1)
            host = '//'.join([url.split('/')[0],url.split('/')[2]])
            print(host+d)

@home.route('/38')
def m38():
    url = request.args.get("url") or "args没有参数"

    res = requests.get(
        'http://pl.cp12.wasu.tv/playlist/m3u8?ts=1533835112&keyframe=0&m3u8Md5=ed7601ef1022241daef6f86813264ffd&vid=XMzc1NTk5OTkyOA==&type=flv&guid=7066707c5bdc38af1621eaf94a6fe779&ver=3.9.4&pid=87c959fb273378eb&sid=0533835112500305ed950&token=9383&oip=2006029515&did=&ctype=30&ev=1&ep=SmsFRhXLwSSrapo3DDbOiAkPeIV2OAfkc0aAFcbQMdrVXutIcwW06l%2B0eRwQHjHY')
    resp =     make_response(res.content.decode('utf-8'))
    # print(res.content.decode('utf-8'))
    # return res.content.decode('utf-8')
    return  'res',{'Content-Disposition': 'attachment; filename=myfilename.m3u8'}