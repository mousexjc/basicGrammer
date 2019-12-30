"""
    条件控制语句
    Jacky  2019-12-30
"""
var1 = False
if var1:
    print("true")
else:
    print("false")
a = 1
b = 2
if a > b:
    print("a")
else:
    print("b")
c = []
if c:
    print(" not empty")
else:
    print("empty")
# 常量属性名全大写
USER_NAME = "jacky"
PWD = '001'
print("please input userName:")
in_uName = input()
print("please input passWord:")
in_pwd = input()
if USER_NAME == in_uName and PWD == in_pwd:
    print("congratulations~")
else:
    print("sorry !")
