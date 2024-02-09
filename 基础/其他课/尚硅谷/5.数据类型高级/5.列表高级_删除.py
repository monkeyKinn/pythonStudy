# _*_ coding : utf-8 _*_
# @Time : 2022/10/20 21:48
# @Author : 金圣聪
# @File : 5.列表高级_删除
# @Project : pythonStudy

friend = ['小美', '大美', '小黄','老黄']
# 根据下标删除
del friend[0]
print(friend)
# 删除最后一个
friend.pop()
print(friend)

# 会报错 实际用的时候要先判断再删除
# 根据元素删除
friend.remove('小黄')
print(friend)
