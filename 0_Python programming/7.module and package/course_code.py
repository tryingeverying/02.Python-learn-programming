#只导入某个模块而不导入则在导入改模块下面的函数时需要在函数前面加上模块名
import calc

print(calc.sum(1,2))

import calc as cc

print(cc.sum(1,2))
#导入了模块中的具体函数的时候就不用再加上模块名了
from calc import sum

print(sum(1,2))

from calc import *

print(sum(1,2))

#模块符号表
# import module
# print(dir(module)) 可以打印module中的所有函数名

#__name__变量
# 在文件中如果想查看自己的name的话直接调用__name__即可
# 如果导入了某个模块，想查看模块的name，要使用module.__name__的方式调用
#在命令行中，可以脚本方式运行某一文件/模块，这种场景下，全局变量 __name__ 的值为 __main__，因此在 Python 中常常通过判断 __name__ 的值来编写测试用例。

# sys 在测试的时候传入测试的参数
import sys

print(sys.argv)

# sys.version	字符串，包含 Python 版本信息
# sys.platform	字符串，包含操作系统信息
# sys.path	列表，包含元素为字符串，存储了模块搜索路径
# sys.byteorder	字符串，包含当前字节序，'little' / 'big'
# sys.argv	列表，包含元素为字符串，存储了被空格分割的参数

#模块的路径
# 在导入模块的过程中，Python 内置了一个搜索规则来查找所需的模块：

# 内置模块
# sys.path
#   包含输入脚本的目录（或者未指定文件时的当前目录）。
#   PYTHONPATH （一个包含目录名称的列表，它和 shell 变量 PATH 有一样的语法）。
#   取决于安装的默认设置。

# 避免在自己的代码目录里给文件名和标准库相同的名
import sys
print(sys.path)

# 包就是把一揽子的module放到一个文件夹中，包的文件夹内也可以有其他包
# 但是文件夹的最顶级文件必须是__init__.py.来告诉python这是个包
# 导入包的时候 不推荐使用from sound.formats import * 这类于法导入包中的所有模块。
# 开发者在 __init__.py 中定义了列表变量 __all__ ，并且其中包含了要导入的模块名字，要不然的话这样导入会找不到相应的模块


