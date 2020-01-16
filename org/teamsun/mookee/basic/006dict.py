"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""
dictVar = {"a": "av", "b": "bv", 3: "cv"}
print(dictVar[3])
var1 = {"a": 1, 2: 2, 3: "c", "4": dictVar}
print(var1["4"])
var2 = {1: "a", 2: "b", 3: "c", 4: "d"}
print(var2)
del var2[2]
print("After Del :", var2)
# var2.clear()
# print("After Del :", var2)
