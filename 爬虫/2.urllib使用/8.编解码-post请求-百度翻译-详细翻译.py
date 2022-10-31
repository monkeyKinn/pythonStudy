# _*_ coding : utf-8 _*_
# @Time : 2022/11/1 0:06
# @Author : 金圣聪
# @File : 8.编解码-post请求-百度翻译-详细翻译.py
# @Project : pythonStudy
import urllib.request
import urllib.parse
import json
# 安装 execjs 库,用于执行js代码
import execjs
import traceback

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
key = 'do love'

headers = {
    # 'Accept': '*/*',
    # # 不能有
    # # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Acs-Token': '1667199837498_1667232271123_UNE9tDg+8urThUE6Uf0M+E89AFMvu7JHbaxaDxfSaipFF+7GhvBHb/EFoSxWVICAerY8jGNKz7gCOKe5/pTMirSb1Bo5aV/bZA4uBpl8b7EHd2LWVxfEX7GtlIFVBuls1fZFUZ7MQC9yyvc5Lix4jUTozuMQfh5S6YIQuaIQOJ2gN8vbtT9izFrhnp4/jVkYQ3ncjd6KkOUtmySM35i0y5M3aa3xj4fJdaAAKXJzEv5VQNALt7Vzh2o2AZwKIkK88+WAAdizc754p19r1uMCI3RxJVCdx1XyzIpprPkS0hCFtRCNaK2FdYqooFnM0BH8',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '167',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    # 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',

    # 一定要要cookie 防止百度安全验证
    # 只有这里会验证cookie有效性 (不能是过期的)
    'Cookie': '你的cookie'
}
# 打开解密文件
# 文件来源:
# https://blog.csdn.net/Dinner_Python/article/details/106787816
fp = open('js/baidufanyi.js', 'r')
js_data = fp.read()
# 关闭资源
fp.close()
# Python执行js用execjs就可以了。
# e是js文件中的函数名字
sign = execjs.compile(js_data).call("e", key)
print(f'sign: {sign}')

load_data = {
    # 'from': 'zh',
    'from': 'en',
    'to': 'zh',
    'query': key,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': sign,
    'token': '5b4d3d0776f177cefb30c38f6aa8b597',
    'domain': 'common'
}
# data编码
req_data = urllib.parse.urlencode(load_data).encode('utf-8')
# 请求对象的定制
req = urllib.request.Request(url=url, data=req_data, headers=headers)
# 发起请求
resp = urllib.request.urlopen(req)
# 读并解码获取响应
content = resp.read().decode('utf-8')
# 响应转换成json
json_content = json.loads(content)
print('\n-----')
print(json_content)
print('-----\n')


try:
    # 因为没有cookie/sing解密可能会失败
    print(json_content.get('trans_result').get('data')[0].get('dst'))
except Exception as e:
    print(f'解析失败{e}\n')
    print(f'errno:{str(json_content.get("errno"))}',
          f',errmsg:{json_content.get("errmsg")}')
    # traceback.print_exc()
