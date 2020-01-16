"""
    父类
"""


class People:
    sex = "male"
    name = "people"

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def eat(self):
        print(self.name + "I am eating!!!")
