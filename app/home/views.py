#coding:utf8
import re
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify ,render_template
from . import home
@home.route('/', methods=['GET', 'POST'])
def hello_world():
    url = request.args.get("url") or "args没有参数"
    apiUrl = 'http://yun.baiyug.cn/vip/index.php?url='
    url = apiUrl + url
    html =  getUrl_Baiyug(url)


    return  html

@home.route('/baiyug', methods=['POST'])
def baiyug():
    datax = request.form.to_dict()
    print(datax)
    host = datax['host']
    res = requests.post(host+'/vip_all/baiyug.php',datax)
    return res.content

def getUrl_Baiyug (url):
    if   url.startswith('/') :
        if url.startswith('//'):
            url ='http:'+ url
        else:
            url = 'http://yun.baiyug.cn' + url
    obj = requests.get(url, allow_redirects=False)
    html = obj.content.decode('utf-8')
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        print('have')
        return getUrl_Baiyug( iframes['src'])
    else:
        print('not have')
        print(url)
        host ='http://' + url.split('/')[2]

        print(host)
        if not html:
            # print(url)
            # res =  requests.get(url)
            # HTML= res.content.decode('utf-8')
            # print(url.split('/')[2])
            # print(HTML)
            # d = re.search(r'"(.+m3u8)', HTML).group(1)
            # print(url.split('/')[2]+'/'+d)
            return render_template('home/player.html')
        if 'hdMd5' in html:
            print('have hdMd5')
            html = html.replace('src="baiyug', 'src="'+ host+ '/vip_all/baiyug', -1)
            html = html.replace('href="baiyug', 'src="'+ host+ '/vip_all/baiyug', -1)
            html = html.replace('baiyug.php', 'baiyug')
            reStr = ' host :"{}" ,"md5"'.format(host)
            html = re.sub(r'"md5"',reStr,html)
            return html
        cndJs = {'https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.js': 'js/DPlayer.min.js',
                 ' https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.css': 'js/DPlayer.min.css',
                 'https://cdn.bootcss.com/hls.js/0.9.1/hls.min.js': 'js/hls.min.js',
                 'https://cdn.bootcss.com/flv.js/1.4.2/flv.min.js': 'js/flv.min.js'
                 }
        for key in cndJs:
            html = html.replace(cndJs[key], key)
        return  html