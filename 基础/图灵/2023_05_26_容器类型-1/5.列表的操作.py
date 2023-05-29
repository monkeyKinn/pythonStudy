# 定义列个表存储3个学生的姓名
stu_names = ['张三','李四','王五']
print("-----添加之前，列表的数据-----")
for name in stu_names:
    print(name)

# 提示、并添加元素
temp = input('请输入要添加的学生姓名:')
stu_names.append(temp)

print("-----添加之后，列表的数据-----")
for name in stu_names:
    print(name)