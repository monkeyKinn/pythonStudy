# _*_ coding : utf-8 _*_
# @Time : 2022/10/20 21:25
# @Author : 金圣聪
# @File : 2.列表高级_添加
# @Project : pythonStudy


# append 在末尾添加元素
# insert 在指定位置插入元素
# extend 合并两个列表

# 1.append 在末尾添加元素
food = ['铁锅炖大鹅', '酸菜五花肉']
print(food)
food.append('小鸡炖蘑菇')
food.append(521)
print(food)

# insert 在指定位置插入元素
char = ['a', 'c', 'd']
char.insert(1, 'b')
print(char)

# extend 合并两个列表
food.extend(char)
print(food)
