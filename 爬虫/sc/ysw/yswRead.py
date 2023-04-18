# _*_ coding : utf-8 _*_
# ysw阅读
# @Time : 2023/4/18 19:58
# @Author : 金圣聪
# @File : yswRead.py
# @Project : pythonStudy

import requests
import os
import time
import random
def getCookie():
    try:
        if "YSW_TOKEN" in os.environ:
            if len(os.environ["YSW_TOKEN"]) > 10:
                token = os.environ["YSW_TOKEN"]
                print("\n当前从环境变量获取YSW_TOKEN\n")
                return token
    except Exception as e:
        print(f"【getTOKEN Error】{e}")

cookieList = getCookie().split('&')
print(cookieList)


def read(tokenParams):
    headers = {
        'authority': 'api.codeleven.cn',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://shipan.yuanshuwang.com',
        'pragma': 'no-cache',
        'referer': 'https://shipan.yuanshuwang.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'user-token': tokenParams,
    }

    params = {
    'taskCode': 'ab005',
    }

    # 随机睡几秒
    time.sleep(round(random.uniform(1, 10), 3))

    # 阅读
    response = requests.post(
        'https://api.codeleven.cn/nft-live/server/integral/user/receive/integral',
        params=params,
        headers=headers,
    )
    print('挂机领取成功' if len(response.json().get('message')) == 0 else response.json().get('message'))

for cookie in cookieList:
    read(cookie)