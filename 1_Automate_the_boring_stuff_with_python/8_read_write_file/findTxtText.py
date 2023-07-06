#! python3
# findTxtText.py
# 编写一个程序，打开文件夹中所有的.txt文件，
# 查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。

import os, sys, re

# 获取目标路径下的所有文件名，并将之写入到一个list中
basePath = r"1_Automate_the_boring_stuff_with_python\8_read_write_file\test_file"
fileList = os.listdir(basePath)
txtFileList = []

# 利用正则表达式获取所有后缀为.txt
findTxtRegex = re.compile(r".*\.txt$")
for fileName in fileList:
    matchObj = findTxtRegex.search(fileName)
    if matchObj :
        txtFileList.append(matchObj.group())

# 根据用户命令写一个查找具体内容的正则
toMatchRegex = re.compile(sys.argv[1])
# 遍历匹配出的.txt文件，逐行读取内容
for txtFileName in txtFileList:
    txtFile = open(basePath + "\\" + f"{txtFileName}",'r',encoding="utf-8" )
    linesOfTxtFile = txtFile.readlines()
    # 遍历上面逐行读取出来的内容，使用正则表达式匹配，符合要求的打印
    for line in linesOfTxtFile:
        lineMatchObj = toMatchRegex.search(line)
        if lineMatchObj:
            print(line)
    txtFile.close()











