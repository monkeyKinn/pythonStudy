# _*_ coding : utf-8 _*_
# @Time : 2022/11/17 23:18
# @Author : 金圣聪
# @File : 13.微博的cookie登录
# @Project : pythonStudy


import urllib.request
import gzip

# 场景:在数据采集的时候绕过登录
# url = 'https://weibo.cn/5917156804/info' #注意  这是老版的微博域名
url = 'https://m.weibo.cn/users/5917156804?set=1'
headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 因为做了压缩 所以一定要加上
    'accept-encoding': 'gzip, deflate, br',
    'cookie': '',
    # 做防盗链  判断当前路径是不是由上一个路径进来的 一般情况下做的图片防盗
    'referer': 'https://weibo.cn/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url=url, headers=headers)
resp = urllib.request.urlopen(req)

# content = resp.read().decode('utf-8') # 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte 说明要用gizp包
content = resp.read()
res = gzip.decompress(content).decode("utf-8")
# 将数据保存到本地
with open('weibo-old.html', 'w', encoding='utf-8') as f:
    f.write(res)
