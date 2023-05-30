# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 23:21
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""
"""
第一题
    以下代码的运行结果是
    n = 'world'
    print(n[3])
答: l

第二题
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(number[3])
    print(number[3:5])
答: 4
    [4,5]
  
第三题
    L = ['a','b','c','a']
    统计列表L中'a'字符串出现的个数
答: print(L.count('a'))


第四题
    L = ['a','b','c','d']
    删除列表中最后一个元素
答: L.pop()

第五题

    numbers = ['a', 1, 'b']
    统计列表numbers有多少元素
答: len(numbers)

第六题

    往以下列表list_data末尾追加一个元素'a' (字符串)
    list_data = [1, 2, 3]
答: list_data.append('a')

第七题

    msg = 'hello python'
    把字符串msg的python字符提取出来
答: msg[msg.find('python'):]

第八题
    list1 = ['真正的勇士','敢于直面惨淡的人生','敢于正视淋漓的鲜血']
    利用字符串方法把list1里面的字符串拼接成以下字符串
    '真正的勇士,敢于直面惨淡的人生,敢于正视淋漓的鲜血'
答: result = ','.join(list1)

第九题

    定义一个列表，列表中的元素有'安琪拉','妲己','韩信','典韦','吕布'五个元素，然后进行以下操作：

    1.末尾追加两个元素，'小乔','貂蝉'
    2.查找'妲己'的索引
    3.删除'韩信'
    4.将最后一个元素修改为'白起'
"""
list = ['安琪拉', '妲己', '韩信', '典韦', '吕布']
# 1.末尾追加两个元素，'小乔','貂蝉'
# list.append('小乔')
# list.append('貂蝉')
list.extend(['小乔', '貂蝉'])
# 2.查找'妲己'的索引
dj_index = list.index('妲己')
print(dj_index)
# 3.删除'韩信'
list.remove('韩信')
print(list)
# 4.将最后一个元素修改为'白起'
list[-1] = '白起'
print(list)
