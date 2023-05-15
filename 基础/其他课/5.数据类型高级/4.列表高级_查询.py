# _*_ coding : utf-8 _*_
# @Time : 2022/10/20 21:40
# @Author : 金圣聪
# @File : 4.列表查询
# @Project : pythonStudy
friend = ['小美', '大美', '小黄']
print(friend)
people = input('请输入你想要的人:')
isExist = people in friend
print('是否存在%s' % isExist)


people = input('请输入你想要的人:')
isNot = people not in friend
if isNot:
    print('不存在')
