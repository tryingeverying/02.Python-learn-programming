#! python3
# Mad Libs.py 一个在模板句子里填充内容的代码


# 读取文本的内容
filename='mad_lib.txt'
with open(filename,'r') as m_l:
    text =m_l.readline()
    print(text)

# 获取输入
ADJ = input('enter an adjective:\n')
NOUN1 = input('enter a noun:\n')
VERB = input('enter a verb:\n')
NOUN2 = input('enter a noun:\n')

# 替换内容
text =text.replace('ADJECTIVE',ADJ)
text =text.replace('NOUN1',NOUN1)
text =text.replace('VERB',VERB)
text =text.replace('NOUN2',NOUN2)

print(text)
with open('new_lib.txt','w') as f:
    f.write(text)






