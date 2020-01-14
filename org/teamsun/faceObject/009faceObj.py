"""
    面向对象：类/对象
    1/ class 关键字定义类
    2/ 建议首字母大写，驼峰格式
    3/ 可用[()] 定义参数，后接[:]
    4/ 使用类前，先实例化:类名()
    5/ 类的内部不能调用自己的方法
"""


class Student:
    # 类变量
    sum = 0
    name = "学生"
    age = 7

    #  类中的方法必须有默认参数[self]
    def student_print(self):
        print("我是" + self.name)
        print("我" + str(self.age) + "岁")

    # 构造函数: 自动调用
    def __init__(self, name, age):
        print("Student __init__ runs~")
        # 实例变量：self.
        self.name = name
        self.age = age
        Student.sum += 1


stu_zs = Student("张三", 18)
print(stu_zs.__dict__)
print(Student.__dict__)
print(stu_zs.__class__.sum)
