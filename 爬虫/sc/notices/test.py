# _*_ coding : utf-8 _*_
# @Time : 2023/4/28 1:22
# @Author : 金圣聪
# @File : test.py
# @Project : pythonStudy
# 定义18的公告url
import time

notice_url_18 = 'https://info.18art.art/html/infor/infor.html?sub=0&v=1682010188874'
a = {'https://info.18art.art/html/infor/infor.html?sub=0&v=1682010188874': {
    'title': '【十八数藏寄售公告】藏品《满窗清景》开放寄售',
    'url': 'https://info.18art.art/html/infor/detail/infor_detail_260bf62de2d54882ac9d148e444958f4.html?v=1682609703623',
    'time': '2023-04-27 23:35:04'}}

for (key, value) in a.items():
    # print(key, value)
    # print()
    if key == notice_url_18:
        # print(value)
        # 组装msg
        title = value['title']
        url = value['url']
        msg = '【18】\n' \
              '公告: ' + title + '\n' \
                                 '链接: ' + url
        print(msg)

urls = [notice_url_18,
        # XXX
        ]
print(len(urls))
for url in urls:
    print(url)
url = '123' + '时间'
print(url)

print(int(round(time.time() * 1000)))
