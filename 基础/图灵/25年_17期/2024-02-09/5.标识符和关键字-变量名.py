"""
标识符:
    在py中,自己定义的一些变量名称,称为标识符,py中,有大小写之分
在py中创建标识符的规则
    由字母,数字, 下划线 组成,数字不能最为标识符开头
命名规则:
    见名知意
    驼峰命名
        大驼峰
        小驼峰

    下划线命名
在py中,变量名用下划线
类名用大驼峰
全局变量全是大写,并且用下划线连接
"""
print("----------------------")
"""
    关键字是py中已经定义好的一些特殊含义的单词
    这些单词不能用作自己修饰符的创建
"""

import keyword

print(keyword.kwlist)  # 打印关键字
""""
[
    'False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert',
    'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
    'return', 'try', 'while', 'with', 'yield'
]
"""
