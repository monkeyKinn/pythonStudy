# -*- coding: utf-8 -*-

"""
@Time : 2023/5/18 21:34
@Author : 金圣聪
@File : 0.作业.py
@Project : pythonStudy
"""

""""
第一题
    Python是由谁发明的一种编程语言?
答:	吉多·范罗苏姆
第二题
    Python有应用领域（回答5种）
答:	1.爬虫
    2.大数据
    3.web开发
    4.人工智能
    5.自动化测试/办公等...
第三题
    python有哪几种数据类型?
答:	1.String
    2.Bool
    3.number
        3.1.    int
        3.2.    float(注意,区别于java,py没有double)
        3.3.    long
        3.4.    complex(复数; 注意,区别于java,java没有complex)
    4.Tuple(元组,区别于java)
    5.Dictionary(区别于java)
    6.List
    7.Set
第四题
    查看变量类型的 Python 内置函数是?
答:	type()
第五题
    代码 print(type([1,2])) 输出结果为?
答:  <class 'list'>
第六题
    表达式 3 ** 2 的值为?
答:	即3的平方2 = 9
第七题
    下面代码的运行结果是
    a = 10
    a *= 10
    print(a)
答:	即:a=a*10=10*10
    =100
第八题
    下面代码的运行结果是
    print(9//2)
答:	4
第九题
    下面代码的运行结果是
    print(3*1**3)
答: 即3*(1^3) = 3 * 1 = 3
第十题
    定义两个字符串，str1='HELLO', str2='我是来自火星的火星人'，然后进行以下操作：
    将2个字符串进行拼接为一句话(一个字符串)，中间用逗号隔开。
    怎样得出结果：HELLO,我是来自火星的火星人                 这个字符串
答:
    str1='HELLO'
    str2='我是来自火星的火星人'

    # 因为通过肉眼可见的原因可知,str1和str2两个字符串长度不超过20,所以,
    # 从效率角度,可以直接用+号拼接;
    # 如果长度超过20,可以用join方法提高效率,
    # 当然,f''格式化输出也行

    result = str1 + ',' + str2
    print('This Str must be: ' + result)
"""