# _*_ coding : utf-8 _*_
# @Time : 2022/10/28 23:06
# @Author : 金圣聪
# @File : 4.
# @Project : pythonStudy

import urllib.request

url = 'https://www.baidu.com'
response = urllib.request.urlopen(url)
# 发现返回的不完整
print(response.read().decode('utf-8'))
# UA介绍：User Agent中文名为用户代理，简称 UA，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本。
# 浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等
# 语法:
# request = urllib.request.Request()
print(
    '--------------------------------------------------------------------------------------------------------------------------')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# 因为urlopen()中不能存字典,所以headers不能传入
# 请求对象定制
# 注意: 因为这个Request()形参顺序问题,所以要传入参数指定是哪个形参(关键词传参)
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
