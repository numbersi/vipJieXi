import re
import requests
from bs4 import BeautifulSoup
from flask import request, render_template ,make_response

from . import home

import json
def mgtvJx(html, url):
    import os
    host = re.search("var WWW_URL='(.*)'", html).group(1) + 'baiyug.php'
    hdMd5 = re.search("'(.{32})'", eval(re.search('eval\((".*")\)', html).group(1))).group(1)
    print("8" * 99)
    print(hdMd5)
    p = os.popen('node ./app/home/s.js {}'.format(hdMd5))
    signature = p.readlines()[0]
    print(signature)
    datax = {"id": url.split('url=')[1].split('&')[0], "type": "mgtv", "siteuser": '',
             "md5": "".join(signature.split()), "hd": "", "lg": ""}
    res = requests.post(host, datax)
    data = json.loads(res.content.decode('utf-8'))
    vurl =data['url']
    return render_template('home/player.html',url=vurl)
def getUrl_Baiyug(url, Referer=''):
    host = ''
    headers = {"Referer": 'http://baidu.com'}
    if Referer:
        host = Referer.split('/')[2]
        headers = {"Referer": Referer}
    if url.startswith('//'):
        print('//')
        url = 'http:' + url
    if url.startswith('/'):
        print('/')
        print('host')
        url = 'http://' + host + url
    obj = requests.get(url,
                       # allow_redirects=False,
                       headers=headers,
                       verify=False
                       )
    html = obj.content.decode('utf-8')
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        print('have ifarme')
        return getUrl_Baiyug(iframes['src'], url)
    else:

        if 'mgtv' in url:
            return mgtvJx(html, url)
        if '<iframe' in html:
            print('have <iframe')
            res = re.search(r'<iframe name ="iframe-player" src="(.*)" width="100%"', html)
            if res:
                return getUrl_Baiyug(res.group(1), url)
@home.route('/')
def index():
    url = request.args.get("url") or ""
    if not url:
        return "<div style='width: 100%;height: 100%'><div style='margin:0 auto;'> Url=</div></div>"
    if 'mgtv' in url:
        return getUrl_Baiyug('http://yun.baiyug.cn/vip/index.php?url=' + url)
    if 'youku' in url:
        url = 'http://206dy.com/vip.php?url=' + url
        return getUrl_206dy(url)
    url = 'http://206dy.com/vip.php?url=' + url
    return getUrl_206dy(url)
@home.route('/mgtv')
def mgtv ():
    url = request.args.get("url") or "args没有参数"
    return getUrl_Baiyug('http://yun.baiyug.cn/vip/index.php?url='+url)
@home.route('/pptv')
def pptv():
    url = request.args.get("url") or "args没有参数"
    return getUrl_206dy('http://206dy.com/vip.php?url='+url)
def xml2m3u8(s):
    rgx = re.compile("\<\!\[CDATA\[(h.*?)\]\]\>")
    m = rgx.findall(s)
    print(m)
    seconds = re.compile('\<seconds\>(.*?)\<')
    s = seconds.findall(s)
    d = dict(zip(m, s))

    m3u8 = '#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:8\n#EXT-X-MEDIA-SEQUENCE:0'
    for item in d:
        # EXTINF:4.103,
        itemStr = '''#EXTINF:{},\n{}\n'''.format(d[item], item)
        m3u8 += itemStr

    return  m3u8
def pptvJx(html, url):
    import os
    res = re.search('post\("(.*).*(\{.*\})',html)
    postUrl = res.group(1)
    datax= json.loads(res.group(2))
    host = url.split('/')[0]+'//'+url.split('/')[2]
    postUrl = host+postUrl
    print(host)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "125",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Cookie": "UM_distinctid=1651eec3fa9329-03c5706e34a368-514d2f1f-1fa400-1651eec3faa800; player_forcedType=h5_VOD",
        # "Host":url.split('/')[2],
        # "Origin":host,
        # "Referer": "http://206dy.com/207/Box1.php?url=http://v.pptv.com/show/3hQBfibdNvfte3EQ.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }


    res = requests.post(host+'/207/api.php',datax,
                        headers=headers
                        ).content.decode()
    print(res)
    res = json.loads(res)
    if res['play'] == 'xml':
        xmlUrl = host + res['url']
        print(xmlUrl)
        xmlContent = requests.get(xmlUrl)
        m3u8  = xml2m3u8(xmlContent.content.decode())
        rsp = make_response(m3u8)
        rsp.headers['Content-Type'] = 'application/vnd.apple.mpegURL'
        rsp.headers['Connection'] = 'keep-alive'
        rsp.headers['Transfer-Encoding'] = 'chunked'
        rsp.headers['Access-Control-Allow-Header'] = 'X-Requested-With'
        rsp.headers['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS'
        rsp.headers['Access-Control-Allow-Origin'] = '*'

        return rsp

        # host = re.search("var WWW_URL='(.*)'", html).group(1) + 'baiyug.php'
    # hdMd5 = re.search("'(.{32})'", eval(re.search('eval\((".*")\)', html).group(1))).group(1)
    # print("8" * 99)
    # print(hdMd5)
    # p = os.popen('node ./app/home/s.js {}'.format(hdMd5))
    # signature = p.readlines()[0]
    # print(signature)
    # datax = {"id": url.split('url=')[1].split('&')[0], "type": "mgtv", "siteuser": '',
    #          "md5": "".join(signature.split()), "hd": "", "lg": ""}
    # res = requests.post(host, datax)
    # data = json.loads(res.content.decode('utf-8'))
    # vurl =data['url']
    # return render_template('home/player.html',url=vurl)
def getUrl_206dy (url,Referer=''):
    headers = { "Referer":Referer}
    if Referer:
        host = Referer.split('/')[2]
        headers = {"Referer": Referer}
    if   url.startswith('/') :
        if url.startswith('//'):
            url ='http:'+ url
        else:
            url = 'http://'+host + url
    obj = requests.get(url,
                       # allow_redirects=False,
                       headers =headers)
    html = obj.content.decode()
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        print( 'have ifarme')
        return getUrl_206dy( iframes['src'],url)
    else:
        if '<iframe' in html:
            print( 'have <iframe')
            res = re.search(r'<iframe name ="iframe-player" src="(.*)" width="100%"', html)
            if res:
                return getUrl_206dy(res.group(1),url)
        print('no ifarme')
        return jxHtml(html,url)

@home.route('/parse.php',methods=['GET', 'POST'])
def parse():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "125",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "UM_distinctid=1651eec3fa9329-03c5706e34a368-514d2f1f-1fa400-1651eec3faa800; player_forcedType=h5_VOD",
        "Host": "le.206dy.com",
        "Origin": "https://le.206dy.com",
        # "Referer": "https://le.206dy.com/Box.php?url=http://www.iqiyi.com/v_",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    print(request.args.to_dict())
    datax = request.args.to_dict()
    domain = datax.pop('domain')
    print('*'*199)
    print(datax)
    print(domain)
    str =domain+'/parse.php?'
    for item in datax:
        str= str+item+'='+datax[item]+"&"
    res  = requests.get(str,
                        # allow_redirects=False,
                        verify=False,
                        # headers=headers
                        )
    return  res.content.decode('utf-8')
@home.route('/api.php',methods=['POST'])
def api():
    datax = request.form.to_dict()

    host = datax.pop('host')
    print(host)
    print(datax)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "125",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Cookie": "UM_distinctid=1651eec3fa9329-03c5706e34a368-514d2f1f-1fa400-1651eec3faa800; player_forcedType=h5_VOD",
        # "Host": '206dy.com',
        # "Origin": 'https://206dy.com',
        # "Referer": "https://206dy.com/207/Box1.php?url=http://v.pptv.com/show/3hQBfibdNvfte3EQ.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }


    res = requests.post(host,datax,headers=headers)
    print(res.content)

    return res.content
@home.route('/207/api.php',methods=['POST'])
def api207():
    datax = request.form.to_dict()

    host = datax.pop('host')
    print(host)
    print(datax)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "125",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Cookie": "UM_distinctid=1651eec3fa9329-03c5706e34a368-514d2f1f-1fa400-1651eec3faa800; player_forcedType=h5_VOD",
        # "Host": '206dy.com',
        # "Origin": 'https://206dy.com',
        # "Referer": "https://206dy.com/207/Box1.php?url=http://v.pptv.com/show/3hQBfibdNvfte3EQ.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }


    res = requests.post(host,datax,headers=headers)
    return res.content
def jxHtml(html,url):
    host = '//'.join([url.split('/')[0], url.split('/')[2]])

    if 'kplayer.js' in html:
        # res = re.search(r'<script type="text/javascript" src="(.*)ckplayer/ckplayer.js" charset="utf-8">', html).group(1)
        # host ='http://' + res.split('/')[2]
        html = re.sub(r'src="', 'src="'+host+'/', html)
        html = re.sub(r'href="', 'href="'+host+'/', html)
    if 'DPlayer.min.js' in html:
        cndJs = {
                 'https://le.206dy.com/ckplayer/ckplay.js':'/ckplayer/ckplay.js',
                 'https://le.206dy.com/load.gif':'/load.gif',
                 'https://le.206dy.com/ckplayer/ckplayer.swf':'/ckplayer/ckplayer.swf',
                 'https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.js': '/ckplayer/DPlayer.min.js',
                 'https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.css': '/ckplayer/DPlayer.min.css',
                 'https://cdn.bootcss.com/hls.js/0.9.1/hls.min.js': '/ckplayer/hls.min.js',
                 'https://cdn.bootcss.com/flv.js/1.4.2/flv.min.js': '/ckplayer/flv.min.js'
                 }
        for key in cndJs:
            html = html.replace(cndJs[key], key)
    postUrl = re.search('post\("(.*php)",',html).group(1)
    reStr = ' host :"{}" ,"key"'.format(host+postUrl)
    html = re.sub(r'"key"', reStr, html)
    res = re.search(r'<!DOCTYPE html>.*</html>', html.replace("\n", "$$$")).group()
    html=   res.replace("$$$", "\n")
    html = re.sub(r"{url:url,tm:tm,vuid:vuid,key:key}", "{url:url,tm:tm,vuid:vuid,key:key,domain:domain}", html)
    # print(html)
    return  html