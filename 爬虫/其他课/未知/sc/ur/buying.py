# _*_ coding : utf-8 _*_
# @Time : 2023/5/16 19:25
# @Author : 金圣聪
# @File : buying.py
# @Project : pythonStudy

import requests
import time
cookies = {
    'acw_tc': '7ae4df2716843012609303161e4c9e65c8fe9dc99466b5ced1692fdaea',
    'cdn_sec_tc': '7ae4df2716843012609303161e4c9e65c8fe9dc99466b5ced1692fdaea',
    'acw_sc__v2': '646465cc9b671e34b43a779fa9b28d00a5c50286',
    'PHPSESSID': '1p9iisnstm8r4gul4csmni02aj',
    'arp_scroll_position': '0',
    'ssxmod_itna': 'iq+x9Dc7it0QGQN0=DX3nqDvrqDqErSxO0Gf2mDGN4e3DZDiqAPGhDC+8zYLwSEuAtOmA4rvKvmGipxqPq2nO2tflpe0aDbqGki074iiyDCeDIDWeDiDGR=DFxYoDePNQDFWqvU1cmxWKDKx0kDY5DwZv8DYPDWxDFfgrNfcAFf=vFP/yhDiHqurDxfxG1DQ5DshDf1AKD0pSf1myCG33DEA4OqtYDvxDk3K5H54Gd66H1h1MNqARqqihNNmhnF1R4e0weKnqxVe+edGWxNGhnvyxD=cibITGDD=',
    'ssxmod_itna2': 'iq+x9Dc7it0QGQN0=DX3nqDvrqDqErSxO0Gf2DGtG9QKRRDBwDK7P4+v8HB71l8dI1TvmhemeQFvk=fOmoxe3wbBgRkTpPci66yb/PmywSeFZ3uPySG=utjDN5Q=k9264p71GsHNV=ZS+G9783q08fgKAUUIuo2YqGFjfABDMbYbxG2Cr4ZAg=4c2Twj+GPnOGtbfhax7=DeLqxD',
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
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9pbnNpZGUzXC8iLCJhdWQiOiJodHRwOlwvXC9pbnNpZGUzXC8iLCJpYXQiOjE2ODQzMDEyNjgsIm5iZiI6MTY4NDMwMTI2OCwiZXhwIjoxNjg0Mzg3NjY4LCJtZW1iZXJfaW5mbyI6MzEyMDN9.upCk0wbkr4R8f9SnoJOI9iHonK0Q04p8LJCyqXP8Ku8',
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
