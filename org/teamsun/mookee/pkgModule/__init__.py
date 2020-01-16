"""
    加入本文件，使该文件夹成为包
    本文件也可以使用，包名即是本文件名
    引入该包/ 包下的模块 的时候，该文件自动运行。多用于初始化该包内容
"""
# __all__ 属性 规定了使用 * import 时的文件列表
# __all__ = ['myModule', 'myModule2', 'myModule3']
pkgName = "Jacky_Root"
print("=========>>>>>>>>>__init__.py runs~~~~~~")
