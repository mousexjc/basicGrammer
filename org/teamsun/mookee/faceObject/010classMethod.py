"""
    类方法
"""


class StudentA:
    sum = 0
    name = "学生"

    def __init__(self, name):
        self.name = name

    # 类方法/ @：装饰器
    @classmethod
    def add(cls):
        cls.sum += 1
        print("当前学生总数:" + str(cls.sum))


stu = StudentA("Jacky")
StudentA.add()
# 对象也可以调用类方法,不建议这样调用
stu.add()
print(stu.__dict__)
print(StudentA.__dict__)
