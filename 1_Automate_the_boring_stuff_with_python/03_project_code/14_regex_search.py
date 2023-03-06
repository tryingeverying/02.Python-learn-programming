#! python3
# 14_regex_search.py 查找文件夹中符合正则表达式要求的内容并返回

import os,re

#写一个正则表达式
five_word=re.compile(r'\s[a-z]{5}\s')

re_ans=[]

pathname=r'F:\Programming'
for filename in os.listdir(pathname):
   
    if filename.endswith('.txt'):
        with open(filename,'r') as f:
            t_text = f.read()
            t_re_text = five_word.findall(t_text)
            re_ans += t_re_text

print(re_ans)



