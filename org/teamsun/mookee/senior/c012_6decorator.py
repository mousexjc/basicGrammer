"""
    装饰器：@ 方式调用
    保持原来调用方式不变,体现了 AOP 的编程思想
"""
import time


def decorator(func):

    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def f1():
    print("This is a function:f1.")


f1()
