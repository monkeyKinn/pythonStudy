# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 21:14
@Author : 金圣聪
@File : 9.字典操作.py
@Project : pythonStudy
"""

my_info = {
    'name': 'jsc',
    'age': 18,
    'home': '长沙'
}

# 写入的key不存在会报错
# print(my_info['qq'])


# 这样就不会错了
# 在字典对象中,可以使用get方法获取key对应的值,如果key不存在,默认返回None。可以更改
print(my_info.get('QQ', '当前信息不存在'))

'''
数据修改
'''
info = {
    'name': 'jsc',
    'age': 18,
    'gender': '男',
    'home': '南京'
}
info['gender'] =  '男'
print(info)

'''
数据插入
'''
info['mobile'] = 18111111111
print(info)

'''
数据删除
'''
info.clear()
print(info)
# 不能使用了,直接是删除了这个对象
del info

data = dict()
print(type(data))