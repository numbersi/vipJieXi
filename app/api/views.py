# http://api.bbbbbb.me/jx/?url=https://v.youku.com/v_show/id_XMzc0Mzk5NDc0NA==.html
import re
import requests
from flask import request
from . import api
baseHost ='http://api.bbbbbb.me'
css = ''

'''
<style>
  ody,html,#a1,#ads{background-color:#000;padding:0;margin:0;width:100%;height:100%;color:transparent;} 
  body{position:relative;}
 .panel{background:#000000;background-size:90% 90%;height:26px;padding-top:10px;color:#ffffff;font-family:宋体;display:none;}
 .panel a:link{text-decoration:none;color:#ffffff;font-weight:bold;}
 .panel a:visited{text-decoration:none;color:#ffffff;font-weight:bold;}
 .panel a:hover{text-decoration:none;color:#ffffff;font-weight:bold;}
 .panel a:active{text-decoration:none;color:#ffffff;font-weight:bold;}
 .slide{margin:0;padding:0;border-top:solid 0px #000000;}
 .sigu-jiexi{display:block;position:relative;right:0px;width:90px;height:26px;padding-top:10px;font-family:宋体;font-family:arial, sans-serif;font-size:14px;color:#ffffff;background:#2C2C2C;text-decoration:none;text-align:center;-moz-border-top-left-radius:5px;-moz-border-top-right-radius:5px;border-top-left-radius:5px;border-top-right-radius:5px;-moz-border-bottom-left-radius:5px;-moz-border-bottom-right-radius:5px;border-bottom-left-radius:5px;border-bottom-right-radius:5px;}
    </style>
    </head>
    '''
@api.route('/')
def index():
    url = request.args.get("url") or "args没有参数"
    url='http://api.bbbbbb.me/jx/?url='+url
    return getHtml(url,first=True)
@api.route('/jx/index.php',methods=['POST'])
def jxIndex():
    return api('/jx/index.php', request.form.to_dict())
@api.route('/playm3u8/')
def playm3u8():
    url = request.args.get("url") or "args没有参数"
    return  getHtml('http://api.bbbbbb.me/playm3u8/?url='+url)
@api.route('/playm3u8/index.php',methods=['POST'])
def playm3u8api():
    return api('/playm3u8/index.php', request.form.to_dict())
@api.route('/jx/api.php',methods=['POST'])
def jxApi():
    return api('/yunjx/api.php', request.form.to_dict())
@api.route('/vip/api.php',methods=['POST'])
def vipApi():
    return api('/vip/api.php', request.form.to_dict())
@api.route('/vip/')
def vip():
    url = request.args.get("url") or "args没有参数"
    return getHtml(baseHost+'/vip/?url='+url)
@api.route('/jx/v.php')
def v():
    url = request.args.get("url") or "args没有参数"
    url ='http://api.bbbbbb.me/jx/v.php/?url='+url
    return getHtml(url)
# 三线
@api.route('/yunjx/')
def yunjx():
    url = request.args.get("url") or "args没有参数"
    return  getHtml('http://api.bbbbbb.me/yunjx/?url='+url)
@api.route('/yunjx/api.php',methods=['POST'])
def yunjxApi():
    return api('/yunjx/api.php', request.form.to_dict())

# yun/?url=h
@api.route('/yun/')
def yun():
    url = request.args.get("url") or "args没有参数"
    return getHtml(baseHost + '/yun/?url=' + url)
# yun/api.php
@api.route('/yun/api.php',methods=['POST'])
def yunApi():
    return api('/yun/api.php', request.form.to_dict())
def getHtml(url,first=False):
    html = requests.get(url).content.decode()
    print(html)
    if first:
        html = re.sub(r'src="/jx/v.php', 'src="/api/jx/v.php', html)
        html = re.sub(r'sigu\(\'/', 'sigu(\'/api/', html)
        html = re.sub(r'//cdn\.bbbbbb\.me/jx/css/style\.css', '/static/style1.css', html)
        html = re.sub(r'<iframe','<iframe  allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen" ',html)
    html.replace("\n", "$$$")
    html = re.sub(r'<script>if\(.*ssmuse1314.*\}{,10}</script>','',html)
    html = re.sub(r'<title>.*</title>','<title>NumberSi 解析</title>',html)
    html = re.sub(r'edc193f077b6b613964bcf4bbf0712d2','5cc256ba571f564c241888a30d1a4e9c',html)
    html = re.sub(r'//cdn\.bbbbbb\.me/yun/style\.css', '/static/style.css', html)
    html = re.sub(r'//cdn\.bbbbbb\.me.*tools\.js','/static/tools.js',html)
    html = re.sub(r'//cdn\.bbbbbb\.me.{,50}/ckplayer\.js','/static/ckplayer.js',html)
    html = re.sub(r'//cdn\.bbbbbb\.me.*jquery\.js','/static/jquery.js',html)
    html = re.sub(r'//cdn\.bbbbbb\.me.*h5\.js','/static/h5.js',html)
    html = re.sub(r'//cdn\.bbbbbb\.me.*yun\.js','/static/yun.js',html)
    html = re.sub(r'f:\'/ckplayer/m3u8.swf\'',"f:'/static/m3u8.swf'",html)
    html = re.sub(r'[\'\"]/ckplayer/ckplayer\.swf[\'\"]','"http://api.bbbbbb.me/ckplayer/ckplayer.swf"',html)
    html = re.sub(r'[\'\"]/ckplayer/ckplayer\.js[\'\"]','"http://api.bbbbbb.me//ckplayer/ckplayer.js"',html)

    html= html.replace("$$$", "\n")
    return html.encode()
def api(url,datax):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "h-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "125",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    return requests.post(baseHost+url,data=datax,headers=headers).content.decode()


