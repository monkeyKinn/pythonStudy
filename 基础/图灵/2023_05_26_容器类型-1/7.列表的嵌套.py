import random

# 定义一个列表用来保存3个办公室
offices = [[], [], []]

# 定义一个列表用来存储8位老师的名字
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 遍历所有的老师，随机安排到0、1、2号办公室
for name in names:
    random_num = random.randint(0, 2)
    offices[random_num].append(name)

print(offices)
print("*"*10)
i = 1
for office_names in offices:
    print('办公室%d的人数为:%d' % (i, len(office_names)))
    i += 1
    for name in office_names:
        print("%s" % name, end=' ')
    print("\n")
    print("-" * 20)