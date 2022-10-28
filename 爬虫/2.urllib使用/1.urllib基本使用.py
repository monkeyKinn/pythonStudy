# _*_ coding : utf-8 _*_
# @Time : 2022/10/28 20:59
# @Author : 金圣聪
# @File : 1.urllib基本使用
# @Project : pythonStudy

# 一.使用urllib获取百度首页源码
import urllib.request

# 1.定义一个url
url = 'http://www.baidu.com'
# 2.模拟浏览器向服务器请求
response = urllib.request.urlopen(url)
# 3.获取响应中页面的源码
# read方法返回的是字节形式的二进制数据
#   所以需要  decode('编码的格式')解码
content = response.read().decode('UTF-8')
# 4.打印数据
print(content)
