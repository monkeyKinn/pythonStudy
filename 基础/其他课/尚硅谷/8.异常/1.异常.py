# _*_ coding : utf-8 _*_
# @Time : 2022/10/25 23:56
# @Author : 金圣聪
# @File : 1.异常
# @Project : pythonStudy

# 读取一个不存在的文件
import json

# FileNotFoundError: [Errno 2] No such file or directory: 'text1.txt'
try:
    f = open('text1.txt', 'r')
    content = f.read()
    f.close()
    print(json.loads(content))
except FileNotFoundError:
    print('出错了')
