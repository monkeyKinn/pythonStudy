# _*_ coding : utf-8 _*_
# @Time : 2022/11/18 0:14
# @Author : 金圣聪
# @File : 14.微博的cookie登录新版
# @Project : pythonStudy
import urllib.request
import urllib.parse

base_url = 'https://weibo.com/ajax/friendships/friends?'
headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 因为做了压缩 所以一定要加上
    'cookie': '',
    # 做防盗链  判断当前路径是不是由上一个路径进来的 一般情况下做的图片防盗
    'referer': 'https://weibo.com/u/page/follow/5917156804',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
data = {
    'uid': 5917156804,
    'relate': 'fans',
    'count': 20,
    'page': 1,
    'type': 'fans',
    'fansSortType': 'followTime'
}
url = base_url + urllib.parse.urlencode(data)

req = urllib.request.Request(url=url, headers=headers)
resp = urllib.request.urlopen(req)
content = resp.read().decode('utf-8')
with open('weibo-new.json', 'w', encoding='utf-8') as f:
    f.write(content)
