# _*_ coding : utf-8 _*_
# @Time : 2022/10/19 22:09
# @Author : 金圣聪
# @File : 1.字符串高级
# @Project : pythonStudy

# len() 判断长度 字符串/列表元组等等
s = 'china'
print('长度为:%d' % len(s))
print()

# str.find('字符') 查找是否村在存在返回第一次出现的下标,不存在返回-1
s1 = 'chinai'
print('c出现的下标: %d' % s1.find('z'))
print()

s2 = 'china'
print(s2.startswith('C'))
print(s2.endswith('a'))
print()

s3 = 'aaabb'
print(s3.count('a', 0, 1))
print(s3.count('a'))
print()

s4 = 'aaabb'
print(s4.replace('a', 'c', 1))

s5 = '1#2#3#4'
print(s5.split('#'))

s6 = 'china'
s6 = s6.upper()
print(s6)
print(s6.lower())

s7 = '  12 3  '
print(s7)
print(s7.strip())

s8 = 'a'
print(s8.join('字符串'))