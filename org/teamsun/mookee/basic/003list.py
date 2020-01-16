varList = [1, 2, True, 'a', "Hello"]
varList2 = [False, varList]
print(varList2)
print(varList2[1][4])
# 得到元素
print(varList[2])
# 得到列表
print(varList[2:3])
print(varList[2:4])
print(varList[2:])
# varList[3] = 'b'
print(varList)
print(varList + ['s'])
print(varList * 3)
varQtList = [['巴西', '克罗地亚', '墨西哥', '喀麦隆'],
             ['巴西1', '克罗地亚1', '墨西哥1', '喀麦隆1'],
             ['巴西2', '克罗地亚2', '墨西哥2', '喀麦隆2']]

print(varList[3:], max(varList[3:]))
print(2 in varList)
print(2 not in varList)
