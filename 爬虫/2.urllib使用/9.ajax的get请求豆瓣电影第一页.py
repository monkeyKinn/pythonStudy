# _*_ coding : utf-8 _*_
# @Time : 2022/11/8 23:15
# @Author : 金圣聪
# @File : 9.ajax的get请求豆瓣电影
# @Project : pythonStudy

# 需求:
# 1.get请求
# 2.获取豆瓣第一页的数据并保存起来

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    # 一定要cookie 否则百度安全验证 (截止2022年11月1日 01:48:35 暂时不验证cookie有效性(可以过期))
    'cookie': ''
}
# 1.请求对象的定制
req = urllib.request.Request(url=url, headers=headers)
# 2.获取响应数据
resp = urllib.request.urlopen(req)
content = resp.read().decode('utf-8')
# 数据下载到本地

# 3.下载到本地
# open方法默认使用gbk编码,如果要想保存汉字,需要指定编码格式
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)
# 以上两句话可以等价于下面
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

fp.close()
