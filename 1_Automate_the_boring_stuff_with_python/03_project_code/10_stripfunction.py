import re

def stripregex(longstr,str='\s'):
    stripregex=re.compile(str)
    str_1=stripregex.sub('',longstr)

    print(str_1)

str0 = '000000kdajsjd00000'
str1 = 'aaadsda   sdasda adsadaaaaa'
#传入一个参数的
str2 = '   jbsjdsd     '
str3 = '\n   \n\tdsda   sdasda adsadaaaaa  \n\n'

stripregex(str0,'0')
print(str0.strip('0'))
print('hello')












