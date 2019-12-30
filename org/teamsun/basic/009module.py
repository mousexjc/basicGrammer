"""
    3种import 方式
    包被 import 的同时，会执行 __init__.py
    模块被 import 同时，该模块即被执行
"""
import org.teamsun.pkgModule.myModule as myModule
import org.teamsun.pkgModule as pkgModule
from org.teamsun.pkgModule import myModule2, myModule3
# import org.teamsun.pkgModule.myModule3
from org.teamsun.pkgModule import *
print(myModule.module1)
print(pkgModule.pkgName)
print(myModule2.module2)
print(myModule3.module3)
