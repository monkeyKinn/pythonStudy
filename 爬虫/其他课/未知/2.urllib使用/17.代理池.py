# _*_ coding : utf-8 _*_
# @Time : 2022/11/29 1:05
# @Author : 金圣聪
# @File : 17.代理池
# @Project : pythonStudy
import random
import urllib.request

proxies_pool = [
    {'http': '185.11.89.120:80'},
    {'http': '89.38.98.236:80'},
    {'http': '223.84.240.36:9091'},
    {'http': '223.96.90.216:8085'},
    {'http': '110.164.3.7:8888'},
]


proxies = random.choice(proxies_pool)
print(proxies)
url = "http://www.dingk.cn/IP/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
# 请求对象的定制
req = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问服务器
# resp = urllib.request.urlopen(req)

handler = urllib.request.ProxyHandler(proxies = proxies)
opener = urllib.request.build_opener(handler)
resp = opener.open(req)
content = resp.read().decode('gb2312')
# 保存到本地
with open('daili.html', 'w', encoding='gb2312') as fp:
    fp.write(content)
    fp.close()
