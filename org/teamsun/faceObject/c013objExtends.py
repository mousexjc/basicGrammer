"""
    面向对象的3大特性：
        封装，继承，多态
"""
from org.teamsun.faceObject.c013father import People


class StudentD(People):
    score = 0

    def __init__(self, school, name, sex):
        self.school = school
        super().__init__(name, sex)

    def do_homework(self):
        print("I am doing homework at " + self.school)
        # super().eat()

    def eat(self):
        print("I am eating school foods~")


stu = StudentD("一小", "张三", "男士")
stu.do_homework()
stu.eat()
