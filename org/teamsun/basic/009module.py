"""
    3种import 方式
"""
import org.teamsun.pkgModule.myModule as myModule
import org.teamsun.pkgModule as pkgModule
from org.teamsun.pkgModule import myModule2
import org.teamsun.pkgModule.myModule3
from org.teamsun.pkgModule import *
print(myModule.module1)
print(pkgModule.pkgName)
print(myModule2.module2)
print(org.teamsun.pkgModule.myModule3.module3)
