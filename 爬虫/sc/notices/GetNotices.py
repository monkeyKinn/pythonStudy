# _*_ coding : utf-8 _*_
# 18获取公告
# @Time : 2023/4/20 22:59
# @Author : 金圣聪
# @File : GetNotices.py
# @Project : pythonStudy
import ast
import urllib.request
import urllib.parse
from datetime import datetime

from bs4 import BeautifulSoup
import threading
import time
import json

# 定义Qmsg的key
QMSG_KEY = 'ad4f0b3cfa3f54d577fb171b49df6719'
# 定义18的公告url
notice_url_18 = 'https://info.18art.art/html/infor/infor.html?sub=0&v=1682010188874'


# 过滤18的公告,只需要 className|title|url|time
def filter_notices_18(data):
    for item in data:
        for sub_item in item['list']:
            yield {
                'className': sub_item['className'],
                'title': sub_item['title'],
                'url': sub_item['url'],
                'time': datetime.fromtimestamp(sub_item['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            }


# 获取18最新的公告,返回格式是: {"title": "","url": "","time": ""}
def get_notice_from_18(notice_url):
    # 2.模拟浏览器向服务器请求
    response = urllib.request.urlopen(notice_url)
    # 3.获取响应中页面的源码
    # read方法返回的是字节形式的二进制数据
    #   所以需要  decode('编码的格式')解码
    content = response.read().decode('UTF-8')
    # 4.打印数据
    # print(content)
    soup = BeautifulSoup(content, 'html.parser')
    inject_json_str = soup.findAll('script')[2].text.split(';')[1].strip().replace('window.__injectJson=', '')
    inject_json = ast.literal_eval(inject_json_str)
    # 通知列表
    notices_list = inject_json['noticeList']
    # 返回最新的一个
    return max(filter_notices_18(notices_list), key=lambda x: x['time'])


# 定义每个URL对应的获取值的方法
def get_value_from_url(url):
    # 判断字符川里是否包含指定字符
    if "18art.art" in url:
        # print("是18的告")
        # print("开始获取并设置值.....")
        return get_notice_from_18(url)
    elif "42" in url:
        print("是42的告")
    else:
        return None


# 定义一个字典类型的变量，保存每个URL对应的上一个值
last_values = {}


# 定义每个线程需要执行的方法
def check_value(url):
    while True:
        value = get_value_from_url(url)
        # print(f"此次获取到的值是:{value}")
        last_value = last_values.get(url)
        # print(f"最新的值是:{last_value}")
        if value != last_value:
            # 如果当前值与上一个值不相等，进行进一步的逻辑处理
            # print(f"从 {url} 获取到的值已经从 {last_value} 变成了 {value}")
            last_values[url] = value
            # print(f'最新的值是{last_value[url]}')
            # 发送机器人请求
            msg = get_msg(last_values)
            send_by_qmsg(msg)

        else:
            # 如果相等，则休眠0.5秒
            print(f"{datetime.now()} | 从 {url} 获取到的值:{value},和上次的值:{last_value}的一样. 睡30s")
            time.sleep(0.5)


def get_msg(values):
    # 3.遍历字典的key-value
    for (key, value) in values.items():
        # print(key, value)
        # 是18的url
        if key == notice_url_18:
            return build_msg_18(value)


# 构建18的msg
def build_msg_18(value):
    title = value['title']
    url = value['url']
    class_name = value['className']
    msg = '【18】\n' \
          '类型: ' + class_name + '\n' \
          '公告: ' + title + '\n' \
          '链接: ' + url + '\n' \
          '图灵 | 数藏公告Q裙(PS: 更多功能开发ing...): 340129397'
    return msg


# 发送机器人请求
def send_by_qmsg(msg):
    # print('发送机器人请求')
    # 发送post请求
    qmsg_group_url = 'https://qmsg.zendee.cn:443/send/' + QMSG_KEY

    data = {
        'msg': msg,
        'qq': '340129397'
    }
    # post请求的参数必须编码
    load = urllib.parse.urlencode(data).encode('utf-8')
    # post的请求的参数是不会拼接在Url的后面的，而是需要放在请求对象定制的参数中
    req = urllib.request.Request(url=qmsg_group_url, data=load)
    # 设置Content-Type为application/x-www-form-urlencoded
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    resp = urllib.request.urlopen(req)
    resp_content = resp.read().decode('utf-8')
    # 字符串变json对象
    js_content = json.loads(resp_content)
    print(f"机器人发送结果: {js_content['reason']}")


# 定义多线程执行的方法
def send_notices():
    # todo 在这里添加您需要检查的URL
    urls = [notice_url_18,
            # XXX
            ]

    for url in urls:
        last_values[url] = get_value_from_url(url)
        # print(f'设置值成功,此时,{last_values[url]}')

        thread = threading.Thread(target=check_value, args=(url,))
        thread.start()


if __name__ == '__main__':
    # 执行多线程方法
    send_notices()
