"""
    Chapter 12 函数式编程
    匿名函数
    格式：lambda param_list: expression
    lambda:关键字
    expression * :只能是【表达式】
"""


# 正常函数
def add(x, y):
    return x + y


f = lambda x, y: x + y
print(f(2, 3))
print("=====================")

# 三元表达式
# 其他语言：表达式 ？true结果 : false结果
# Python : true结果 if 表达式 else false结果
x = 1
y = 2
a = x if x > y else y
print(a)
