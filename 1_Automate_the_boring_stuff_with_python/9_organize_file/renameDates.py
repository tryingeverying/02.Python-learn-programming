#! python3
# renameDates.py - 将文件夹中的MM-DD-YYYY格式文件名改成DD-MM-YYYY格式

# 使用 os.listdir获取目标文件夹下的所有文件名
# 使用正则查找文件名中MM-DD-YYYY格式的文件
# 使用shutil更改文件名


import re, os, shutil

# 写一个能够查找MM-DD-YYYY格式的正则表达式
datePatternRegex = re.compile(r"""
    ^(.*?)          # 文件名前的前缀为任意个非换行字符，取少不取多
    ((0|1)?\d)-     # 查找月份(0|1)?意味着0,1 可以出现也不可以不出现
    ((0|1|2|3)?\d)- # 匹配日
    ((19|20)\d\d)   # 匹配年份
    (.*?)$          # 最后以任意个非换行符结尾取少不取多
""", re.VERBOSE)


# 遍历目标路径下的所有文件名，获取符合要求的文件名
aimPath = r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\9_organize_file\toolFiles"
for amerFilename in os.listdir(aimPath):
    mo = datePatternRegex.search(amerFilename)
    
    # 跳过不符合要求的文件名
    if mo == None:
        continue

    # 获取符合要求的日期的各部分
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPath = mo.group(8)


# 根据上面获取的文件名的各个部分组合出新的符合DD-MM-YYYY格式的文件名
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPath

# 拼接得到新格式文件的路径
    amerFilename = os.path.join(aimPath,amerFilename)
    euroFilename = os.path.join(aimPath,euroFilename)

# 重命名文件
    print(f"已经将{amerFilename} 修改为 {euroFilename}\n")
    shutil.move(amerFilename,euroFilename)









