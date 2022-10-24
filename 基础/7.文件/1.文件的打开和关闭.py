# _*_ coding : utf-8 _*_
# @Time : 2022/10/24 23:42
# @Author : 金圣聪
# @File : 1.文件的打开和关闭
# @Project : pythonStudy

# 创建一个文件
# 文件路径必须要写
# 文件模式:
#     w 可写
#     r 可读
# open('text.txt','w')
# 打开文件(没有则创建)
f = open('text.txt', 'w')
# 写内容
f.write('helloWorld')
# 文件关闭
f.close()
# 注意一定要有文件夹,
g = open('text/text.txt', 'w')
g.write('folderWrite')
# 文件关闭
g.close()
