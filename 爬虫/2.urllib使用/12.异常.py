# _*_ coding : utf-8 _*_
# @Time : 2022/11/17 23:02
# @Author : 金圣聪
# @File : 12.异常
# @Project : pythonStudy

import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/hh867308122/article/details/1275394191'
url = 'https://www.sb.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

req = urllib.request.Request(url=url, headers=headers)
try:
    resp = urllib.request.urlopen(req)
    content = resp.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError as e:
    print('系统正在升级')
except urllib.error.URLError as e:
    print('无响应')


