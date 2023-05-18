# _*_ coding : utf-8 _*_
# @Time : 2023/5/16 19:25
# @Author : 金圣聪
# @File : buying.py
# @Project : pythonStudy

import requests
import time
cookies = {
    'acw_tc': '700f252016843069164351454ea0681e020ee7bba8ad27e1294fcfe929',
    'cdn_sec_tc': '700f252016843069164351454ea0681e020ee7bba8ad27e1294fcfe929',
    'acw_sc__v2': '64647be4bdb8febd4a8c21fdbbf9e623e85c36b5',
    'PHPSESSID': 'rje1lfrug11gn76e5m8ppajpsa',
    'arp_scroll_position': '0',
    'ssxmod_itna': 'GqmOBI4IxGxRxBPGKiQi30Ihj17vq34pdjdD/ADfx4iNDnD8x7YDvG+pK7GY7YW2D2EGmWBG2E=bt1QgRTogrD4GLDmKDyWiaeeDxaq0rD74irDDxD3+xlFkDvxG=DpxGPnDj4i1RxjKDhpP8WDGd3WYqLx0WDCyaD7KDn6BdD4DOnxGCAxDrnxG1Hx07n2BzDYFdk9KDEjKqDG5qnR0QQnEO693ztKopFIovHfgaGUOLvBFCchKDopcAPU9RurHLZ0exbD2Wqn1WHirq7WtPb0ZYGGm4anayHn=D==zNHYD',
    'ssxmod_itna2': 'GqmOBI4IxGxRxBPGKiQi30Ihj17vq34pdQDSD8wGDeGN+QGaAmm+H1OIa+28EIho9hHxw=By=4qk2kc2mNofqKWfSCn4idDEQAyFzRRfcIhODfOkHnq=x7jaAZraKPPtoQN3p93tYKQDjKD+2GDD',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acco': '2',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://ur.himayi.cn',
    'Referer': 'https://ur.himayi.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9pbnNpZGUzXC8iLCJhdWQiOiJodHRwOlwvXC9pbnNpZGUzXC8iLCJpYXQiOjE2ODQzMDY5NDEsIm5iZiI6MTY4NDMwNjk0MSwiZXhwIjoxNjg0MzkzMzQxLCJtZW1iZXJfaW5mbyI6MzEyMDN9.a1OuHrMZfAmkviQBR4UU5v-Uam4EKCGpr5v0SICwwB8',
}

json_data = {
    'goods_id': '14',
    'sort_type': 2,
    'page_size': 15,
    'page': 1,
}

while True:
    response = ''
    try:
        time.sleep(0.001)
        response = requests.post(
            'https://ur.himayi.cn/h5/super/api/member/getDetailsSealList',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        goods = response.json().get('data').get('data')
        if len(goods) >= 1:
            for good in goods:
                it_id = good.get('id')
                if good.get('goods_status') != 2:
                    print(f'有可锁的,编号:{good.get("collection_number")}')
                    json_data_creat = {
                        'goods_id': 14,
                        'order_type': 3,
                        'id': it_id,
                    }
                    response = requests.post('https://ur.himayi.cn/h5/super/order/createOrder', cookies=cookies,
                                             headers=headers,
                                             json=json_data_creat)
                    try:
                        flag = response.json().get('msg') == '点击的太快了呢,请您稍后重试!'
                        while flag:
                            # time.sleep(0.001)
                            response = requests.post('https://ur.himayi.cn/h5/super/order/createOrder', cookies=cookies,
                                                     headers=headers,
                                                     json=json_data_creat)
                            flag = response.json().get('msg') == '点击的太快了呢,请您稍后重试!'
                            if not flag:
                                if response.json().get('msg') == 'OK':
                                    order_id = response.json().get('data').get('order_id')
                                    order_sn = response.json().get('data').get('order_sn')
                                    json_data = {
                                        'order_id': order_id,
                                    }

                                response = requests.post('https://ur.himayi.cn/h5/super/order/getPaySetting',
                                                         cookies=cookies, headers=headers, json=json_data)
                    except Exception as e:
                        print(e)
                        print(f'小错误:{e}')
                        print(response.text)
                print(f'没有未锁定的,id为{it_id}')
                print(f'----------')
        else:
            print('已退市')
    except Exception as e:
        print(f'大错误:{e}')
        print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"goods_id":"14","sort_type":2,"page_size":15,"page":1}'
# response = requests.post(
#    'https://ur.himayi.cn/h5/super/api/member/getDetailsSealList',
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
