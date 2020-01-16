"""
    闭包例子
    旅行者：x,y
    x = 0
    步数  总步数
    3     3
    5     8
    6     14
"""

# Type 1 ：类的方式
print("Type 1 ============================")


class Step:
    origin = 0

    def goStep(self, steps):
        self.origin += steps
        return self.origin


step = Step()
print(step.goStep(3))
print(step.goStep(5))
print(step.goStep(6))

# Type 2
print("Type 2 ============================")
origin = 0


def goStep(steps):
    # 尽量不使用全局变量
    global origin
    newPos = origin + steps
    origin = newPos
    return origin


print(goStep(3))
print(goStep(5))
print(goStep(6))

# Type 3 :闭包的方式
print("Type 3 ============================")


def factory(pos):

    def gostep2(steps):
        nonlocal pos
        pos += steps
        return pos

    return gostep2


s = factory(0)
print(s(3))
print(s.__closure__[0].cell_contents)
print(s(5))
print(s.__closure__[0].cell_contents)
print(s(6))
print(s.__closure__[0].cell_contents)
