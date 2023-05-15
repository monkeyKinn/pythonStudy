# _*_ coding : utf-8 _*_
# @Time : 2022/10/28 21:17
# @Author : 金圣聪
# @File : 2.一个类型和六个方法
# @Project : pythonStudy
import urllib.request
url = 'http://www.baidu.com'
# 模拟发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# <class 'http.client.HTTPResponse'>
# print(type(response))

# 1.read方法 按照一个字节去读
# content = response.read()
# print(content)

# 1.1.返回多少个字节
# content = response.read(5)
# print(content)

# 1.2.读一行
# content = response.readline()
# print(content)

# 1.3读全部
# content = response.readlines()
# print(content)

# 2.返回状态码  200 就是成功
print(response.getcode())
# 3.返回请求的url地址
print(response.geturl())
# 4.获取响应头
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法
# response.read(5)
# response.readline()
# response.readlines()
# response.getcode()
# response.geturl()
# response.getheaders()
