# _*_ coding : utf-8 _*_
# 1. 头部参数加密模拟生成:
# http://webapi.cninfo.com.cn/#/marketDataDate  mcode加密
# 交给何老师企业微信
# @Time : 2023/4/12 0:01
# @Author : 金圣聪
# @File : 1.py
# @Project : pythonStudy

import requests
import execjs


cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1681226697',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1681227385',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1681226697; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1681227385',
    'Origin': 'http://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# 添加字典,
# todo 从js中解密获取
# headers['mcode'] = 'MTY4MTIyODkwMQ=='
mcode = execjs.compile(open('1.js', 'r', encoding='utf-8').read()).call('getMcode')
headers['mcode'] = mcode

print(f'mcode: {mcode}')

data = {
    'tdate': '2023-04-10',
    'market': 'SZE',
    'scode': '399001',
}

response = requests.post(
    # 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007',
    'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1015',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False
)

print(response.json())