#! python3
# mad_libs.py 将待查询文本中的制定内容用自己的文本替换
"""
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
una fected by these events.
程序将找到这些出现的单词，并提示用户取代它们。
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
以下的文本文件将被创建：
The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.
"""

import re 


# 打开文件，读取内容
basePath = r"1_Automate_the_boring_stuff_with_python\8_read_write_file\test_file"

dealFile = open(basePath + r"\test.txt", "r")
dealContent = dealFile.read()
dealFile.close()

# 写一个匹配指定内容的正则表达式
matchWordList = ["ADJECTIVE","NOUN","ADVERB","VERB"]
regexList = '|'.join(matchWordList)

matchRegex = re.compile(regexList)
matchContent = matchRegex.search(dealContent)

while matchContent is not None:
    changePart = matchContent.group()
    replaceContent = str(input(f"请输入待替换的{changePart.lower()}\n"))
    dealContent = matchRegex.sub(replaceContent, dealContent,1)

    matchContent = matchRegex.search(dealContent)

dealedFile = open(basePath + r"\dealedtest.txt", "w")
dealedFile.write(dealContent)
dealedFile.close()






