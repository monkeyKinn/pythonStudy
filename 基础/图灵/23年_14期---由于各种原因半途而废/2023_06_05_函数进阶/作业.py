# -*- coding: utf-8 -*-

"""
@Time : 2023/6/6 23:22
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

""""
第一题
    对于函数 的传参来说 *和**的 区别 是？
    A. 都是接收额外参数
    B. 二者只是称呼上有些不同 其实没有什么区别
    C. 前者接收多余的普通参数形成字典 后者接收键值形式的参数形成元组
    D. 前者接收多余的普通参数形成元组 后者接收键值形式的参数形成字典
答: D

第二题
    关于函数的参数使用限制，以下选项中描述 错误 的是（ ）
    A.关键字参数必须位于位置参数之前
    B.关键字参数必须位于位置参数之后
    C.关键字参数顺序无限制
    D.位置形参限制了实参的传参个数
答: A

第三题
    定义一个函数，可以完成以下国家汇率的计算，要求输入是各国的金额，输出的是中国人民币的金额
    各国汇率如下：美元6.84，欧元8.12，日元0.06，港元0.88，澳元4.98
    例如输入美元，金额100，兑换成人民币是100*6.84=684元
"""


def currency_converter(money, country='澳元'):
    if country == '美元':
        return money * 6.84
    elif country == '欧元':
        return money * 8.12
    elif country == '日元':
        return money * 0.06
    elif country == '港元':
        return money * 0.88
    else:
        return money * 4.98


if __name__ == '__main__':
    country = input('请输入需要计算的汇率标准(美元/欧元/日元/港元/默认澳元): ')
    money = float(input('请输入需要计算的汇率标准(美元/欧元/日元/港元/默认澳元): '))
    result = currency_converter(money, country)
    print(f'换成人名币为: {result} 元')
