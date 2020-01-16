"""
    Chapter 12 函数式编程
    高阶函数 : reduce(function,sequence)
    reduce : 连续调用
"""
from functools import reduce

list_x = [1, 2, 3, 4, 5, 6]
res = reduce(lambda x, y: x * y, list_x)
print(res)
print("============1============")

list_str = ["a", "b", "c", "d"]
res2 = reduce(lambda x, y: x + y, list_str, "jacky:")
print(res2)
print("============2============")
