# _*_ coding : utf-8 _*_
# @Time : 2022/11/8 23:31
# @Author : 金圣聪
# @File : 9.ajax的get请求豆瓣电影前十页
# @Project : pythonStudy

import urllib.request
import urllib.parse


# urllib.request.Request()
#
# 3.下载数据

# 定制请求对象
def customize_req(page):
    print(f'正在读取第{page}页数据...')
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': 20 * (page - 1),
        'limit': '20'
    }
    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }
    try:
        return urllib.request.Request(url=url, headers=headers)
    except Exception as e:
        print(f'customizeReq error,error is {e}')
    finally:
        print(f'读取第{page}页数据...完成...\n')


def get_content():
    resp = urllib.request.urlopen(req)
    return resp.read().decode('utf-8')


# 程序入口
if __name__ == '__main__':
    start_page = int(input('起始页码'))
    end_page = int(input('结束页码'))

    content_list = '['
    # [1,10+1)才是1-10页
    for page in range(start_page, end_page + 1):
        # 1.每一页 请求对象的定制
        req = customize_req(page)
        # 2.获取响应数据
        content = get_content()
        # 2.1.这里做优化 保存到一个文件里
        if page != end_page:
            content += ','
        else:
            content += ''
        content_list += content
        if page == end_page:
            content_list += ']'
    # 3.保存到文件
    with open('top10pageDouban.json', 'w', encoding='utf-8') as f:
        f.write(content_list)
    f.close()
print("success~")
