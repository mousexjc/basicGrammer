"""
    Chapter10 正则表达式与json
    Part 1 正则表达式
"""
import re

languages = "C|C++|Java|C#|Python|Javascript|Python|Python"
# print(languages.index("Python"))
# print("Python" in languages)
res = re.findall("Python", languages)
if len(res) > 0:
    print("包含")
else:
    print("不包含")

# 提取字符串中的所有数字
str = "C9C++2Java6C#3Python|7Java|.script-4Pyn8PondsPan"
res = re.findall("\D", str)
print(res)
print(re.findall("P[^yo]n", str))
print(re.findall("P[a-o]n", str))
