# 操盘大师列表
import requests


def get_CPDS() -> list:
    """
    获取操盘大师界面列表 的前十位
    :rtype: list
    :return:
    """
    headers = {
        'Host': 'game-api.juhaoqiang.com',
        'Origin': 'http://www.hotdogapp.cn',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Referer': 'http://www.hotdogapp.cn/',
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiI3NTU0MjMiLCJCdWZmZXJUaW1lIjo2MDAsImV4cCI6MTY4NjIwMjgzOSwiaXNzIjoiZ2FtZS1hcGkiLCJuYmYiOjE2ODU1OTcwMzl9.0AfdXGfiePTayIjeJ_vVatuXo6BZiHsJFwOwqtkj6DQ',
    }
    json_data = {}
    response = requests.post('https://game-api.juhaoqiang.com/aiera/v1/game/hof/buyer_rank', headers=headers,
                             json=json_data)
    if response.json().get('code') != 0:
        return None
    resp_list = response.json().get('data').get('rank_list')[0:10]
    return resp_list


def get_ZYMS() -> list:
    """
    获取专业买手界面列表 的前十位
    :rtype: list
    :return:
    """
    headers = {
        'Host': 'game-api.juhaoqiang.com',
        'Origin': 'http://www.hotdogapp.cn',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Referer': 'http://www.hotdogapp.cn/',
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiI3NTU0MjMiLCJCdWZmZXJUaW1lIjo2MDAsImV4cCI6MTY4NjIwMjgzOSwiaXNzIjoiZ2FtZS1hcGkiLCJuYmYiOjE2ODU1OTcwMzl9.0AfdXGfiePTayIjeJ_vVatuXo6BZiHsJFwOwqtkj6DQ',
    }
    json_data = {}
    response = requests.post('https://game-api.juhaoqiang.com/aiera/v1/game/hof/master_trader_rank', headers=headers,
                             json=json_data)
    if response.json().get('code') != 0:
        return None
    resp_list = response.json().get('data').get('rank_list')[0:10]
    return resp_list


def get_buy_info(user_id):
    """
    获取具体的某个人买的列表
    :param user_id: 用户id
    :return:
    """
    headers = {
        'Host': 'game-api.juhaoqiang.com',
        'Content-Type': 'application/json',
        'Origin': 'http://www.hotdogapp.cn',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Referer': 'http://www.hotdogapp.cn/',
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiI3NTU0MjMiLCJCdWZmZXJUaW1lIjo2MDAsImV4cCI6MTY4NjIwMjgzOSwiaXNzIjoiZ2FtZS1hcGkiLCJuYmYiOjE2ODU1OTcwMzl9.0AfdXGfiePTayIjeJ_vVatuXo6BZiHsJFwOwqtkj6DQ',
    }

    json_data = {
        'user_id': user_id,
    }

    response = requests.post('https://game-api.juhaoqiang.com/aiera/v1/game/hof/buyer_buy', headers=headers,
                             json=json_data)
    if response.json().get('code') != 0:
        return None
    buy_list = response.json().get('data').get('buy_list')
    return buy_list


if __name__ == '__main__':
    # 操盘大师
    cpds_list = get_CPDS()
    info_1 = '热狗 操盘大师 排行:'
    print(info_1)
    for cpds in cpds_list:
        name = cpds.get('name')
        user_id = cpds.get('user_id')
        rank_num = cpds.get('rank_num')
        buy_list = get_buy_info(user_id)
        str_info_1 = f'No.{rank_num} 【{name}】买了如下: '
        print(str_info_1)
        for buy in buy_list:
            # 名字
            product_name = buy.get('product_name')
            # 均价
            buy_price = buy.get('buy_price')
            # 数量
            product_num = buy.get('current_price')
            # 购买时间
            buy_time = buy.get('buy_time')
            str_info_2 = f'\t藏品名:{product_name},购入均价:{buy_price},购入数量:{product_num},购买时间:{buy_time}'
            print(str_info_2)
    print('-' * 50)
    # 专业买手
    zyms_list = get_ZYMS()

    info_2 ='热狗 专业买手 排行:'
    print(info_2)
    for zyms in zyms_list:
        name = zyms.get('name')
        user_id = zyms.get('user_id')
        rank_num = zyms.get('rank_num')
        buy_list = get_buy_info(user_id)
        str_info_1 = f'No.{rank_num} 【{name}】买了如下: '
        print(str_info_1)
        for buy in buy_list:
            # 名字
            product_name = buy.get('product_name')
            # 均价
            buy_price = buy.get('buy_price')
            # 数量
            product_num = buy.get('current_price')
            # 购买时间
            buy_time = buy.get('buy_time')
            str_info_2 = f'\t藏品名:{product_name},购入均价:{buy_price},购入数量:{product_num},购买时间:{buy_time}'
            print(str_info_2)
