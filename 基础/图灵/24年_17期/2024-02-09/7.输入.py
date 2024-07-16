"""
使用python进行模拟账号登录
"""
from datetime import datetime

local_name = "金圣聪"
local_pwd = 123
user_name = input('请输入用户名: ')
user_pwd = input('请输入密码: ')
# print(user_name)
# print(type(user_name))  # str
if user_name == local_name and local_pwd == int(user_pwd):
    # now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"恭喜 {user_name},登录成功!密码为:{user_pwd},时间:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    print("fail")
"""
input是py提供的用于接收用户输入信息的功能
    input接收的是用户在键盘上输入的
    input接收的的类型永远是一个字符串
"""
