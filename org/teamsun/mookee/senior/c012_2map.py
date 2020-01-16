"""
    Chapter 12 函数式编程
    高阶函数 : map
    结合 lambda表达式
"""

list_x = [1, 2, 3, 4, 5, 6]


def square(a):
    return a * a


res = map(square, list_x)
print(list(res))
print("1=======================")

# 结合lambda表达式使用
res2 = map(lambda a: a * a, list_x)
print(list(res2))
print("2=======================")

list_y = [1, 2, 3, 4, 5, 6]
res3 = map(lambda a, b: a * a + b, list_x, list_y)
print(list(res3))
print("3=======================")

list_a = [1, 2, 3, 4]
list_b = [1, 2, 3, 4, 5, 6]
res4 = map(lambda a, b: a * a + b, list_a, list_b)
print(list(res4))
print("4=======================")
