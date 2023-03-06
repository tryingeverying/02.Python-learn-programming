import re 
import pyperclip 

def password(password):
    lowerregex=re.compile(r'[a-z]+')
    upperregex=re.compile(r'[A-Z]+')
    numregex=re.compile(r'\d+')
    digitsregex=re.compile(r'.{8,}')
    if lowerregex.search(password) and upperregex.search(password) and numregex.search(password) and digitsregex.search(password):
        print(f'{password}符合密码强度要求')
    else:
        print(f'{password}不符合密码强度要求')

def password_test(password):
    len_re = re.compile(r'.{8,}')
    a_re = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')
    num_re = re.compile(r'\d')
    if len_re.search(password) and a_re.search(password) and num_re.search(password):
        print('your password is strong enough!')
    else:
        print('please reset your password')

text = pyperclip.paste()
password(text)
password_test(text)



def re_strip(text,delchar=' '):
    stringregex=re.compile(r'^['+ delchar + ']*|['+ delchar +']*$')
    print(stringregex.sub('',text))

text = str(pyperclip.paste())
print(text)
re_strip(text,'a')

