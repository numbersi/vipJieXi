$.post("api.php",
    {
        'url': 'SgYWFf_1fw5oaa4c9bCHGahY6fRn9ppJfW/isKUvZtFmNBQm0n29cVaBxAeBvkXMmMqgwSEFqOr5TxPST82Zvx04WtjwS9Ixo6EXYQ',
        'referer': 'aHR0cDovL2FwaS54Y3E5MS50b3AvP3VybD1odHRwczovL3YueW91a3UuY29tL3Zfc2hvdy9pZF9YTXpnd016ZzRNekl6Tmc9PS5odG1s',
        'ref': form, 'time': '1536464072', 'type': '', 'other': y.base64_encode(other_l), 'key': key, 't': cip,
        'times': B, 'uuid': A, 'tip': C, 'tips': tips, 'k1': k1, 'fuck': fuck
    },
    function (data) {
        if (data.code == "200") {
            if (data.play == "lication") {
                play = {url: decodeURIComponent(lequgirl(data.url, data.utd))};
                eval("parse." + data.list + ".parser(play)")
            } else {
                if (data.play == "dplayer") {
                    parse.h5play.dplayer_play(decodeURIComponent(lequgirl(data.url, data.utd)), data.type, form)
                } else {
                    if (
                        isiPad & & data.msg == "h5") {
                        if (data.list == 'sohu') {
                            parse.setimg(data.play)
                        }
                        ;
                        $("#a1").html('<video src="' + lequgirl(data.url,
                                data.utd) + '" controls="controls"  preload="preload" poster="' + site_domaim + 'loading_wap.gif" width="100%" height="100%"></video>')
                    } else {
                        if (
                            data.type == "m3u8") {
                            var
                                flashvars = {
                                    f: "/player/ckplayer/m3u8.swf",
                                    a: lequgirl(data.url, data.utd),
                                    c: 0,
                                    s: 4,
                                    lv: data.live,
                                    p: auto,
                                    v: 100
                                }
                        } else {
                            if (data.type == "mp4") {
                                var
                                    flashvars = {f: lequgirl(data.url, data.utd), c: 0, s: 0, p: auto, v: 100, h: 3}
                            } else {
                                if (data.type == "xml") {
                                    var
                                        flashvars = {f: lequgirl(data.url, data.utd), c: 0, s: 2, p: auto, v: 100, h: 3}
                                }
                            }
                        }
                        var
                            params = {
                                bgcolor: "#FFF",
                                allowFullScreen: true,
                                allowScriptAccess: "always",
                                wmode: "transparent"
                            };
                        CKobject.embedSWF("/player/ckplayer/ckplayer.swf", "a1", "ckplayer_a1", "100%", "100%", flashvars, params)
                    }
                }
            }
            $(
                "#loading").hide();
            $("#a1").show()
        } else {
            $("#loading").hide();
            $("#a1").hide();
            $("#error").show();
            $("#error").html(
                data.msg)
        }
        ;
        if (
            data.code == '500' & & data.mode == '1') {
            $("#a1").html('<iframe frameborder=0  marginheight=0 marginwidth=0 scrolling=no src="' + (data.url + data.play) + '" width="100%" height="100%" allowfullscreen="true"></iframe>');
            $("#error").hide();
            $("#loading").hide();
            $("#a1").show()
        }
    }, "json")
}
