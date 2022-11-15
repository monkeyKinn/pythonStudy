# _*_ coding : utf-8 _*_
# @Time : 2022/11/15 23:49
# @Author : 金圣聪
# @File : 11.ajax的post请求肯德基餐厅
# @Project : pythonStudy

# 第1页: http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname:杭州
# pid:
# pageIndex:1
# pageSize:10

# 第2页: http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname:杭州
# pid:
# pageIndex:2
# pageSize:10

# 需求: 前十页杭州餐厅

import urllib.request
import urllib.parse


def get_resp(data: dict) -> str:
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    # post请求 编码
    data_encode = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }
    # 定制化请求对象

    req = urllib.request.Request(url=base_url, data=data_encode, headers=headers)
    resp = urllib.request.urlopen(req)
    return resp.read().decode('utf-8')


if __name__ == '__main__':
    start_page = int(input('请输入开始页码: '))
    end_page = int(input('请输入结束页码: '))
    data_list = []
    # 循环构建参数
    for pageIndex in range(start_page, end_page + 1):
        data = {
            'cname': '杭州',
            'pid': '',
            'pageIndex': pageIndex,
            'pageSize': 10
        }
        data_list.append(data)
    # 循环调用方法
    for (data) in data_list:
        resp = get_resp(data)

        with open('KFC_CT/kfc_ct_' + str(data_list.index(data)) + '.json', 'w', encoding='utf-8') as f:
            f.write(resp)
            f.close()
