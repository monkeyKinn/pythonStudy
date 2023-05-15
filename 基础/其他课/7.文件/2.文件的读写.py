# _*_ coding : utf-8 _*_
# @Time : 2022/10/25 0:16
# @Author : 金圣聪
# @File : 2.文件的读写
# @Project : pythonStudy

# 写数据
# f = open('txt.txt', 'w')
# f.write('i am here\n' * 5)
# f.close()
#
# # 如果再次运行会打印几次(会覆盖不?) a不会覆盖会追加
# fp = open('txt.txt','a')
# fp.write('iamBatMAm\n'*10)
# fp.close()

# 读数据
fp = open('txt.txt', 'r')
# 默认情况下,read是一个字节一个字节读
# content = fp.read()
# print(content)
# readline是一行一行读,但是每次只能一行
# content = fp.readline()
# print(content)
# readlines按照行来读取,会将所有的数据都读取到,然后变成一个列表作为返回
# 列表中的元素是一行一行的数据
content = fp.readlines()
print(content)
