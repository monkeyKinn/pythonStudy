# _*_ coding : utf-8 _*_
# @Time : 2022/11/28 23:19
# @Author : 金圣聪
# @File : 16.代理
# @Project : pythonStudy
import urllib.request
# 百度ip不显示,所以用这个网站来做显示
url = "http://www.dingk.cn/IP/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
# 请求对象的定制
req = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问服务器
# resp = urllib.request.urlopen(req)

proxies = {
# 高可用全球免费代理IP库
# https://ip.jiangxianli.com/blog/23562.html
    'http': '110.164.3.7:8888'
}
handler = urllib.request.ProxyHandler(proxies = proxies)
opener = urllib.request.build_opener(handler)
resp = opener.open(req)
content = resp.read().decode('gb2312')
# 保存到本地
with open('daili.html', 'w', encoding='gb2312') as fp:
    fp.write(content)
    fp.close()
