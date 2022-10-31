# _*_ coding : utf-8 _*_
# @Time : 2022/10/31 23:01
# @Author : 金圣聪
# @File : 6.编解码-get请求方式的urlencode方法.py
# @Project : pythonStudy

# 应用场景:  有多个参数的时候


import urllib.request
import urllib.parse

# url = 'https://www.baidu.com/s?wd=周杰伦&sex=男'
# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location': '中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)


base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
url = base_url + urllib.parse.urlencode(data)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    # 一定要cookie 否则百度安全验证 (截止2022年11月1日 01:48:35 暂时不验证cookie有效性(可以过期))
    'cookie': 'BAIDUID=123891A85BA85C16E5C9B5560154BA69C:FG=1; BIDUPSID=1B6A72EB557B74FFA3D56BB80DB603C2C; '
              'PSTM=1663062807; BD_UPN=13314752; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; '
              'BA_HECTOR=alal2001850g8l81252h8aqu1hi0t9e18; ZFY=SEUInM0ZuRBXFZUw1B0dlkNP:BZj3M:BZlpxlcZfdCgw8:C; '
              'BD_HOME=1; H_PS_PSSID=36558_37117_37354_37300_36885_34812_36802_36789_37145_37258_26350_37364; delPer=0; BD_CK_SAM=1; PSINO=7;'
              ' BDRCVFR[Fc9oatPmwxn]=aeXf-1x8UdYcs; '
              'BDUSS=Zpc0MwUDE5bTZ4dUdQcUIxM2Z1SnFZMEpvUGpxTlRBWTBaTjZVdlh1V0tDRWxqRVFBQUFBJCQAAAAAAQAAAAEAAACnh'
              'FosAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIp7IWOKeyFjUD;'
              ' H_PS_645EC=18db%2FxuyDIkSXG5WHmpOcEYdpAWQjJ77VSAYXPxhCINzCpt3nIF4SZssA6n9ATbCjzGM; '
              'BDSVRTM=247; baikeVisitId=e2c826a7-6934-4751-ac3d-29e118347887'
}

req = urllib.request.Request(url=url, headers=headers)
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))
