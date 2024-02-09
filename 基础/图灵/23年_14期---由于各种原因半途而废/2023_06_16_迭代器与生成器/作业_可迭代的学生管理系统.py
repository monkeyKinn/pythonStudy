class StudentSystem:
    """
    学生管理系统(可迭代版)
    """

    def __init__(self):
        self.stu = list()
        self.current = 0

    def add(self):
        name = input('请输入学生名字: ')
        gender = input('请输入学生性别: ')
        age = input('请输入学生年龄: ')
        dict_stu = dict()
        dict_stu['name'] = name
        dict_stu['gender'] = gender
        dict_stu['age'] = age
        self.stu.append(dict_stu)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.stu):
            stu = self.stu[self.current]
            self.current += 1
            return stu
        else:
            raise StopIteration


student_sys = StudentSystem()
student_sys.add()
student_sys.add()
student_sys.add()

# for student_sy in student_sys:
#     print(student_sy)

# 推导式变成列表
stu_list = [x for x in student_sys]
print(stu_list)