import requests

headers = {
    'Host'          : 'api.aichaoliuapp.cn:443',
    'User-Agent'    : 'AIEra/3.11.50 (iPhone; iOS 16.0.2; Scale/3.00)',
    'channel'       : '010100',
    'sm-deviceid'   : '6ac148944903dc85c19d7e3e16bb5453',
    'version'       : '31150',
    'session'       : 'z2KYbqTmOvNSpgpRvzxdna5BMuCAh5PdIE2apc5WbnFT2c6I3xWcxRs5CxtkcHpM',
    'sign'          : '9195e21dfa0d7d8ecc010595ef642339',
    'appName'       : 'aiera.sneaker.snkrs.shoe',
    'platform': 'ios',
    'token': 'af7a73bcbdcf49c08aba029f6d9be868',
    'timestamp': '1684902368700',
    'Accept-Language': 'zh-Hans-CN;q=1, ja-CN;q=0.9, en-CN;q=0.8',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Content-Type': 'application/json',
}

json_data = {
    'page_num': 1,
    'follow': 0,
    'page_size': 20,
}

response = requests.post('https://api.aichaoliuapp.cn:443/aiera/common/banner_index_v2/notice', headers=headers, json=json_data)
print(response.json())