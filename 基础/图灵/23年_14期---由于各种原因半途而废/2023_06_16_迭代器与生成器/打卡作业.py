"""
第一题
    以下代码的打印结果
    def func(a):
        a = a + 4
        yield a
        a = a - 8
        yield a
    g=func(26)  --->遇到yield停在第六行
    res1=next(g) --->获取值,所以是30
    print(res1)  ---所以是30
    res2=next(g) --->下一个,停在第八行
    print(res2)  --->所以是30-8=22

答: 30
    22
"""

"""
第二题
定义一个生成器，这个生成器可以生成 1到10的奇数
解析:
    当序列过长， 而每次只需要获取一个元素时，应当考虑使用生成器表达式而不是列表解析
    生成器表达式的语法和列表解析一样，只不过生成器表达式是被()括起来的，而不是[]
"""
print('No.2')
# 定义的生成器
gen = (i for i in range(11) if i % 2)
# <generator object <genexpr> at 0x00000291CC4304A0>,说明是一个生成器对象
print(gen)

# 遍历元素
# for i in gen:
#     print(i, end=' ')
# print()
# print([i for i in gen])

print(hasattr(gen, "__iter__"))  # True,有iter方法
print(hasattr(gen, "__next__"))  # True,有next方法

# 使用sum求和,或者for遍历(32-36行试验得出结论)之后, 会导致再次迭代所获取的值为空
print(sum(gen))
print([i for i in gen])
print()
# 答:  综上 ,定义的生成器在第28行,所需要注意点如上代码


"""
第三题
定义一个生成器，这个生成器可以生成 1 2  4 5 6  9 10
"""
print('No.3')
gen_3 = (i for i in range(1, 11) if i not in [3, 7, 8])
for i in gen_3:
    print(i, end=' ')
print()
# 再次验证: for遍历之后, 会导致再次迭代所获取的值为空
print([i for i in gen_3])
