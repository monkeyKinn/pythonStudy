# _*_ coding : utf-8 _*_
# ysw互助
# @Time : 2023/4/18 19:57
# @Author : 金圣聪
# @File : yswHelpEachOther.py
# @Project : pythonStudy
import requests
import os
import time
import random

# 获取cookie
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

def help(tokenParams):

    headers = {
        'authority': 'api.codeleven.cn',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://shipan.yuanshuwang.com',
        'pragma': 'no-cache',
        'referer': 'https://shipan.yuanshuwang.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'user-token': tokenParams,
    }

    paramsList = [{
        'inviteCode': '6ra343001',
    },{
        'inviteCode': 'oN7342993',
    }
    ]
    # 有bug 每个cookie进来都会助力paramList.size()的次数(存在重复助力+会给自己助力)
    # 但是接口没有限制,暂且就这样吧
    for params in paramsList:
        # 随机睡几秒
        time.sleep(round(random.uniform(1, 10), 3))
        response = requests.post(
            'https://api.codeleven.cn/nft-live/server/integral/user/receive/help',
            params=params,
            headers=headers
        )
        print('助力成功' if len(response.json().get('message')) == 0 else response.json().get('message'))

for cookie in cookieList:
    help(cookie)