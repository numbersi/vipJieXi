#coding:utf8
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify
from . import home
@home.route('/', methods=['GET', 'POST'])
def hello_world():
    url = request.args.get("url") or "args没有参数"
    apiUrl = 'http://yun.baiyug.cn/vip/index.php?url='
    url = apiUrl + url
    html =  getUrl_Baiyug(url)

    if 'hdMd5' in html:
        print('have hdMd5')
        html = html.replace('src="baiyug', 'src="http://youkus.baiyug.cn:3697/vip_all/baiyug', -1)
        html = html.replace('baiyug.php','baiyug')
        print(html)
        return html
    cndJs  = { 'https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.js' : 'js/DPlayer.min.js',
   ' https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.css': 'js/DPlayer.min.css',
    'https://cdn.bootcss.com/hls.js/0.9.1/hls.min.js' :   'js/hls.min.js',
    'https://cdn.bootcss.com/flv.js/1.4.2/flv.min.js': 'js/flv.min.js'
               }
    for key in cndJs:
        html =  html.replace(cndJs[key],key)
    print(html)
    return  html

@home.route('/baiyug', methods=['POST'])
def baiyug():
    datax = request.form.to_dict()

    res = requests.post('http://youkus.baiyug.cn:3697/vip_all/baiyug.php',datax)
    return res.content

    print(datax)
    return  'baiyug'
def getUrl_Baiyug (url):
    if   url.startswith('/') :
        url = 'http://yun.baiyug.cn'+ url
    obj = requests.get(url, allow_redirects=False)
    html = obj.content.decode('utf-8')
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        return getUrl_Baiyug( iframes['src'])
    else:

        return  html