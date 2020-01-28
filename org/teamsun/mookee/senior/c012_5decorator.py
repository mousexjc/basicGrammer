"""
    装饰器：(Java的注解)
"""
import time


def f1():
    print("This is a function:f1.")


# 可用以下方式实现：但不好
def decorator(func):
    print(time.time())
    func()


decorator(f1)
print("=================1=================")
# ==================================
# 装饰器方式解决办法


def decorator2(func):

    def wrapper():
        print(time.time())
        func()

    return wrapper


new_f2 = decorator2(f1)
new_f2()
print("=================2=================")

