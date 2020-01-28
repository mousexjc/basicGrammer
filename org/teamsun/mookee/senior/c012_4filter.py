"""
    Chapter 12 函数式编程
    高阶函数 : filter(function, iterator)
    filter : 过滤
    function : 返回值必须为 bool 类型的值
    场景：适合集合的过滤
"""
list_x = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
res = filter(lambda x: True if x > 0 else False, list_x)
print(list(res))

# 例子 过滤小写字母
list_a = ["a", "A", "D", "E", "e"]

"""
    函数式编程，可以用，不必执着。
"""
