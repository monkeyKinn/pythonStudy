# _*_ coding : utf-8 _*_
# @Time : 2022/11/28 23:03
# @Author : 金圣聪
# @File : 15.handle的基本使用
# @Project : pythonStudy

# 需求:演示使用handle访问百度,获取网页源码
import urllib.request

url = "http://www.baidu.com"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

req = urllib.request.Request(url=url, headers=headers)

# 原来
# resp = urllib.request.urlopen(req)

# 现在
# handler build_open open
# 1.获取handler对象
handler = urllib.request.HTTPHandler()
# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调用opener方法
resp = opener.open(req)
content = resp.read().decode('utf-8')
print(content)
