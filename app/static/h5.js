/* ktPlayer by Scott */
!
function(a, b) {
	function c(a) {
		this.options = a, this.root = a.root || b.body, this.target = null
	}
	var d, e, f, g, h = {
		play: "M153.6 75.794916C153.6 19.283822 190.753317-0.345061 237.362821 32.501243L819.04468 442.419778C865.30561 475.020437 865.140746 527.555686 818.320241 560.007424L238.087264 962.172457C191.426236 994.513664 153.6 974.380703 153.6 918.409001L153.6 75.794916Z",
		pause: "M153.6 98.185425C153.6 43.959112 196.985769 0 251.345455 0 305.328778 0 349.090909 44 349.090909 98.185425L349.090909 925.814574C349.090909 980.040888 305.70514 1024 251.345455 1024 197.362131 1024 153.6 980 153.6 925.814574L153.6 98.185425ZM674.909092 98.185425C674.909092 43.959112 718.294861 0 772.654546 0 826.63787 0 870.4 44 870.4 98.185425L870.4 925.814574C870.4 980.040888 827.014231 1024 772.654546 1024 718.671222 1024 674.909092 980 674.909092 925.814574L674.909092 98.185425Z",
		volume_small: "M768 512c0 109.568-47.104 188.0064-141.312 235.52L626.688 276.48C720.896 323.9936 768 402.432 768 512L768 512 768 512zM0 439.0912c0-56.5248 45.8752-102.4 102.8096-102.4l123.904 0L512 43.8272l0 936.3456-285.2864-292.864L102.8096 687.3088c-56.7296 0-102.8096-45.8752-102.8096-102.4L0 439.0912 0 439.0912zM0 439.0912",
		volume_big: "M626.666665 0C742.222848 25.554484 837.332992 86.245551 912 182.074779 986.667008 277.904181 1024 387.878146 1024 512 1024 636.121856 986.667008 746.095821 912 841.925222 837.332992 937.754486 742.222848 998.445496 626.666665 1024L626.666665 903.529411C710.222679 877.974912 778.221911 829.604628 830.666752 758.417111 883.111424 687.229594 909.333335 605.091436 909.333335 512 909.333335 418.908565 883.111424 336.770404 830.666752 265.582888 778.221911 194.395372 710.222679 146.025072 626.666665 120.470588L626.666665 0ZM768 512C768 621.519242 720.889344 700.00684 626.666665 747.465242L626.666665 276.534759C720.889344 323.993162 768 402.480758 768 512L768 512ZM0 439.079676C0 382.575632 45.869382 336.770054 102.722168 336.770054L226.666666 336.770054 512 43.807487 512 980.192512 226.666666 687.229947 102.722168 687.229947C45.990281 687.229947 0 641.413437 0 584.920325L0 439.079676Z",
		mute: "M626.688 742.6048l0 4.9152c1.024-0.6144 2.2528-1.2288 3.2768-1.6384L626.688 742.6048zM745.0624 629.1456c15.36-33.9968 22.9376-73.1136 22.9376-117.1456 0-109.568-47.104-188.0064-141.312-235.52l0 234.2912L745.0624 629.1456zM830.6688 265.6256C883.0976 336.6912 909.312 418.816 909.312 512c0 81.92-20.2752 155.4432-61.0304 220.3648l83.1488 83.1488C993.0752 726.016 1024 624.8448 1024 512c0-124.1088-37.2736-234.0864-112.0256-329.9328C837.4272 86.2208 742.1952 25.6 626.688 0l0 120.4224C710.2464 146.0224 778.24 194.3552 830.6688 265.6256zM220.9792 336.6912 102.8096 336.6912c-56.9344 0-102.8096 45.8752-102.8096 102.4l0 145.8176c0 56.5248 46.08 102.4 102.8096 102.4l123.904 0 285.2864 292.864 0-352.256L220.9792 336.6912zM512 396.0832 512 43.8272 338.1248 222.208ZM735.6416 851.3536c-32.768 22.528-69.0176 39.936-108.9536 52.0192L626.688 1024c72.0896-15.9744 136.3968-45.6704 192.512-88.8832L735.6416 851.3536zM5.143757 77.55776l72.40704-72.40704 941.29152 941.29152-72.40704 72.40704-941.29152-941.29152Z",
		full_on: "M324.266667 406.755556 68.266667 406.755556 68.266667 338.488889 250.311111 338.488889 250.311111 150.755556 324.266667 150.755556ZM318.577778 617.244444 318.577778 873.244444 247.466667 873.244444 247.466667 691.2 59.733333 691.2 59.733333 617.244444ZM708.266667 617.244444 961.422222 617.244444 961.422222 685.511111 779.377778 685.511111 779.377778 873.244444 708.266667 873.244444ZM705.422222 409.6 705.422222 153.6 776.533333 153.6 776.533333 335.644444 964.266667 335.644444 964.266667 409.6Z",
		full_off: "M65.422222 145.066667 321.422222 145.066667 321.422222 216.177778 139.377778 216.177778 139.377778 401.066667 65.422222 401.066667ZM59.733333 867.555556 59.733333 611.555556 128 611.555556 128 793.6 315.733333 793.6 315.733333 867.555556ZM958.577778 867.555556 705.422222 867.555556 705.422222 796.444444 887.466667 796.444444 887.466667 608.711111 958.577778 608.711111ZM961.422222 147.911111 961.422222 403.911111 890.311111 403.911111 890.311111 221.866667 702.577778 221.866667 702.577778 147.911111Z"
	},
		i = {
			timeFormat: function(a) {
				var b = parseInt(a / 60),
					c = parseInt(a % 60),
					d = b < 10 ? "0" + b : b,
					e = c < 10 ? "0" + c : c;
				return d + ":" + e
			},
			leftDistance: function(a) {
				var c = a.offsetLeft;
				if (b.fullscreenElement || b.mozFullScreenElement || b.webkitFullscreenElement || b.msFullscreenElement) for (; a.offsetParent && a.offsetParent !== d.target;) a = a.offsetParent, c += a.offsetLeft;
				else for (; a.offsetParent;) a = a.offsetParent, c += a.offsetLeft;
				return c
			},
			topDistance: function(a) {
				var c = a.offsetTop;
				if (b.fullscreenElement || b.mozFullScreenElement || b.webkitFullscreenElement || b.msFullscreenElement) for (; a.offsetParent && a.offsetParent !== d.target;) a = a.offsetParent, c += a.offsetTop;
				else for (; a.offsetParent;) a = a.offsetParent, c += a.offsetTop;
				return c
			}
		};
	c.prototype = {
		init: function() {
			if ("object" != typeof this.options || !this.options.src) return void console.error("璇锋纭厤缃璞★紒");
			if(this.options.play==1){
				play = 'autoplay="autoplay"';
				playbtn = '';
				play_btn = h.pause;
			}else{
				play = '';
				playbtn = 'ktPlayer-on';
				play_btn = h.play;
			}
			var a = '    <video id="video" src="' + this.options.src + '" controls="controls" '+play+' class="ktPlayer-source"></video>';
			a += '    <div class="ktPlayer-pause '+playbtn+'">', a += '        <svg width="50%" height="40%" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">', a += '            <g transform="scale(0.03125, 0.03125)">', a += '                <path d="M153.6 75.794916C153.6 19.283822 190.753317-0.345061 237.362821 32.501243L819.04468 442.419778C865.30561 475.020437 865.140746 527.555686 818.320241 560.007424L238.087264 962.172457C191.426236 994.513664 153.6 974.380703 153.6 918.409001L153.6 75.794916Z" fill="#fff"></path>', a += "            </g>", a += "        </svg>", a += "    </div>", a += '    <div class="ktPlayer-layer">', a += '        <div class="ktPlayer-load">', a += '            <svg width="100%" height="100%" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">', a += '                <g transform="scale(0.03125, 0.03125)">', a += '                    <path class="ktPlayer-circle" d="M959.6 452.2c-2.8-17.4-6.2-34.6-10.6-51.6-5.6-21.6-12.8-43-21.6-63.6-17.8-42.4-42.2-82-71.8-117.2-32-37.8-70.6-70.4-113.4-95.4C700 99.6 654 82 606 72.2c-24.8-5-49.8-8-75.2-8.2-19.8-0.2-39.6 0.6-59.2 2.4-51 5-101.4 19.2-147.8 41-39.8 18.8-76.8 43.2-109.6 72.4-32.8 29.2-61.4 63.2-84.4 100.6-25.4 41.6-44.4 87-54.8 134.6-8.4 38-12.4 77.2-10.4 116.2 1.8 37.8 7.6 75.6 19 111.8 7.2 23 15.8 45.4 26.6 67.2 10.6 21.4 23 42 36.8 61.4 27.6 38.6 61.2 72.8 99.6 101 39.2 29 83.4 51.4 129.8 66.2 48.4 15.4 99.8 22.6 150.6 20.8 49.6-1.6 98.8-11.2 145.2-29 44.6-17.2 86.4-41.8 123-72.6 18.4-15.6 34.8-33.2 50.2-51.8 15.6-18.8 29.6-38.6 41.2-60 10-18.4 18.4-37.6 25.6-57 3.6-9.6 7-19.2 9.8-29.2 3-10.6 5.2-21.6 7.2-32.4 3-17 4.2-34.6 2.6-51.8-1.4 7.6-2.6 15-4.4 22.4-2.2 8.6-5 17-8.2 25.2-6.4 17.4-14.4 34.2-22 51-9.8 21.4-21.2 41.8-33.6 61.6-6.4 10.2-13 20.2-20.2 29.8-7.2 9.6-15.4 18.8-23.6 27.8-16.4 18.2-34.2 34.4-54 48.8-20.2 14.8-41.6 27.8-64.2 38.6-45.2 22-94.6 35.2-144.6 39.6-51.2 4.4-103.4-0.6-152.6-15.2-46.8-13.8-91.2-36.2-130.2-65.6-37.8-28.6-70.6-63.8-96.4-103.6C150.8 695.6 132.2 649.8 122 602c-2.6-12.4-4.6-25.2-6-37.8-1.2-10.8-2.2-21.8-2.6-32.8-0.6-22.6 0.8-46 4.2-68.4 7.4-49.2 23.4-96.6 48.2-139.8 22-38.6 50.6-73.4 84.2-102.8 33.6-29.6 72-53.4 113.6-70.2 24-9.8 49.2-17 74.8-21.8 13-2.4 26-4.4 39-5.4 6.4-0.6 12.6-0.6 19-1.2 2.6 0 5.2 0.2 7.8 0.2 43.4-0.8 87 4.8 128.4 17.8 44.6 14 86.6 36.6 123 66 38.2 30.8 70 68.8 94 111.6 20.4 36.4 35 75.6 43.8 116.4 2 9.4 3.6 18.8 5.2 28.2 1.4 8.6 6.2 16.6 13.6 21.4 15.6 10.4 37.4 3.4 45-13.4C959.8 464.2 960.6 458 959.6 452.2z" fill="#fff"></path>', a += "                </g>", a += "            </svg>", a += "        </div>", a += "    </div>", a += '    <div class="ktPlayer-controller-mask"></div>', a += '    <div class="ktPlayer-controller">', a += '        <div class="ktPlayer-controller-left">', a += '            <button class="ktPlayer-icon ktPlayer-icon-play">', a += '                <svg width="100%" height="100%" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">', a += '                    <g transform="scale(0.03125, 0.03125)">', a += '                        <path d="'+play_btn+'" fill="#fff"></path>', a += "                    </g>", a += "                </svg>", a += "            </button>",  a += '            <span class="ktPlayer-time">', a += '                <span class="ktPlayer-time-now">00:00</span>&nbsp;/&nbsp;<span class="ktPlayer-time-total">00:00</span>', a += "            </span>", a += "        </div>", a += '        <div class="ktPlayer-controller-right">',a += '            <div class="ktPlayer-volume">', a += '                <button class="ktPlayer-icon ktPlayer-icon-volume">', a += '                    <svg width="100%" height="100%" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">', a += '                        <g transform="scale(0.03125, 0.03125)">', a += '                            <path d="M626.666665 0C742.222848 25.554484 837.332992 86.245551 912 182.074779 986.667008 277.904181 1024 387.878146 1024 512 1024 636.121856 986.667008 746.095821 912 841.925222 837.332992 937.754486 742.222848 998.445496 626.666665 1024L626.666665 903.529411C710.222679 877.974912 778.221911 829.604628 830.666752 758.417111 883.111424 687.229594 909.333335 605.091436 909.333335 512 909.333335 418.908565 883.111424 336.770404 830.666752 265.582888 778.221911 194.395372 710.222679 146.025072 626.666665 120.470588L626.666665 0ZM768 512C768 621.519242 720.889344 700.00684 626.666665 747.465242L626.666665 276.534759C720.889344 323.993162 768 402.480758 768 512L768 512ZM0 439.079676C0 382.575632 45.869382 336.770054 102.722168 336.770054L226.666666 336.770054 512 43.807487 512 980.192512 226.666666 687.229947 102.722168 687.229947C45.990281 687.229947 0 641.413437 0 584.920325L0 439.079676Z" fill="#fff"></path>', a += "                        </g>", a += "                    </svg>", a += "                </button>", a += '                <div class="ktPlayer-volume-bar-wrap">', a += '                    <div class="ktPlayer-volume-bar">', a += '                        <div class="ktPlayer-volume-line">', a += '                            <i class="ktPlayer-volume-thumb"></i>', a += "                        </div>", a += "                    </div>", a += "                </div>", a += "            </div>", a += '            <div class="ktPlayer-setting">', a += '                <button class="ktPlayer-icon ktPlayer-icon-setting">', a += '                    <svg width="100%" height="100%" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">', a += '                        <g transform="scale(0.03125, 0.03125)">', a += '                            <path class="ktPlayer-gear" d="M829.1 553.8c1.7-13.7 3-27.3 3-41.8 0-14.5-1.3-28.2-3-41.8l90-70.4c8.1-6.4 10.2-17.9 5.1-27.3l-85.3-147.6c-5.1-9.4-16.6-12.8-26-9.4l-106.2 42.7c-22.2-17.1-46.1-31.1-72.1-41.8L618.3 103.3c-1.3-10.2-10.2-17.9-20.9-17.9L426.8 85.4c-10.7 0-19.6 7.7-20.9 17.9l-16.2 113.1c-26 10.7-49.9 25.2-72.1 41.8L211.3 215.5c-9.8-3.8-20.9 0-26 9.4l-85.3 147.6c-5.5 9.4-3 20.9 5.1 27.3l90 70.4c-1.7 13.7-3 27.7-3 41.8 0 14.1 1.3 28.2 3 41.8l-90 70.4c-8.1 6.4-10.2 17.9-5.1 27.3l85.3 147.6c5.1 9.4 16.6 12.8 26 9.4l106.2-42.7c22.2 17.1 46.1 31.1 72.1 41.8l16.2 113.1c1.3 10.2 10.2 17.9 20.9 17.9l170.7 0c10.7 0 19.6-7.7 20.9-17.9l16.2-113.1c26-10.7 49.9-25.2 72.1-41.8l106.2 42.7c9.8 3.8 20.9 0 26-9.4l85.3-147.6c5.1-9.4 3-20.9-5.1-27.3L829.1 553.8zM512.1 661.3c-82.3 0-149.3-67-149.3-149.3s67-149.3 149.3-149.3 149.3 67 149.3 149.3S594.4 661.3 512.1 661.3z" fill="#fff"></path>', a += "                        </g>", a += "                    </svg>", a += "                </button>", a += '                <div class="ktPlayer-setting-wrap">', a += '                    <div class="ktPlayer-setting-item" data-speed="0.5">0.5</div>', a += '                    <div class="ktPlayer-setting-item" data-speed="1">1</div>', a += '                    <div class="ktPlayer-setting-item" data-speed="1.5">1.5</div>', a += '                    <div class="ktPlayer-setting-item" data-speed="2">2</div>', a += "                </div>", a += "            </div>", a += '            <button class="ktPlayer-icon ktPlayer-icon-fullscreen" data-on="0">', a += '                <svg width="100%" height="100%" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">', a += '                    <g transform="scale(0.03125, 0.03125)">', a += '                        <path d="M65.422222 145.066667 321.422222 145.066667 321.422222 216.177778 139.377778 216.177778 139.377778 401.066667 65.422222 401.066667ZM59.733333 867.555556 59.733333 611.555556 128 611.555556 128 793.6 315.733333 793.6 315.733333 867.555556ZM958.577778 867.555556 705.422222 867.555556 705.422222 796.444444 887.466667 796.444444 887.466667 608.711111 958.577778 608.711111ZM961.422222 147.911111 961.422222 403.911111 890.311111 403.911111 890.311111 221.866667 702.577778 221.866667 702.577778 147.911111Z" fill="#fff"></path>', a += "                    </g>", a += "                </svg>", a += "            </button>", a += "        </div>", a += '        <div class="ktPlayer-bar-wrap">', a += '            <div class="ktPlayer-bar">', a += '                <div class="ktPlayer-loaded"></div>', a += '                <div class="ktPlayer-played">', a += '                    <i class="ktPlayer-thumb"></i>', a += "                </div>", a += "            </div>", a += "        </div>", a += "    </div>";
			var c = b.createElement("div");
			c.innerHTML = a, c.className = "ktPlayer", this.root.appendChild(c), d = this, this.bind()
		},
		bind: function() {
			d.target = this.root.querySelector(".ktPlayer"), e = this.target.querySelector(".ktPlayer-source"), a.navigator.userAgent.indexOf("Firefox") == -1 && this.target.querySelector(".ktPlayer-circle").setAttribute("class", "ktPlayer-circle ktPlayer-circle-rotate"), e.addEventListener("canplay", this.canPlay), e.addEventListener("durationchange", this.totalTime), e.addEventListener("progress", this.load), e.addEventListener("timeupdate", this.updateTime), this.target.querySelector(".ktPlayer-icon-volume").addEventListener("click", this.mute), e.addEventListener("ended", this.end), this.bindSpeedRate(), this.target.querySelector(".ktPlayer-icon-fullscreen").addEventListener("click", this.fullScreen), e.addEventListener("playing", this.loading), this.target.querySelector(".ktPlayer-bar-wrap").addEventListener("click", this.clickProgressBar), this.target.querySelector(".ktPlayer-thumb").addEventListener("mousedown", this.dragProgressThumb), this.target.querySelector(".ktPlayer-volume-bar").addEventListener("click", this.clickVolumeBar), this.target.querySelector(".ktPlayer-setting").addEventListener("mouseenter", this.SVGSettingMouseenter), this.target.querySelector(".ktPlayer-setting").addEventListener("mouseleave", this.SVGSettingMouseleave), this.target.querySelector(".ktPlayer-icon-fullscreen").addEventListener("mouseenter", this.SVGFullscreenMouseenter), this.target.querySelector(".ktPlayer-icon-fullscreen").addEventListener("mouseleave", this.SVGFullscreenMouseleave), this.target.addEventListener("mousemove", this.hideController), this.target.addEventListener("mouseleave", this.hideController), this.target.querySelector(".ktPlayer-controller").addEventListener("mouseenter", this.controllerMouseenter), this.target.querySelector(".ktPlayer-controller").addEventListener("mouseleave", this.controllerMouseleave), b.addEventListener("keydown", this.keyBoard), b.addEventListener("fullscreenchange", this.fullscreenchange), b.addEventListener("webkitfullscreenchange", this.fullscreenchange), b.addEventListener("mozfullscreenchange", this.fullscreenchange), b.addEventListener("MSFullscreenChange", this.fullscreenchange)
		},
		canPlay: function() {
			d.target.querySelector(".ktPlayer-layer").style.display = "none", d.target.querySelector(".ktPlayer-icon-play").addEventListener("click", d.buttonPlay), e.addEventListener("click", d.videoPlay), d.target.querySelector(".ktPlayer-pause").addEventListener("click", d.videoPlay)
		},
		buttonPlay: function() {
			var a = d.target.querySelector(".ktPlayer-icon-play");
			e.paused ? (d.changeSVG(a, h.pause), e.play(), d.target.querySelector(".ktPlayer-pause").classList.remove("ktPlayer-on")) : (d.changeSVG(a, h.play), e.pause(), d.target.querySelector(".ktPlayer-pause").classList.add("ktPlayer-on"), f && (clearInterval(f), "block" == d.target.querySelector(".ktPlayer-layer").style.display && (d.target.querySelector(".ktPlayer-layer").style.display = "none")))
		},
		videoPlay: function() {
			var a = d.target.querySelector(".ktPlayer-icon-play");
			e.paused ? (d.changeSVG(a, h.pause), e.play(), d.target.querySelector(".ktPlayer-pause").classList.remove("ktPlayer-on")) : (d.changeSVG(a, h.play), e.pause(), d.target.querySelector(".ktPlayer-pause").classList.add("ktPlayer-on"))
		},
		mute: function() {
			e.muted ? (e.muted = !1, d.changeVolumeBar(100 * e.volume)) : (e.muted = !0, d.changeVolumeBar(0))
		},
		changeSVG: function(a, b) {
			a.querySelector("path").setAttribute("d", b)
		},
		end: function() {
			var a = d.target.querySelector(".ktPlayer-icon-play");
			d.changeSVG(a, h.play), d.hideController()
		},
		bindSpeedRate: function() {
			for (var a = d.target.querySelectorAll(".ktPlayer-setting-item"), b = 0; b < a.length; b++) a[b].addEventListener("click", function() {
				e.playbackRate = this.getAttribute("data-speed")
			})
		},
		totalTime: function() {
			var a = d.target.querySelector(".ktPlayer-time-total");
			a.innerHTML = i.timeFormat(e.duration)
		},
		updateTime: function() {
			var a = parseFloat(e.currentTime),
				b = a / e.duration * 100;
			d.target.querySelector(".ktPlayer-played").style.width = b.toFixed(2) + "%", d.target.querySelector(".ktPlayer-time-now").innerHTML = i.timeFormat(a)
		},
		load: function() {
			var a = e.buffered.length ? e.buffered.end(e.buffered.length - 1) / e.duration * 100 : 0;
			d.target.querySelector(".ktPlayer-loaded").style.width = a.toFixed(2) + "%"
		},
		fullScreen: function() {
			var a = (d.target.querySelector(".ktPlayer-icon-fullscreen"), b.fullscreenElement || b.mozFullScreenElement || b.webkitFullscreenElement || b.msFullscreenElement);
			a ? b.exitFullscreen ? b.exitFullscreen() : b.mozCancelFullScreen ? b.mozCancelFullScreen() : b.webkitCancelFullScreen ? b.webkitCancelFullScreen() : b.msExitFullscreen && b.msExitFullscreen() : d.target.requestFullscreen ? d.target.requestFullscreen() : d.target.mozRequestFullScreen ? d.target.mozRequestFullScreen() : d.target.webkitRequestFullscreen ? d.target.webkitRequestFullscreen() : d.target.msRequestFullscreen && d.target.msRequestFullscreen()
		},
		loading: function() {
			var a = 0,
				b = 0,
				c = !1;
			f && clearInterval(f), f = setInterval(function() {
				b = e.currentTime, !c && b < a + .01 && !e.paused && (d.target.querySelector(".ktPlayer-layer").style.display = "block", c = !0), c && b > a + .01 && !e.paused && (d.target.querySelector(".ktPlayer-layer").style.display = "none", c = !1), a = b
			}, 100)
		},
		keyBoard: function(b) {
			var c, f = b || a.event;
			switch (f.keyCode) {
			case 37:
				f.preventDefault(), e.currentTime -= 10;
				break;
			case 39:
				f.preventDefault(), e.currentTime += 10;
				break;
			case 38:
				f.preventDefault(), c = e.volume + .1, d.keyboardVolume(c);
				break;
			case 40:
				f.preventDefault(), c = e.volume - .1, d.keyboardVolume(c)
			}
		},
		keyboardVolume: function(a) {
			a = a.toFixed(2), a = a > 0 ? a : 0, a = a < 1 ? a : 1, d.changeVolumeBar(100 * a), e.volume = a, e.muted && (e.muted = !1)
		},
		changeVolumeBar: function(a) {
			d.target.querySelector(".ktPlayer-volume-line").style.height = a + "%", a >= 50 ? d.changeSVG(d.target.querySelector(".ktPlayer-icon-volume"), h.volume_big) : a > 0 ? d.changeSVG(d.target.querySelector(".ktPlayer-icon-volume"), h.volume_small) : d.changeSVG(d.target.querySelector(".ktPlayer-icon-volume"), h.mute)
		},
		clickProgressBar: function(b) {
			var c, f = b || a.event;
			c = f.pageX ? (f.pageX - i.leftDistance(this)) / this.offsetWidth : (f.clientX - i.leftDistance(this)) / this.offsetWidth, this.querySelector(".ktPlayer-played").style.width = 100 * c + "%", d.target.querySelector(".ktPlayer-time-now").innerHTML = i.timeFormat(c * e.duration), e.currentTime = parseFloat(c * e.duration)
		},
		dragProgressThumb: function() {
			e.removeEventListener("timeupdate", d.updateTime), b.addEventListener("mousemove", d.progressMouseMove), b.addEventListener("mouseup", d.progressMouseUp)
		},
		progressMouseMove: function(b) {
			var c, f = b || a.event,
				g = d.target.querySelector(".ktPlayer-bar");
			c = f.pageX ? (f.pageX - i.leftDistance(g)) / g.offsetWidth : (f.clientX - i.leftDistance(g)) / g.offsetWidth, c = c > 0 ? c : 0, c = c < 1 ? c : 1, d.target.querySelector(".ktPlayer-played").style.width = 100 * c + "%", d.target.querySelector(".ktPlayer-time-now").innerHTML = i.timeFormat(c * e.duration)
		},
		progressMouseUp: function() {
			b.removeEventListener("mousemove", d.progressMouseMove), b.removeEventListener("mouseup", d.progressMouseUp), e.currentTime = parseFloat(d.target.querySelector(".ktPlayer-played").style.width) / 100 * e.duration, e.addEventListener("timeupdate", d.updateTime)
		},
		clickVolumeBar: function(b) {
			var c, f = b || a.event;
			c = f.pageY ? (f.pageY - i.topDistance(this)) / this.offsetHeight : (f.clientY - i.topDistance(this)) / this.offsetHeight, c = 1 - c, c = c > 0 ? c : 0, c = c < 1 ? c : 1, e.volume = c, d.changeVolumeBar(100 * c), e.muted && (e.muted = !1)
		},
		hideController: function() {
			d.target.classList.contains("ktPlayer-controller-hide") && d.target.classList.remove("ktPlayer-controller-hide"), g && clearTimeout(g), e.paused || (g = setTimeout(function() {
				d.target.classList.add("ktPlayer-controller-hide")
			}, 1700))
		},
		SVGSettingMouseenter: function() {
			a.navigator.userAgent.indexOf("Firefox") == -1 && this.classList.add("ktPlayer-setting-on")
		},
		SVGSettingMouseleave: function() {
			this.classList.remove("ktPlayer-setting-on")
		},
		SVGFullscreenMouseenter: function() {
			a.navigator.userAgent.indexOf("Firefox") == -1 && this.classList.add("ktPlayer-icon-fullscreen-on")
		},
		SVGFullscreenMouseleave: function() {
			this.classList.remove("ktPlayer-icon-fullscreen-on")
		},
		controllerMouseenter: function() {
			g && clearTimeout(g), d.target.removeEventListener("mousemove", d.hideController)
		},
		controllerMouseleave: function() {
			d.target.addEventListener("mousemove", d.hideController)
		},
		fullscreenchange: function() {
			var a = d.target.querySelector(".ktPlayer-icon-fullscreen"),
				b = a.getAttribute("data-on");
			"1" === b ? (a.setAttribute("data-on", "0"), a.querySelector("path").setAttribute("d", h.full_off)) : (a.setAttribute("data-on", "1"), a.querySelector("path").setAttribute("d", h.full_on))
		}
	}, a.KTPlayer = c
}(window, document), "undefined" != typeof module && "undefined" != typeof module.exports && (module.exports = window.KTPlayer);