from time import time

# LOGO Base64图像
DATA_LOGO = '''iVBORw0KGgoAAAANSUhEUgAAAEYAAAAqCAIAAACBerryAAAAAXNSR0IArs4c6QAAAARnQU1
    BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAFgSURBVGhD7ZPRbcMwDAU7SL+KjNNlO1hncAPo5Mr
    Pii2JdKWkOtxPQlLkQ5C35eXwjPT9frvLh374RAphUinkKOmx8NeRCtssOESSK1cpbynpMTIj5ZArVyknSEOQmh
    /WSHKfSFNEqkFqfsxIO+Q+kaaIVIPU/JiRdsh9Ik0RqQap+TEj7ZD7GuQhP/pHCvKcB42R5CBHWWCgJZIccY
    VsaqI6kuy+SJY1URdJFh/LTII0HMtMPf0jPSqF7xu4KhIDO6TtQAbq+ff/pTuy+yJZ1kR1pIBc4CgLDDRGWpGDL
    PKiGWukFDnxVMa8sUb6+Pp0lEdtFEWSxV3klALykeS5AeXQHBpJJgeXo7dsIsnAU8jpCb+RpLVQhp2QxwtlOFIUi
    Y6uyEmpdERMvxKTrsiKEpmMvPR/KSADg8vRWzRSQCYHlENz5COlyFsd5aAzziMdICtd5GkDpkhjMiONz7L8AOPg
    WYPWCndQAAAAAElFTkSuQmCC
    '''

# 窗口把手 Base64图像，翻译器不使用
DATA_SASH = '''R0lGODlhGAADAPIFAEBAQGBgYICAgLu7u8zMzAAAAAAAAAAAACH5BAEAAAUALAAAAA
            AYAAMAAAMaWBJQym61N2UZJTisb96fpxGD4JBmgZ4lKyQAOw==
'''


PANE_COLORS = ['blue', 'blue']
MAIN_FRAME_BG = LB_GB = 'blue'
LB_FG = 'white'

# 有道在线翻译URL
URL1 = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# 有道翻译API URL
URL = 'http://aidemo.youdao.com/trans'

# 有道翻译API所需的Request Header
HEADERS = {
    'Host': 'aidemo.youdao.com',
    'Connection': 'keep-alive',
    'Content-Length': '24',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://aidemo.youdao.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://aidemo.youdao.com/transdemo',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'

}
HEADERS['User-Agent'] =  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'


HEADERS['Cookie'] = 'OUTFOX_SEARCH_USER_ID=409455193@10.168.8.76; \
OUTFOX_SEARCH_USER_ID_NCOO=2113473423.5020742; fanyi-ad-id=40789; \
fanyi-ad-closed=1; UM_distinctid=1618e20c3e3190-031bfc0c4d2ac5-3c604504-144000-1618e20c3e4317; \
_ntes_nnid=8f57137f8b374f4df18235c4002a23a1,1518509662707; JSESSIONID=aaadxYyqAuuUBd5xwesgw; \
___rl__test__cookies=' + str(time()*1000)

# 有道在线翻译所需的Request Header
Headers_1 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Length': '200',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

Headers_1['Cookie'] = 'OUTFOX_SEARCH_USER_ID=833904829@10.169.0.84; OUTFOX_SEARCH_USER_ID\
_NCOO=1846816080.1245883;  ___rl__test__cookies='+str(time()*1000)


post_form = {                  # 有道翻译API页面需要提交的数据表单
    'q': 'face',
    'from':'Auto',
    'to': 'Auto'
}

post_form1 = {                   # 有道在线翻译页面需要提交的数据表单
    'i': '',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'',
    'sign':'',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'false'
}

WORDS_NUM_LIMIT_1 = 4800  # 有道在线翻译页面专用
WORDS_NUM_LIMIT_2 = 800   # 有道翻译API专用

