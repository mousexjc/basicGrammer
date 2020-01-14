"""
    函数 Chapter 8
"""
param = 1.12345678
b = round(param, 4)
print(b)
print(round(param, 2))


def print_a():
    print("Hello ,My First function~")


print_a()


def myAdd(a, b):
    print("a=", a)
    print("b=", b)
    return a + b


print(myAdd(2, 4))

print(myAdd(b=3, a=2))


def myFunction(name, age=13, sex="男孩"):
    print("我叫" + name)
    print("我今年" + str(age))
    print("我是" + sex)


myFunction("张三", 20, "女孩")
myFunction("李四", 20, sex="女孩")
