#! python3
# multiclipboard.pyw 存储和加载剪切板上的内容
# usage: python.exe multiclipboard.pyw save <keyword> - 存储剪切板上的内容关联keyword
#         python.exe multiclipboard.pyw <keyword> - 加载keyword对应的内容到剪切板上
#         python.exe multiclipboard.pyw list - 加载所有剪切板上的关键字
#         python.exe multiclipboard.pyw delete <keyword> - 删除对应关键字以及对应的内容
#         python.exe multiclipboard.pyw delete 删除所有内容
#         .pyw扩展名意味着Python运行该程序时，不会显示终端窗口
"""
针对要检查的关键字，提供命令行参数。
如果参数是save，那么将剪贴板的内容保存到关键字。
如果参数是list，就将所有的关键字拷贝到剪贴板。
否则，就将关键词对应的文本拷贝到剪贴板。
增加一个delete <keyword>命令行参数，它将从shelf中删除一个关键字。
然后添加一个delete命令行参数，它将删除所有关键字。
"""

import shelve, pyperclip, sys

# 创建一个二进制文件用于存储信息
basePath = r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\8_read_write_file\test_file"
mcbshelf = shelve.open(basePath + r"\mcb")

# 判断命令行输入的情况如果命令参数为三个
# 且第二个命令是save则把剪切板上的内容写入到对应的关键字后面
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbshelf[sys.argv[2]] = pyperclip.paste()
# 判断命令行输入的情况如果命令参数为三个
# 且第二个命令是delete则把keyword对应的关键字键值对删除
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbshelf[sys.argv[2]]
# 如果命令参数是两个，且第二个参数为list 则把所有的关键写入剪切板
# 如果第二个参数在二进制文件中,则把其对应的value写入剪切板
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
    elif sys.argv[1].lower() == "delete":
        # # 这个删除好像只能遍历所有key来删
        # for key in mcbshelf.keys():
        #     del mcbshelf[key]
        mcbshelf.clear()
        # 好吧，清空是clear，这样的话上面哪个写法就有点蠢了

mcbshelf.close()




