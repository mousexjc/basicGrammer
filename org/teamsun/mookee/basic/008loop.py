"""
    循环控制语句
    Jacky 2019-12-30
    for / while
"""
a = 1
s = 0
while a <= 100:
    s += a
    a += 1
else:
    print(a)
print(s)
'''
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
print("loop list...........")
arr = [1, 3, 4, 2]
for _a in arr:
    print(_a, end=" ")
print("\nloop set...........")
aset = {1, 3, 2, 4, 3, 0}
for _a in aset:
    print(_a, end=" ")
print("\nloop dict...........")
dicta = {1: "a", 4: "d", 3: "c", 2: "b"}
for _a in dicta:
    if _a == 3:
        break
    print(_a, ": ", dicta[_a], end=" ,")
# range()
print("\nloop range(a)...........")
for _a in range(4):
    print(_a, end=" ,")
print("\nloop range(a, b)...........")
for _a in range(3, 5):
    print(_a, end=" ,")
print("\nloop range(a, b, c)...........")
for _a in range(0, 21, 3):
    print(_a, end=" ,")
print("\nloop range(len(list))...........")
for _a in range(len(arr)):
    print(_a, ":", arr[_a], end=",")
print("\nloop range(b, a)...........")
for _a in range(len(arr)):
    _b = len(arr)-_a-1
    print(_b, ":", arr[_b], end=" ;")
