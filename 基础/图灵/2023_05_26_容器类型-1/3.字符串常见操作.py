my_str = "welcome to www.tulingxueyuan.com"
# 上述运行中数值`8`表示`"to"`这个字符串在原字符串的开始下标值是`8`(最低索引)
print(my_str.find("www"))
# 类似于` find()`函数，不过是从右边开始查找，返回的索引是从左边开始(最高索引)
print(my_str.rfind("to"))
# 返回` str`在`start`和`end`之间在 `my_str`里面出现的次数
print(my_str.count("w"))
print(my_str.replace('w', 'W', 1))
my_str = """welcome to www.tulingxueyuan.com
thank you
good boy"""
print(my_str)
print(my_str.splitlines())
my_str = '-'
str_list = ['welcome', 'to', 'changsha']
print(my_str.join(str_list))
