import json
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
from . import home
def jxHtml(html, url):
    host = '//'.join([url.split('/')[0], url.split('/')[2]])
    if 'kplayer.js' in html:
        res = re.search(r'<script type="text/javascript" src="(.*)ckplayer/ckplayer.js" charset="utf-8">', html).group(
            1)
        host = 'http://' + res.split('/')[2]
        html = re.sub(r'src="baiyug', 'src="' + res + 'baiyug', html)
        html = re.sub(r'href="baiyug', 'href="' + res + 'baiyug', html)
    if 'DPlayer.min.js' in html:
        cndJs = {
            'https://le.206dy.com/ckplayer/ckplay.js': '/ckplayer/ckplay.js',
            'https://le.206dy.com/load.gif': '/load.gif',
            'https://le.206dy.com/ckplayer/ckplayer.swf': '/ckplayer/ckplayer.swf',
            'https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.js': '/ckplayer/DPlayer.min.js',
            'https://cdn.bootcss.com/dplayer/1.22.2/DPlayer.min.css': '/ckplayer/DPlayer.min.css',
            'https://cdn.bootcss.com/hls.js/0.9.1/hls.min.js': '/ckplayer/hls.min.js',
            'https://cdn.bootcss.com/flv.js/1.4.2/flv.min.js': '/ckplayer/flv.min.js'
        }

        for key in cndJs:
            html = html.replace(cndJs[key], key)
    reStr = ' host :"{}" ,"key"'.format(host)
    html = re.sub(r'"key"', reStr, html)
    res = re.search(r'<!DOCTYPE html>.*</html>', html.replace("\n", "$$$")).group()
    html = res.replace("$$$", "\n")

    return html
def pan27(html, url):
    host = url.split('/')[0] + '//' + url.split('/')[2]
    print(host)
    main = re.search(r'main.*"/(.*\.m3u8)"', html).group(1)
    data = {}
    data['url']  = host+ main
    return  url
    return render_template('home/player.html',data=data)

def getUrl_Baiyug(url, Referer=''):
    print("*" * 99)
    print(url)
    print("*" * 99)

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
    print(url)
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
        if '<iframe' in html:
            print('have <iframe')
            res = re.search(r'<iframe name ="iframe-player" src="(.*)" width="100%"', html)
            if res:
                return getUrl_Baiyug(res.group(1), url)
            return jxHtml(html, url)
        print('no ifarme')
        print(html)
        return url
        if not html:
            print('no html')
        print(url)
        if "27pan" in html:
            return pan27(html, url)
        return url
        host = 'http://' + url.split('/')[2] + '/'
        html = re.sub(r'src="', 'src="' + host, html)
        html = re.sub(r'href="', 'href="' + host, html)

        html = re.sub(r"{url:url,tm:tm,vuid:vuid,key:key}", "{url:url,tm:tm,vuid:vuid,key:key,domain:domain}", html)
        return html


from flask import Flask, request, render_template

app = Flask(__name__)


@home.route('/')
def index():
    url = request.args.get("url") or "args没有参数"
    url = 'http://206dy.com/vip.php?url=' + url

    res = getUrl_Baiyug(url)
    if re.match(r'^https?:/{2}\w.+$', res):
        return '<iframe src="{}" frameborder="0" scrolling="no" style="width:100%;height:100%;" ></iframe>'.format(res)
    return res


@home.route('/api.php', methods=['GET', 'POST'])
def api():
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

    datax = request.form.to_dict()
    host = datax.pop('host')
    print(host)
    print(datax)
    res = requests.post(host + '/api.php', datax, headers=headers)
    print(res.content)

    return res.content


@home.route('/parse.php', methods=['GET', 'POST'])
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
    print('*' * 199)
    print(datax)
    print(domain)
    str = domain + '/parse.php?'
    for item in datax:
        str = str + item + '=' + datax[item] + "&"
    print(str)
    res = requests.get(str,
                       # allow_redirects=False,
                       verify=False,
                       # headers=headers
                       )
    return res.content.decode('utf-8')


if __name__ == '__main__':
    # 优酷
    # url = 'http://206dy.com/vip.php?url=https://v.youku.com/v_show/id_XMzc3MjA4MzkwNA==.html?spm=a2hww.11359951.m_26657.5~1~3~A'

    # QQ
    # url = 'http://206dy.com/vip.php?url=https://v.qq.com/x/cover/tyyx4oj6ejkooa0.html'
    # getUrl_Baiyug(url)
    app.run(debug=True)

