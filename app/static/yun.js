var cip,vodurl,get;
var adtime = pid = h5fd = 0;
function error() {
	if (yun.isiPad) {
		if ($('video')[0].error != null && typeof($('video')[0].error.code) != undefined && $('video')[0].error.code == 4) {
			play_up();
		}
		if(h5fd==1){
			var jicount = vodurl.length-1;
			if(jicount > pid && $('video')[0].ended){
				pid++;
				$('video').attr('src',vodurl[pid]['purl']);
				$('video')[0].play();
			}
		}
	} else {
		CKobject.getObjectById('ckplayer_a1').addListener('error', 'play_up');
	}
}
function get_msg(msg) {
	$('#loading').hide();
	$('#a1').hide();
	$('#error').html(msg).show();
}
function playad() {
	if (yun.ads) {
		yun.play = 1;
		if (yun.isiPad) {
			yun.play = 0;
		}
		$('#loading').hide();
		var ads = yun.ads.split('|');
		var adhtml = '<a href="' + ads[1] + '" target="_blank"><img src="' + ads[0] + '"></a><span>广告<b>' + ads[2] + '</b>秒后关闭</span>';
		$('#ads').html(adhtml).show();
		var img = new Image();
		img.src = ads[0];
		img.onload = function() {
			var w = $('#ads').width();
			if (img.width > w) {
				$('#ads img').css('width', w);
				$('#ads img').css('left', 0);
				var h = $('#ads img').height();
				$('#ads img').css('margin-top', '-' + h / 2 + 'px');
			} else {
				$('#ads img').css('margin-left', '-' + parseInt(img.width) / 2 + 'px');
				$('#ads img').css('margin-top', '-' + parseInt(img.height) / 2 + 'px');
			}
		};
		adtime = ads[2];
		var adds = setInterval(function() {
			adtime--;
			if (adtime < 1) {
				if (yun.isiPad) {
					$('video')[playerNum].play();
				}
				$('#ads').hide();
				$('#a1').show();
				clearInterval(adds);
			} else {
				$('#ads b').html(adtime);
				$('#ads').show();
				$('#a1').hide();
			}
		}, 1000);
	}
}
function player(up) {
	if (up == 0) {
		playad();
	}
	$.post("api.php", {
		"url": yun.url,
		"up": up,
		"ip": cip
	}, function(data) {
		if (data['msg'] == 'ok' && data['url']) {
			if (data['ext'] == 'post') {
				posts(data['url']);
			} else if (data['ext'] == 'ajax') {
				var ajaxurl = data['url'];
				eval('get_'+data['type']+'(ajaxurl);');
			} else {
				vod_player(data);
			}
		} else {
			vod_err(data['msg']);
		}
	}, "json");
}
function play_up() {
	yun.errid++;
	if (yun.errid < 3) {
		player(1);
	} else {
		get_msg('播放视频异常，请稍候重再试~！');
	}
}
function posts(url) {
	$.getJSON(url + "&callback=?", function(json) {
		if(json){
			$.post("api.php", {
				"url": yun.url,
				"up": yun.update,
				"data": json
			}, function(data) {
				if (data['msg'] == 'ok' && data['url']){
					vod_player(data);
				} else {
					vod_err(data['msg']);
				}
			});
		} else {
			vod_err('');
		}
	});
}
function vod_player(data) {
	var autoplay = yun.play == 1 ? 'autoplay="autoplay"' : '';
	if (data['ext'] == 'link') {
		$('#a1').html('<iframe width="100%" height="100%" allowTransparency="true" frameborder="0" scrolling="no" src="' + data['url'] + '"></iframe>');
	} else if (data['ext'] == 'h5_fd') {
		h5fd = 1;
		vodurl = data['url'];
		$('#a1').html('<video src="'+vodurl[0]['purl']+'" controls="controls" autoplay="autoplay" width="100%" height="100%"></video>');
		yun.isiPad = true;
		setInterval('error()', 1000);
	} else if (yun.isiPad) {
		$('#a1').html('<video src="'+data['url']+'" controls="controls" autoplay="autoplay" width="100%" height="100%"></video>');
		yun.isiPad = true;
		setInterval('error()', 1000);
	} else if (data['ext'] == 'h5') {
		if(!window.applicationCache){
			get_msg('您的浏览器不支持HTML5，请跟换浏览器重试~！');
		}
		var player = new KTPlayer({src:data['url'],play:yun.play,root:document.getElementById('a1')});
		player.init();
		yun.isiPad = true;
		setInterval('error()', 1000);
	} else {
		if (data['ext'] == 'm3u8' || data['ext'] == 'm3u8_list') {
			var m3u8swf = data.hasOwnProperty('m3u8swf') ? data['m3u8swf'] : yun.webpath + 'ckplayer/m3u8.swf';
			var flashvars = {
				f: m3u8swf,
				a: data['url'],
				c: 0,
				s: 4,
				lv: 0,
				p: 1,
				v: 100,
				loaded: 'error'
			}
		} else if (data['ext'] == 'mp4') {
			var flashvars = {
				f: data['url'],
				c: 0,
				s: 0,
				p: yun.play,
				v: 100,
				h: 3,
				loaded: 'error'
			};
		} else if (data['ext'] == 'xml') {
			var flashvars = {
				f: data['url'],
				c: 0,
				s: 2,
				p: yun.play,
				v: 100,
				h: 3,
				loaded: 'error'
			};
		}
		var params = {
			bgcolor: '#FFF',
			allowFullScreen: true,
			allowScriptAccess: 'always',
			wmode: 'transparent'
		};
		CKobject.embedSWF(yun.webpath + 'ckplayer/ckplayer.swf', 'a1', 'ckplayer_a1', '100%', '100%', flashvars, params);
	}
	$('#loading').hide();
	$('#a1').show();
}
function vod_err(msg) {
	if (msg == null) {
		get_msg('获取视频地址异常，请刷新重试~！');
	} else {
		get_msg(msg);
	}
}
function get_play(up) {
        player(up);
/*
	$.get("https://data.video.iqiyi.com/v.f4v", function(cdnip) {
		var sip = cdnip.match(/http:\/\/([^\"]*)\/v.f4v/);
		cip = sip[1];
		player(up);
	});
*/
}
function get_qiyis(url) {
	 $.ajax({
		url: url.replace('http:', ''),
		dataType: 'jsonp',
		jsonpCallback: "callbackfunction",
		success: function(json) {
			if (json.code == 'A00110') {
				play_up();
			} else if (json.code == 'A00000') {
				var data = new Array();
				if (yun.isiPad) {
					data['url'] = json.data.m3u;
					data['ext'] = 'h5';
					vod_player(data);
				} else {
					var array = {};
					for (var i = json.data.vidl.length - 1; i >= 0; i--) {
						if (json.data.vidl[i].fileFormat != "H265") {
							array[json.data.vidl[i].vd] = json.data.vidl[i];
						}
					};
					if (array[4] != undefined) {
						data['url'] = array[4].m3u;
					} else if (array[3] != undefined) {
						data['url'] = array[3].m3u;
					} else if (array[2] != undefined) {
						data['url'] = array[2].m3u;
					} else if (array[1] != undefined) {
						data['url'] = array[1].m3u;
					} else if (array[96] != undefined) {
						data['url'] = array[96].m3u;
					}
					data['url'] = yun.webpath+'yun/key.php?m3u8='+encodeURIComponent(encodeURIComponent(data['url']+'&yunkey='+yun.url));
					data['ext'] = 'm3u8';
					vod_player(data);
				}
			} else {
				vod_err(null);
			}
		}
	});
}
function get_qq(url) {
	var get = getQuery(url);
	$.ajax({
		url: "//h5vv.video.qq.com/getinfo?charge=0&vid=" + get.vid + "&defaultfmt=auto&otype=json&guid=" + get.guid + "&platform=" + get.platform + "&defnpayver=1&appVer=3.0.83&sdtfrom=" + get.sdtfrom + "&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fnuijxf6k13t6z9b%2Fl0023olk3g4.html&_0=" + get._0 + "&defn=mp4&fhdswitch=0&show1080p=1&isHLS=0&newplatform=" + get.sdtfrom + "&defsrc=1&_1=" + get._1 + "&_2=" + get._2,
		dataType: 'jsonp',
		jsonpCallback: "txplayerJsonpCallBack_getkey_" + parseInt(Math.random() * 800000 + 80000),
		success: function(getinfo) {
			if (!getinfo.exem) {
				$.ajax({
					url: url + '&filename=' + getinfo.vl.vi[0].lnk + '.mp4',
					dataType: 'jsonp',
					jsonpCallback: "txplayerJsonpCallBack_getkey_" + parseInt(Math.random() * 800000 + 80000),
					success: function(json) {
						var data = new Array();
						data['ext'] = 'h5';
						data['url'] = getinfo.vl.vi[0].ul.ui[0].url + json.filename + '?sdtfrom=' + get.sdtfrom + '&guid=' + get.guid + '&vkey=' + json.key;
						vod_player(data);
					}
				})
			} else {
				vod_err(null);
			}
		}
	});
}
function get_youku(url) {
	get = getQuery(url);
	var data = new Array();
	if (yun.isiPad) {
		weParserParams = {'vid':get.vid,'ccode':get.code,'site':'youku','hd':get.hd};
		var weParserJS = document.createElement("script");
		weParserJS.type = "text/javascript";
		weParserJS.src = get.js;
		document.getElementsByTagName("head")[0].appendChild(weParserJS);
	} else {
		var aurl = 'hd='+get.hd+'&vid='+get.vid+'&code='+get.code+'&swf='+get.swf+'&site=youku&yunkey='+yun.url;
		data['url'] = yun.webpath+'yun/key.php?xml='+encodeURIComponent(encodeURIComponent(aurl));
		data['ext'] = 'xml';
		vod_player(data);
	}
}
function get_letv(url) {
	$.getJSON(url.replace('http:', '')+"&jsonp=?",function(json) {
		if (json.status == '200') {
			var data = new Array();
			var vod = json.nodelist;
			for(var i=0;i<vod.length;i++){
				if(vod[i]['location'].indexOf(':110/') < 0){
					data['url'] = vod[i]['location'];
					break;
				}
			}
			if (yun.isiPad) {
				data['ext'] = 'h5';
			} else {
				data['url'] = encodeURIComponent(data['url']);
				data['ext'] = 'm3u8';
			}
			vod_player(data);
		} else {
			vod_err(null);
		}
	});
}
function getQuery(url) {
    if (typeof url !== 'string')  return null;
    var query = url.match(/[^\?]+\?([^#]*)/, '$1');
    if (!query || !query[1])  return null;
    var kv = query[1].split('&');
    var map = {};
    for (var i = 0, len = kv.length; i < len; i++) {
        var result = kv[i].split('=');
        var key = result[0],
            value = result[1];
        map[key] = value || (typeof value == 'string' ? null : true);
    }
    return map;
}

var YunJS = document.createElement("script");
YunJS.type = "text/javascript";
YunJS.src = "";
document.getElementsByTagName("head")[0].appendChild(YunJS);