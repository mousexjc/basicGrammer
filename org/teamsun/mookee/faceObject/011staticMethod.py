"""
    静态方法：类和对象都可以调用静态方法
    和普通的函数没什么区别
"""


class StudentB:

    param1 = "param1"

    def __init__(self):
        pass

    # 加  @staticmethod 装饰器即可
    @staticmethod
    def testStaticMethod(stra):
        print("This is a static method:" + stra)


stu = StudentB()
stu.testStaticMethod("object")
StudentB.testStaticMethod("class")
