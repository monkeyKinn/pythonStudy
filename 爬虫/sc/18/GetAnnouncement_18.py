# _*_ coding : utf-8 _*_
# 18获取公告
# @Time : 2023/4/20 22:59
# @Author : 金圣聪
# @File : GetAnnouncement_18.py
# @Project : pythonStudy
import urllib.request
from bs4 import BeautifulSoup
import ast
from datetime import datetime
import time

# 记录开始时间
start_time = time.time()


def filter_data(data):
    for item in data:
        for sub_item in item['list']:
            yield {
                'title': sub_item['title'],
                'url': sub_item['url'],
                'time': datetime.fromtimestamp(sub_item['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            }


# 1.定义一个url
url = 'https://info.18art.art/html/infor/infor.html?sub=0&v=1682010188874'
# 2.模拟浏览器向服务器请求
response = urllib.request.urlopen(url)
# 3.获取响应中页面的源码
# read方法返回的是字节形式的二进制数据
#   所以需要  decode('编码的格式')解码
content = response.read().decode('UTF-8')
# 4.打印数据
# print(content)

soup = BeautifulSoup(content, 'html.parser')
injectJsonStr = soup.findAll('script')[2].text.split(';')[1].strip().replace('window.__injectJson=', '')

injectJson = ast.literal_eval(injectJsonStr)
# 通知列表
noticeList = injectJson['noticeList']

result = max(filter_data(noticeList), key=lambda x: x['time'])
print(result)
# 记录结束时间
end_time = time.time()

print("代码执行时间为：", end_time - start_time, "秒")
