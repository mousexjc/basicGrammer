"""
    方法和属性的可见性：
        __ 开头的方法或属性为私有
        但 [__aa__] 再以 __ 结尾的,就不是私有了
        私有变量会被重命名为 _累名__变量名,其实还是可以访问到
"""


class StudentC:
    name = "student"

    def __init__(self, name):
        self.name = name
        self.__score = 0

    def setScore(self, score):
        if score < 0:
            return "ERROR:score can not <0"
        self.__score = score

    def getScore(self):
        return self.__score


stu = StudentC("张三")
# stu.__score = -1
# stu._StudentC__score = 5
print(stu.__dict__)
stu.setScore(2)
print(stu._StudentC__score)
