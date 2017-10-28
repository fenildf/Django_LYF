export const GET_QUESTIONS = 'GET_QUESTIONS';
export const UPDATE_QUESTIONS = 'UPDATE_QUESTIONS';
export const GET_SIMILAR_QUESTIONS = 'GET_SIMILAR_QUESTIONS';
export const UPDATE_SIMILAR_QUESTIONS = 'UPDATE_SIMILAR_QUESTIONS';
export const AUTH_USER_INFO = 'AUTH_USER_INFO';
export const UPDATE_AUTH_INFO = 'UPDATE_AUTH_INFO';
export const GET_PAPER = 'GET_PAPER';
export const UPDATE_PAPER = 'UPDATE_PAPER';
export const GET_FILTER_OPTIONS = 'GET_FILTER_OPTIONS';
export const UPDATE_PAPER_LIST = 'UPDATE_PAPER_LIST';
export const GET_BOTH_OPTIONS = 'GET_BOTH_OPTIONS';
export const UPDATE_CURRENT_PAPER_LIST = 'UPDATE_CURRENT_PAPER_LIST';

export function change2Https (data) {
    if (data && location.protocol === 'https:') {
        data.question_html && data.question_html !== '' && (data.question_html = data.question_html.replace(/http:/ig, 'https:'));
        data.option_html && data.option_html !== '' && (data.option_html = data.option_html.replace(/http:/ig, 'https:'));
        data.fenxi && data.fenxi !== '' && (data.fenxi = data.fenxi.replace(/http:/ig, 'https:'));
        data.answer_all_html && data.answer_all_html !== '' && (data.answer_all_html = data.answer_all_html.replace(/http:/ig, 'https:'));
        data.jieda && data.jieda !== '' && (data.jieda = data.jieda.replace(/http:/ig, 'https:'));
        data.dianping && data.dianping !== '' && (data.dianping = data.dianping.replace(/http:/ig, 'https:'));
    }
}

export function appendComments() {
	//测试环境
	//var appid = 'cyt711fXC'; 
	//var conf = '43e0ed9e356220f881795f163db59f0f';
	//生产环境
	var appid = 'cyt7wyxNx'; 
	var conf = '07752d867d384577b7803e71a0686214';
	var width = window.innerWidth || document.documentElement.clientWidth; 
	if (width < 960) {
		//window.document.write('<script id="changyan_mobile_js" charset="utf-8" type="text/javascript" src="https://changyan.sohu.com/upload/mobile/wap-js/changyan_mobile.js?client_id=' + appid + '&conf=' + conf + '"><\/script>');
		var c=document.getElementsByTagName("head")[0]||document.head||document.documentElement;
		var b=document.createElement("script");
		b.setAttribute("id","changyan_mobile_js");
		b.setAttribute("type","text/javascript");
		b.setAttribute("charset","UTF-8");
		b.setAttribute("src","https://changyan.sohu.com/upload/mobile/wap-js/changyan_mobile.js?client_id=" + appid + "&conf=" + conf);
		c.appendChild(b);
	} else {
		var loadJs=function(d,a) {
			var c=document.getElementsByTagName("head")[0]||document.head||document.documentElement;
			var b=document.createElement("script");
			b.setAttribute("type","text/javascript");
			b.setAttribute("charset","UTF-8");
			b.setAttribute("src",d);
			if(typeof a==="function"){
				if(window.attachEvent){
					b.onreadystatechange=function(){
						var e=b.readyState;
						if(e==="loaded"||e==="complete"){
							b.onreadystatechange=null;a()
						}
					}
				}else{
					b.onload=a
				}
			}
			c.appendChild(b)
		};
		loadJs("https://changyan.sohu.com/upload/changyan.js",function(){
			window.changyan.api.config({appid:appid,conf:conf})
		});
	}
}

export function getCookie(key) {
    let a, reg = new RegExp('(^| )' + key + '=([^;]*)(;|$)');
    if (a = document.cookie.match(reg)) {
        return decodeURIComponent(a[2]);
    } else {
        return '';
    }
}

export function removeCookie(key) {
	var exp = new Date();
	exp.setTime(exp.getTime() - 100000);
	var cval =getCookie(key);
	if(cval!=null) {
		document.cookie = key+"="+cval+";expires="+exp.toGMTString();
	}
}