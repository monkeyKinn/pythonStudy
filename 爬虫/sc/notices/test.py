import requests
from bs4 import BeautifulSoup
import ast

cookies = {
    'USER-TOKEN': 'd8OLe1gxt40bQ9oVtgLOCoormmr0nrsGftpadgVSqK0=',
}

headers = {
    'authority': 'info.18art.art',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'USER-TOKEN=d8OLe1gxt40bQ9oVtgLOCoormmr0nrsGftpadgVSqK0=',
    'if-modified-since': 'Fri, 28 Apr 2023 06:53:29 GMT',
    'if-none-match': '"9F226414FEF9D5962040E14D7E26C970"',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

response = requests.get('https://info.18art.art/html/infor/infor.html', cookies=cookies, headers=headers)
response.encoding = "UTF-8"
soup = BeautifulSoup(response.text, 'html.parser')
inject_json_str = soup.findAll('script')[2].text.split(';')[1].strip().replace('window.__injectJson=', '')
inject_json = ast.literal_eval(inject_json_str)
# 通知列表
notices_list = inject_json['noticeList']
print(notices_list)