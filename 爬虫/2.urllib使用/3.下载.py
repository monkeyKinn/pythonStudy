# _*_ coding : utf-8 _*_
# @Time : 2022/10/28 21:40
# @Author : 金圣聪
# @File : 3.下载
# @Project : pythonStudy
import traceback
import urllib.request

url = 'http://www.baidu.com'

# 1.网页下载

# 网址检索,返回一个元组，其中包含新创建的数据文件的路径以及生成的 HTTPMessage 对象。
# url:下载路径, filename 文件名
# 在py中可以写变量的 名字,也可以直接写值
tuple_resp = urllib.request.urlretrieve(url, 'baidu.html')
# ('baidu.html', <http.client.HTTPMessage object at 0x000001E53C0613D0>)
print(tuple_resp)

# 2.图片下载
img_url = "https://pbs.twimg.com/media/FgJRtvKUYAEMbKH?format=jpg&name=large"
try:
    tuple_resp_img = urllib.request.urlretrieve(filename='yua_mikami.jpg', url=img_url)
    # ('yua_mikami.jpg', <http.client.HTTPMessage object at 0x000001E53C061460>)
    print(tuple_resp_img)
except Exception as e:
    print(f'problem is {e}')
    traceback.print_exc()

# 3.视频下载
view_url = 'https://vd2.bdstatic.com/mda-njqpsgtjp53qbvc3/cae_h264/1666722546608557255/mda-njqpsgtjp53qbvc3.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1666971142-0-0-6d36a7a79b24bbc9c2b961f9961a4abc&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0141935138&vid=7973159718388296463&abtest=104959_1-105227_2&klogid=0141935138'

tuple_resp_view = urllib.request.urlretrieve(filename='view.mp4', url=view_url)
# ('view.mp4', <http.client.HTTPMessage object at 0x000001E53C061D90>)
print(tuple_resp_view)
