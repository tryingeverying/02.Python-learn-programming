#! python3
# phoneAndEmail.py 找出复制到剪切板信息中的电话号和电子邮箱并返回到剪切板上

import re, pyperclip

# 查找电话号码的正则表达式
phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?  # 三个数字or括号三个数字 出现零次or一次
    (\s|-|\.)?          # 一个制表符or空格or短横线or任意符号 出现零次or一次
    (\d{3})             # 三个数字
    (\s|-|\.)           # 一个制表符or空格or短横线or任意符号
    (\d{4})             # 四个数字
    (\s*(ext|x|ext.)\s*(\d{2,5}))?)
                        # 任意个制表符or空格or换行 一个ext|x|ext.任意个制表符or空格or换行 二到五位的数字
""", re.VERBOSE)

# 创建一个查找电子邮件的正则表达式
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+  #出现至少一次的a-zA-Z0-9._%+-
    @                  #一个必须的@
    [a-zA-Z0-9.-]+     #出现至少一次的a-zA-Z0-9.-
    (\.[a-zA-Z]{2,4})  #一个必须出现的. 2到4位的a-zA-Z
)""", re.VERBOSE)

# 获取剪切板上的内容，并将之赋值一个变量
text = str(pyperclip.paste())
    # 创建一个用于储存匹配结果的list
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1],groups[3],groups[5]])
    # join传入的参数是一个list
    # 在不同的电话号部分间加上-
    if groups[8] != "":
        phoneNum += " x" + groups[8]
        print(groups[6])    # (\s*(ext|x|ext.)\s*(\d{2,5}))?)
        print(groups[7])    # (ext|x|ext.)
        print(groups[8])    # (\d{2,5})
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# 将得到的匹配结果返回到剪切板上

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("匹配结果已经返回到剪切板上")
    print("\n".join(matches))
else:
    print("剪切板上的内容无电话号码和电子邮箱地址")



