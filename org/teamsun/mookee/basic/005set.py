"""
集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
parame = {value01,value02,...}
或者
set(value)
"""
var1 = {1, 2, 3, 4}
print(var1)
print(1 in var1)
var2 = {2, 3, 4, 5, 6}
print(var1-var2)
print("1 & 2", var1 and var2)
print("2 & 1", var2 and var1)
print(var1 | var2)
