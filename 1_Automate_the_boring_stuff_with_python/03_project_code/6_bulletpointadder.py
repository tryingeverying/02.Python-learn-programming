#! python3
# 6_bulletpointadder.py 每行之前加星号

import pyperclip
text=pyperclip.paste()
#获取剪切板上的内容
line=text.split('\n')
#将获取的内容以换行符作为分隔
for i in range(len(line)):
    line[i]='! '+line[i]
# 取出每行内容，并对其进行处理
text='\n'.join(line)
pyperclip.copy(text)








