import re
import requests
from bs4 import BeautifulSoup
from flask import request, render_template, make_response, current_app
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
    vurl = data['url']
    return render_template('home/player.html', url=vurl)


def getUrl_Baiyug(url, Referer=''):
    host = ''
    headers = {"Referer": 'http://baidu.com'}
    if Referer:
        host = Referer.split('/')[2]
        headers = {"Referer": Referer}
    if url.startswith('//'):
        url = 'http:' + url
    if url.startswith('/'):
        url = 'http://' + host + url
    if url.startswith('./'):
        url= 'http://yun.baiyug.cn/vip'+url[1:]
    obj = requests.get(url,
                       headers=headers,
                       verify=False
                       )
    html = obj.content.decode('utf-8')
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        print('have ifarme')
        print(iframes)

        return getUrl_Baiyug(iframes['src'], url)
    else:
        print('no ifarme')
        if '<iframe' in html:
            print('have <iframe')
            res = re.search(r'<iframe name ="iframe-player" src="(.*)" width="100%"', html)
            if res:
                print('have iframe-player')
                return getUrl_Baiyug(res.group(1), url)
        return jxHtml(html, url)

@home.route('/')
def index():
    url = request.args.get("url") or ""
    if not url:
        return  'url = null'
    url = url.split('?')[0]
    data = {'1线': '/dy?url={}'.format(url), '2线': '/yun?url={}'.format(url)}
    if '27pan' in url:
        data = {'1线': '/dy?url={}'.format(url), '2线': '/yun?url={}'.format(url)}
    return render_template('home/index.html', data=data)


@home.route('/dy')
def dy206():
    url = request.args.get("url") or ""
    url = 'http://206dy.com/vip.php?url=' + url
    return getUrl_206dy(url)


@home.route('/yun')
def ayun():
    url = request.args.get("url") or ""
    url = 'http://yun.baiyug.cn/vip/index.php?url=' + url
    return getUrl_Baiyug(url)


@home.route('/mgtv')
def mgtv():
    url = request.args.get("url") or "args没有参数"
    return getUrl_Baiyug('http://yun.baiyug.cn/vip/index.php?url=' + url)


@home.route('/pptv')
def pptv():
    url = request.args.get("url") or "args没有参数"
    return getUrl_206dy('http://206dy.com/vip.php?url=' + url)


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

    return m3u8


def pptvJx(html, url):
    import os
    res = re.search('post\("(.*).*(\{.*\})', html)
    postUrl = res.group(1)
    datax = json.loads(res.group(2))
    host = url.split('/')[0] + '//' + url.split('/')[2]
    postUrl = host + postUrl
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

    res = requests.post(host + '/207/api.php', datax,
                        headers=headers
                        ).content.decode()
    print(res)
    res = json.loads(res)
    if res['play'] == 'xml':
        xmlUrl = host + res['url']
        print(xmlUrl)
        xmlContent = requests.get(xmlUrl)
        m3u8 = xml2m3u8(xmlContent.content.decode())
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


def getUrl_206dy(url, Referer='http://www.baidu.com'):
    headers = {"Referer": Referer}
    if Referer:
        host = Referer.split('/')[2]
        headers = {"Referer": Referer}
    if url.startswith('/'):
        if url.startswith('//'):
            url = 'http:' + url
        else:
            url = 'http://' + host + url
    obj = requests.get(url,
                       # allow_redirects=False,
                       headers=headers,
                       verify=False
                       )
    html = obj.content.decode()
    htmlObj = BeautifulSoup(html, 'lxml')
    iframes = htmlObj.find('iframe')
    if iframes:
        print('have ifarme')
        return getUrl_206dy(iframes['src'], url)
    else:
        if '<iframe' in html:
            print('have <iframe')
            res = re.search(r'<iframe name ="iframe-player" src="(.*)" width="100%"', html)
            if res:
                return getUrl_206dy(res.group(1), url)
        print('no ifarme')

        return jxHtml(html, url)


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

    datax = request.args.to_dict()
    domain = datax.pop('domain')

    str = domain + '/parse.php?'
    for item in datax:
        str = str + item + '=' + datax[item] + "&"
    res = requests.get(str,
                       # allow_redirects=False,
                       verify=False,
                       # headers=headers
                       )
    return res.content.decode('utf-8')


@home.route('/api.php', methods=['POST'])
def api():
    datax = request.form.to_dict()
    if 'host' in datax:
        host = datax.pop('host')

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "h-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "125",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'referer': 'https://le.206dy.com/Box.php?url=https://www.iqiyi.com/v_19rr2akbkk.html',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            'Cookie': 's'
        }

        res = requests.post(host, datax, headers=headers)
        return res.content
    else:

        params = request.form.to_dict()
        url = 'http://vip.xcq91.top/player/api.php'
        res1 = requests.post(url, data=params,
                             headers={'Host': 'vip.xcq91.top', 'Connection': 'keep-alive', 'Content-Length': '604',
                                      'Accept': 'application/json, text/javascript, */*; q=0.01',
                                      'Origin': 'http://vip.xcq91.top', 'X-Requested-With': 'XMLHttpRequest',
                                      'User-Agent': request.headers['User-Agent'],
                                      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                      'Accept-Encoding': 'gzip, deflate',
                                      'Accept-Language': 'zh-CN,zh;q=0.9'})

        html = res1.content.decode()


        return html


@home.route('/<U>/api.php', methods=['POST'])
def api207(U):
    datax = request.form.to_dict()

    # host = datax.pop('host')+'/api/{}/api.php'.format(U)
    host ='https://le.206dy.com/api/api/api.php'
    headerss= {'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-encoding': 'gzip, deflate, br',
     'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache', 'content-length': '145',
     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
     'Cookie': 'UM_distinctid=1651eec3fa9329-03c5706e34a368-514d2f1f-1fa400-1651eec3faa800',
     'origin': 'https://le.206dy.com',
    'pragma': 'no-cache',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
     'x-requested-with': 'XMLHttpRequest'}
    print(datax)
    print(host)
    res = requests.post(host,datax, headers=headerss)
    print(res.content)
    return res.content
def jxHtml(html, url):
    if 'index.m3u8' in url:
        return render_template('home/QQkandian.html', url=url.split('url=')[1].split('&')[0])
    host = '//'.join([url.split('/')[0], url.split('/')[2]])
    if 'QQ看点视频' in html:
        url = re.search(r'(http.*qq\.com.*tm=.{32})',html).group()
        print(url)
        return render_template('home/QQkandian.html', url=url)
    if '27pan' in html:
        return '''<iframe id="sigu" scrolling="no" allowtransparency="true" frameborder="0" src="{}" width="100%" height="100%" allowfullscreen="true"></iframe>'''.format(
            url)
    return html

    print(html)
    #
    # if 'baiyug.' in url:
    #     print(html)
    #     res = re.search(r'<script type="text/javascript" src="(.*)ckplayer/ckplayer.js" charset="utf-8">', html).group(
    #         1)
    #     host = res
    #     html = re.sub(r'src="baiyug', 'src="' + res + '/baiyug', html)
    #     html = re.sub(r'href="baiyug', 'href="' + res + '/baiyug', html)
    # else:
    #     html = re.sub(r'src="s', 'src="' + host + "/s", html)
    #     html = re.sub(r'src="p', 'src="' + host + "/p", html)
    #     html = re.sub(r'href="s', 'href="' + host + "/s", html)
    #     html = re.sub(r'href="p', 'href="' + host + "/p", html)


    reStr1 = ' host :"{}" ,"key"'.format(host )
    reStr2 = ' host :"{}" ,"md5"'.format(host)
    html = re.sub(r'"md5"', reStr2, html)
    html = re.sub(r'"key"', reStr1, html)
    res = re.search(r'<!DOCTYPE html>.*</html>', html.replace("\n", "$$$")).group()
    html = res.replace("$$$", "\n")
    html = re.sub(r'https://hm\.baidu\.com/hm\.js\?[0-9a-zA_Z][32]',
                  'https://hm.baidu.com/hm.js?5cc256ba571f564c241888a30d1a4e9c', html)
    html = re.sub(r"{url:url,tm:tm,vuid:vuid,key:key}", "{url:url,tm:tm,vuid:vuid,key:key,domain:domain}", html)
    html = re.sub(r'<title>.*</title>', '<title>NumberSi 解析</title>', html)

    return html


@home.route('/baiyug.php', methods=['POST'])
def baiyug():
    datax = request.form.to_dict()
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "125",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "X-Requested-With": "XMLHttpRequest",
        'Cookie': 's'
    }
    host = datax['host']

    res = requests.post(host + '/baiyug.php', datax, headers=headers)
    print(res.content)
    return res.content


@home.route('/video/qiyi2.php')
def videoQiyi():
    url = request.args.get("url") or ""
    return requests.get('http://api.jxegc.com/video/qiyi2.php?url=' + url).content

@home.route('/xcq')
def xcq():
    url = request.args.get("url") or ""
    urlc = 'http://api.xcq91.top/?url=' + url

    js = '''
      <script type="text/javascript">  
      
      　window.onload = function(){ 
         var first  = document.getElementById("first");
         var first  = document.getElementById("first");
         if (first.attachEvent) {    
            first.attachEvent("onload", function() {    
                //iframe加载完成后你需要进行的操作  
                alert('完成')
            });    
        } else {    
            first.onload = function() {    
                      //iframe加载完成后你需要进行的操作  
                                      alert('完成')

            };    
        } 
        }
        </script>
    '''
    h = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <iframe id="first"  hidden src="{}"></iframe>
    <iframe id="video" src=""></iframe>
</body>
{}
</html>
    '''.format(urlc,js)
    return h
    return  '<body><ifarme   id="1"src="'+urlc+'"></ifarme>'+'<ifarme   id="2"src="/xcq91?url='+url+'" width="100%" height="100%" align="middle" hspace="0" vspace="0" allowfullscreen="true" marginheight="0" marginwidth="0"></ifarme></body>'
@home.route('/xcq91')
def xcq91():
    url = request.args.get("url") or ""
    url = 'http://api.xcq91.top/?url=' + url
    headersStr = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Host: api.xcq91.top
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: {}'''.format(request.headers['User-Agent'])
    headers = {}
    for item in headersStr.split('\n'):
        c = item.split(': ')
        headers.update({c[0]: c[1]})
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        html = res.content.decode()
        obj = BeautifulSoup(html, 'lxml')
        VipHeadersStr = '''Host: vip.xcq91.top
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: {}
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: {}
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9'''.format(request.headers['User-Agent'], url)
        headers = {}
        for item in VipHeadersStr.split('\n'):
            c = item.split(': ')
            headers.update({c[0]: c[1]})
        if obj.iframe:
            url1 = obj.iframe['src']
            print(url1)
            html1 = requests.get(url1, headers=headers).content.decode()
            print(html1)
            # str = '"http://vip.xcq91.top/player/api.php" , "jsonp"'
            # html1 = re.sub('"api.php"', str, html1)
            # html1 = re.sub('"json"\)', '"jsonp")', html1)
            return html1
    return '1'





@home.route("/<re(r'.*'):file_name>")
def get_file(file_name):
    ''''''
    print(file_name)
    file_name = file_name.split('/')[-1]
    return current_app.send_static_file(file_name)
@home.route('/tt')
def tt():
    url = 'https://v.tt-hk.cn/jx.php?url=http://v.youku.com/v_show/id_XMzgzNzEyNDg5Mg==.html'
    headersStr = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
pragma: no-cache
referer: http://api.bbbbbb.me/yunjx/?url=http://v.youku.com/v_show/id_XMzgzNzEyNDg5Mg==.html
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'''
    headers = {}
    for item in headersStr.split('\n'):
        c = item.split(': ')
        headers.update({c[0]: c[1]})
    html = requests.get(url, headers=headers).content
    return  html