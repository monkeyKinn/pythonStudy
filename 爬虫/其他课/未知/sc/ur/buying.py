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
    'PHPSESSID': 'k6kqn4kp3gj93tg3fosbdk4cth',
    'acw_sc__v2': '6463ac0a337330a7954a199374532ecdcda07c53',
    'arp_scroll_position': '44',
    'ssxmod_itna': 'euD=qRODCG83G=DXtRxCaDRn8D7nKniim35DBkAr4iNDnD8x7YDvm+dFlmnDVFDBKWsDQwm+xkG44mhoH9CA5WlIDB3DEx06+8jQxiicDCeDIDWeDiDGb=DFxYoDePNQDFWqvU1cmxWKDKx0kDY5DwZv8DYPDWxDFfam5MAFwOE9COaBs54D1P=5xfxG1DQ5DscDfzAKD0pSfzmyChbDDEG4OqtYDvxDk3KyF54Gd66H1h1kNPG+KPYxN8jGnahm4SeeKzQiNoPe4zWnxsg=NvqiTlWZD4D=',
    'ssxmod_itna2': 'euD=qRODCG83G=DXtRxCaDRn8D7nKniimiDAqA=ND/txKwohcq7PGOUcfh3ULphGcDCSBgLKGkbbq7mw9ec72iviGfW7WNoLEO2XxG3WaCyXVFnRIIq5TvexT+6o9M5mmDFqG7zeD===',
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
                        print(response.json())
                        flag = response.json().get('msg') == '点击的太快了呢,请您稍后重试!'
                        while flag:
                            # time.sleep(0.001)
                            response = requests.post('https://ur.himayi.cn/h5/super/order/createOrder', cookies=cookies,
                                                     headers=headers,
                                                     json=json_data_creat)
                            flag = response.json().get('msg') == '点击的太快了呢,请您稍后重试!'
                            if not flag:
                                print(response.text)
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
