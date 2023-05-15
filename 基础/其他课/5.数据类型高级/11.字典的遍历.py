# _*_ coding : utf-8 _*_
# @Time : 2022/10/24 0:00
# @Author : 金圣聪
# @File : 11.字典的遍历
# @Project : pythonStudy

# 将数据一个一个输出
person = {'name': '老金', 'age': 18, 'gender': True}

# 1.遍历字典的key,遍历所有的key
for key in person.keys():
    print(key)
print()
# 2.遍历字典的value,遍历所有的value值
for value in person.values():
    print(value)
print()
# 3.遍历字典的key-value
for (key, value) in person.items():
    print(key, value)
print()
# 4.遍历字典的项(元素)
for item in person.items():
    print(item)
