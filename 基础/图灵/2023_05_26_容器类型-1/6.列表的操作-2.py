movie_names = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']

print('------删除之前------')
for name in movie_names:
    print(name)

movie_names.remove('指环王')  # 删除指定的数据

print('------删除之后------')
for name in movie_names:
    print(name)