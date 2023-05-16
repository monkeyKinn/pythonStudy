# _*_ coding : utf-8 _*_
# @Time : 2023/5/16 19:25
# @Author : 金圣聪
# @File : buying.py
# @Project : pythonStudy

import requests
import time
cookies = {
    'acw_tc': '7ae4079c16842518773358230e7eceeb35528daab734810cfa88871dc1',
    'cdn_sec_tc': '7ae4079c16842518773358230e7eceeb35528daab734810cfa88871dc1',
    'acw_sc__v2': '6463a4e5fa61adbf4cf25421144044208d66f571',
    'PHPSESSID': 'k6kqn4kp3gj93tg3fosbdk4cth',
    'ssxmod_itna': 'QqGxBDRDcDy7D=Ye0L5YIEP7qCO=KCe7b3ODlOO4A5D8D6DQeGTTXNKeTYed5QvWi70mxQWCbwKGKrfeYhTSADB3DEx06xW9QxiiuDCeDIDWeDiDGRQDFxYoDeg9dDFtyt/luhxWKDwDB=DmqG2BMQDm4DfDDLu3YvuWnfuGu3xgwiDAkDBj0+uD0tDIqGXWAW4tqDBQPa4jqUtVeGWtoQDxeGuDG6q1qd4x0Pc0TtXA1v5txh5I73qzFf+DY5d0hxrY2YKAzAdBSgQzKGIj7mQYxxxD',
    'ssxmod_itna2': 'QqGxBDRDcDy7D=Ye0L5YIEP7qCO=KCe7b3Dnxn9G9AKDsKFDLGQQu0AxmuMGlIQKUlhGGQ1UniwhQqUWiTEu5nA+Wo4I4O+GfTUY8/lvUGoV2eENdh1SuGg0p15WlQLU4qcgj04=twTD8vPixidqC2belGdKtTh+xAWUDYT4bImnYHpk8IrbCmdZgwihamAiFIii4vPeQSNpIyNxKMC1febKrcdKguUnlgNVDMGQeC7P9E6GfgQoNQn1tLuxsTvCSls4wgkWLozlfoWCTErMcoWxHUwyEOkOHQuRlRweV3Z/3lcbHL/Gd7/0zZrWku1R7=Fiz3Dh+dhIgzL27imGinobWTsMz2MH+3w4gzzxhDqCCkwuDpeqT1jknqoyuYCLOLehD4xF0eD7QdlG5QG7OxdWKeAxVGE=nvKYqPGDqn0F2ew4oKDWiOwsjGGlGKeL8ipxADpCxLbweaQfWAeDdbxvs+Ps9oCiq4Aed0DPlD/lqZRW4C34W9+UI50PtDWp4pK7eq0qDjKDeu79B4wSNY7W/+q=bAF0f1aA30fjOWXbihUnh6bia5VrAjb57/Djcnab5CFARtjYTDD=',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://ur.himayi.cn',
    'Referer': 'https://ur.himayi.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9pbnNpZGUzXC8iLCJhdWQiOiJodHRwOlwvXC9pbnNpZGUzXC8iLCJpYXQiOjE2ODQyNTE4OTYsIm5iZiI6MTY4NDI1MTg5NiwiZXhwIjoxNjg0MzM4Mjk2LCJtZW1iZXJfaW5mbyI6MzEyMDN9.NYCCrsaSQxhh1iqdnSw8K82NCXrnzXI0XxB6XmBzlAI',
}

json_data = {
    'goods_id': '14',
    'sort_type': 2,
    'page_size': 15,
    'page': 1,
}

while True:
    try:
        time.sleep(0.8)
        response = requests.post(
            'https://ur.himayi.cn/h5/super/api/member/getDetailsSealList',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        goods = response.json().get('data').get('data')
        print(len(goods))
        if len(goods) >= 1:
            for good in goods:
                if good.get('goods_status') != 2:
                    print('有可锁的')
                    it_id = good.get('id')
                    json_data_creat = {
                        'goods_id': 14,
                        'order_type': 3,
                        'id': it_id,
                    }
                    response = requests.post('https://ur.himayi.cn/h5/super/order/createOrder', cookies=cookies,
                                             headers=headers,
                                             json=json_data_creat)
                    try:
                        print(response.json())
                        flag = response.json().get('msg') == '点击的太快了呢,请您稍后重试!'
                        while flag:
                            time.sleep(0.3)
                            response = requests.post('https://ur.himayi.cn/h5/super/order/createOrder', cookies=cookies,
                                                     headers=headers,
                                                     json=json_data_creat)
                            flag = response.json().get('msg') == '点击的太快了呢,请您稍后重试!'
                            if not flag:
                                print(response.json())
                    except Exception as e:
                        print(e)
                        print(f'小错误:{e}')
                print('没有未锁定的')
    except Exception as e:
        print(f'大错误:{e}')
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"goods_id":"14","sort_type":2,"page_size":15,"page":1}'
# response = requests.post(
#    'https://ur.himayi.cn/h5/super/api/member/getDetailsSealList',
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
