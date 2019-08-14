# encoding='utf-8'

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import random
import datetime
from time import sleep
from threading import Thread

random.seed(datetime.datetime.now())
proxy_list=['162.212.158.182:8080', '35.245.56.57:80', '165.227.64.106:8080', '204.48.24.80:3128',
 '142.93.207.141:8080', '157.230.212.164:3128', '142.93.55.98:8080', '165.22.32.8:80',
  '165.227.71.172:8080', '68.183.100.171:80', '157.230.57.151:8080', '168.235.88.16:8080',
   '142.93.207.141:8090', '159.89.35.245:8080', '159.89.35.245:3128', '209.97.152.252:8080',
    '134.209.166.42:8080', '165.22.32.8:8080', '165.22.14.234:8080', '142.93.127.190:80',
    '104.248.115.236:8080', '206.189.231.226:80', '159.203.88.39:3128', '142.93.59.240:8080',
     '68.183.135.4:8080', '159.203.118.239:8080', '157.230.212.164:80', '134.209.170.22:3128',
      '134.209.73.47:80', '68.183.99.96:8080', '68.183.24.193:8080', '142.93.78.113:8080',
       '104.248.8.35:3128', '142.93.151.72:80', '172.107.2.69:3128', '157.230.227.116:8080',
        '68.183.99.96:3128', '68.183.156.72:80', '134.209.112.110:8080', '134.209.77.133:3128',
         '68.183.156.72:8080', '157.230.212.164:8080', '157.230.8.180:8080', '157.230.13.186:8080',
          '167.88.117.209:8080', '157.230.0.117:8080', '159.89.142.5:8080', '74.91.20.42:8080',
'后面太多省略不写了'
]
article_list=['https://blog.csdn.net/zy345293721/article/details/96855355','https://blog.csdn.net/zy345293721/article/details/97112340']
cookie=list()
cookie.append({'cookie':'你的cookie'})
cookie.append({'12':'1234'})
cookie.append({'121':'1234'})
cookie.append({'122':'1234'})
cookie.append({'123':'1234'})
cookie.append({'126':'1234'})
cookie.append({'125':'1234'})

User_Agent = [
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)"
]

def get_proxy_list():
    for row in urlopen('http://proxylist.fatezero.org/proxy.list').readlines():
        item=json.loads(row)
        if item['type']=='http' and item['anonymity']=='high_anonymous' and item['response_time']<7 :
            proxy_list.append(item['host']+':'+str(item['port']))


def solve():
    article=article_list[random.randint(0,len(article_list)-1)]
    proxy={'http':proxy_list[random.randint(0,len(proxy_list)-1)]}
    header={'User-Agent':User_Agent[random.randint(0,len(User_Agent)-1)],
            'referer':'http://blog.csdn.net'}
    try:
        requests.get(article.replace('https','http'),headers=header,proxies=proxy,
            cookies=cookie[random.randint(0,len(cookie)-1)],timeout=7)
        print('ok ip:'+proxy['http'])
    except:
        print('no')



#get_proxy_list()
#print('Done--get_proxy_list!')
#f=open('output.out','w')
#print(proxy_list,file=f)
#f.close()
#get_article_list()
#print('Done--get_article_list!')
#f=open('output2.out','w')
#print(article_list,file=f)
#f.close()
def do():
    while True:
        solve()

mission=list()      #多线程跑的快
nums=50
for i in range(nums):
    mission.append(Thread(target=do))
for i in range(nums):
    #mission[i].setDaemon(True)
    mission[i].start()
for i in range(nums):
    mission[i].join()
