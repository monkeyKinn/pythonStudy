# _*_ coding : utf-8 _*_
# 18获取公告
# @Time : 2023/4/20 22:59
# @Author : 金圣聪
# @File : GetAnnouncement_18.py
# @Project : pythonStudy

import ast
import json
import threading
import time
import urllib.parse
import urllib.request
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# 定义Qmsg的key
QMSG_KEY = 'ad4f0b3cfa3f54d577fb171b49df6719'
# 定义18的公告url
notice_url_18 = 'https://info.18art.art/html/infor/infor.html?sub=0&v='


class WebsiteChecker:
    def __init__(self, url):
        self.url = url
        self.value = None
        self.lock = threading.Lock()
        self.name = url

    def run(self):
        while True:
            current_value = get_value_from_url(self.url)
            with self.lock:
                if current_value != self.value:
                    print(f"New value for {self.url}: {current_value}")
                    self.value = current_value
                    # do additional logic here
                    print(f"thread name: {self.name} | Value for {self.url} is changed:")
                    print(f"Value is {self.value}")
                    msg = get_msg(self.value)
                    send_by_qmsg(msg)
                    # print(msg)
                else:
                    print(f"{datetime.now()} | thread name: {self.name} | Value for {self.url} is unchanged")
            time.sleep(0.5)


def get_msg(values):
    if "18art.art" in values['url']:
        return build_msg_18(values)


# 构建18的msg
def build_msg_18(value):
    title = value['title']
    url = value['url']
    class_name = value['className']
    msg = \
        '【18】\n' \
        '类型: ' + class_name + '\n' \
        '公告: ' + title + '\n' \
        '链接: ' + url + '\n' \
        '图灵 | 数藏公告Q裙(PS: 更多功能开发ing...): 340129397'
    return msg


# 发送机器人请求
def send_by_qmsg(msg):
    print('发送机器人请求')
    # 发送post请求
    qmsg_group_url = 'https://qmsg.zendee.cn:443/group/' + QMSG_KEY

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


# 获取18最新的公告,返回格式是: {"title": "","url": "","time": ""}
def get_notice_from_18(notice_url):
    # 2.模拟浏览器向服务器请求
    url = notice_url + str(int(round(time.time() * 1000)))
    # response = urllib.request.urlopen(url)
    # # 3.获取响应中页面的源码
    # # read方法返回的是字节形式的二进制数据
    # #   所以需要  decode('编码的格式')解码
    # content = response.read().decode('UTF-8')
    # # 4.打印数据
    # # print(content)
    # soup = BeautifulSoup(content, 'html.parser')
    # inject_json_str = soup.findAll('script')[2].text.split(';')[1].strip().replace('window.__injectJson=', '')
    # inject_json = ast.literal_eval(inject_json_str)
    # # 通知列表
    # notices_list = inject_json['noticeList']

    cookies = {
        'USER-TOKEN': 'd8OLe1gxt40bQ9oVtgLOCoormmr0nrsGftpadgVSqK0=',
    }

    headers = {
        'authority': 'info.18art.art',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = "UTF-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    inject_json_str = soup.findAll('script')[2].text.split(';')[1].strip().replace('window.__injectJson=', '')
    inject_json = ast.literal_eval(inject_json_str)
    # 通知列表
    notices_list = inject_json['noticeList']
    # 返回最新的一个
    return max(filter_notices_18(notices_list), key=lambda x: x['time'])


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


if __name__ == "__main__":
    urls = [notice_url_18, ]
    checkers = []

    for url in urls:
        checker = WebsiteChecker(url)
        checkers.append(checker)
        threading.Thread(target=checker.run, daemon=True).start()

    # main thread waits for keyboard interrupt
    event = threading.Event()
    event.wait()
