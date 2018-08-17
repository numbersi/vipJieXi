#coding:utf8
import re
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify, render_template, make_response, url_for
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
    host = datax['host']
    res = requests.post(host+'/vip_all/baiyug.php',datax)
    return res.content


@home.route('/md5/<md5value>')
def md5html(md5value):
    print('md5htmlmd5value')

    return render_template('home/md5.html',md5value=md5value)
def jiexiHdMd5(html,url):
    '''
    id: http://tv.sohu.com/v/MjAxODA3MTYvbjYwMDU3MDgyNi5zaHRtbA==.html
    type: sohu
    siteuser:
    host: http://youkus.baiyug.cn:3699
    md5: ab59f0c8188ab5d647cfc89528caloij
    hd:
    lg:
    :param html:
    :param url:
    :return:
    '''
    md5value =  re.search(r'value="(.{32})', html).group(1)

    md5 =  url_for('home.md5html',md5value=md5value)
    print(md5)
    res= requests.get(' http://127.0.0.1:5000/md5/EFBFCB31D5BACE6BB5793A529254424E')
    print(res.content)
    print('#'*7)
    host = 'http://' + url.split('/')[2]
    id = url.split('?url=')[1]
    type = re.search('type=(.*)',id).group(1)


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
        if 'id="hdMd5"' in html:
            jiexiHdMd5(html,url)
            print(url)
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
#
# def xml2m3u8(s):
#     rgx = re.compile("\<\!\[CDATA\[(h.*?)\]\]\>")
#     m = rgx.findall(s)
#     print(m)
#     seconds = re.compile('\<seconds\>(.*?)\<')
#     s = seconds.findall(s)
#     d = dict(zip(m, s))
#
#     m3u8 = '''#EXTM3U
#     #EXT-X-VERSION:3
#     #EXT-X-TARGETDURATION:8
#     #EXT-X-MEDIA-SEQUENCE:0'''
#
#     for item in d:
#         # EXTINF:4.103,
#         itemStr = "#EXTINF:{},{}".format(d[item], item)
#         m3u8 += itemStr
#
#     print(m3u8)

@home.route('/38')
def m38():
    return  'ssssd',{'Content-Disposition': 'attachment; filename=myfilename.m3u8'}