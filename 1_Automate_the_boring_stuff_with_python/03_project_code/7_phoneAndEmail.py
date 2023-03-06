# ! python3
# phoneAndEmail.py -实现从剪切板获取电话号码和邮箱
import pyperclip
import re


# 读取电话号码的正则表达式
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))     #获取区号,且包含区号带括号的情况
    (-|\s|\.)    #中间的分隔符是-or空格，制表符，换行符or除了换行符之外的任意字符
    (\d{3})     #获取前三位
    (-|\s|\.)    #中间的分隔符是-or空格，制表符，换行符or除了换行符之外的任意字符
    (\d{4})     #获取后四位
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #如果后面有扩展字符也可以获取
)''',re.VERBOSE)

#获取邮箱的正则表达式

emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #邮箱的用户名部分，想不到除了数字和字母还能是._%+-
    @                   #邮箱标志的@符号
    [a-zA-Z0-9.-]+      #邮箱的域名
    (\.[a-zA-Z]{2,4})   #邮箱的.com部分 .在正则表达式里有其他含义，要转义一下才能用
)''',re.VERBOSE)

#获取剪切板的内容
text=str(pyperclip.paste())     #把获取的内容全部转成str格式，int格式的正则表达式处会出错
# 处理通过正则表达式获取的内容

matches = []
for groups in phoneRegex.findall(text): # 遍历findall获取所有的电话号码列表，并将之储存到列表matches中
    phonenum = '-'.join([groups[1],groups[3],groups[5]])  #把电话号码统统改成中间是-的格式
    matches.append(phonenum)

for groups in emailRegex.findall(text): # 遍历findall获取所有的邮箱列表，并将之储存到列表matches中
    matches.append(groups[0])


# 把获取的内容复制到剪切板上
if len(matches):
    pyperclip.copy('\n'.join(matches))
    print('内容已经复制到剪切板上')
    print('\n'.join(matches)) #把获取的内容打印出来
else:
    print('复制的内容里没有电话号码和邮箱')



