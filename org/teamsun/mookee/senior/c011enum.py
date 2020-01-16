"""
    枚举: 继承 Enum
    name 不能重复
    value 可重复，但被认为是第一个同名的别名，不被视为独立的枚举
            可通过 Enum.__members__ 遍历

    A：Enum : 不限制value 的类型
    B：IntEnum : value 必须是int 型
    C：@unique 加这个装饰器之后，值不能重复
    D: Enum是单例模式，不能实例话
"""
from enum import Enum


class QQVIP(Enum):
    # 枚举的标识最好大写
    YELLOW = 1
    RED = 2
    GREEN = 3
    BLACK = 4


print(QQVIP)
print(type(QQVIP.BLACK.name))
print(QQVIP.BLACK.name)
print(type(QQVIP.BLACK.value))
print(QQVIP.BLACK.value)
print(QQVIP["RED"])

"""
    枚举类可以遍历
"""
for a in QQVIP:
    print(a)
    print(a.value)
    if a == QQVIP.GREEN:
        print("haha~ GREEN")


class QQVIP2(Enum):
    YELLOW_NEW = 1
    RED_NEW = 2
    GREEN_NEW = 2


print("================")
for a in QQVIP2:
    print(a)
    print(a.value)

print("================")
for a in QQVIP2.__members__:
    print(a)
    print(QQVIP2[a])
    print(QQVIP2[a].name)
    print(QQVIP2[a].value)

print(QQVIP(2))
