# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : PythonReversePath

#  HTTP请求构建
import requests
import execjs


cookies = {
    '_horizon_uid': '17d44508-46af-4276-8d02-ad827dba74b1',
    '_horizon_sid': 'e376a219-ea8f-4f55-bbdd-28dc184f55dc',
}

# 请求体
json_data = {
    'type': 'trading-type',
    'publishStartTime': '',
    'publishEndTime': '',
    'siteCode': '44',
    'secondType': 'A',
    'projectType': '',
    'thirdType': '',
    'dateType': '',
    'total': 233955,
    'pageNo': 6,
    'pageSize': 10,
    'openConvert': False,
}

ctx_headers = execjs.compile(open('./demo1.js', 'r', encoding='utf-8').read()).call('main123', json_data)
print(ctx_headers)

# 浏览器模拟
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '_horizon_uid=17d44508-46af-4276-8d02-ad827dba74b1; _horizon_sid=e376a219-ea8f-4f55-bbdd-28dc184f55dc',
    'Origin': 'https://ygp.gdzwfw.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ygp.gdzwfw.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Dgi-Req-App': 'ggzy-portal',
    'X-Dgi-Req-Nonce': ctx_headers['X-Dgi-Req-Nonce'],
    'X-Dgi-Req-Signature': ctx_headers['X-Dgi-Req-Signature'],
    'X-Dgi-Req-Timestamp': str(ctx_headers['X-Dgi-Req-Timestamp']),
}

response = requests.post('https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v1/items', cookies=cookies, headers=headers, json=json_data).json()
print(response)

