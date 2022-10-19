# _*_ coding : utf-8 _*_
# @Time : 2022/10/19 21:14
# @Author : 金圣聪
# @File : 1.1if 案例练习
# @Project : pythonStudy

# 考察
# 控制台输入
# 强制类型转换 因为int和str不能比较

# 控制台输入年龄 如果大于18 可以去网吧
age = input('请输入你的年龄:')
if int(age) > 18:
    print('你可以去网吧了')
