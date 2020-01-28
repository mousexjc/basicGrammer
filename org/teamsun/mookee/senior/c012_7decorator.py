"""
    装饰器：带参数的怎么解决
"""
import time


def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


@decorator
def f0():
    print("This is function F0.")


@decorator
def f1(param):
    print("This is a function:" + param)


@decorator
def f2(param, param2):
    print("This is a function:" + param + " AND: " + param2)


f0()
print("============F0===========")
f1("F1")
print("============F1===========")
f2("F2", "F2")
print("============F2===========")
# Chapter 12 1:40


"""
    关键字参数
"""


def decorator2(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator2
def f3(param1, param2, param3, **kwargs):
    print(param1 + ":" + param2 + ":" + param3)
    print(kwargs)


f3("param1", "param2", "param3", a="va", b="vb")
