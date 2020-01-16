"""
    闭包：函数 + 环境变量
    Python 一切皆可视为对象
    意义：保存一个环境。（保存了环境调用当时的现场）
    环境变量：会常驻内存，容易引起内存泄漏。小心使用
"""


def methoda_pre():
    a = 5
    b = 10

    def methoda(x):
        return (a + b) * x

    return methoda


m = methoda_pre()
print(m(5))
print(m.__closure__)
# 获取环境变量
print(m.__closure__[0].cell_contents)
print(m.__closure__[1].cell_contents)
print("=================================")


def f1():
    a = 10

    def f2():
        # 此处的a是局部变量，不会影响外部变量的值
        # 且再次负值的话不会被认为是闭包了
        a = 20
        b = 4
        print(a)

    print(a)
    f2()
    print(a)
    return f2


m = f1()
print(m.__closure__)
