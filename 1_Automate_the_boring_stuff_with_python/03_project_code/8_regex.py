import re

#20
num_regex=re.compile(r'^\d{1,3}(,\d{3})*$')

num=['12','1,234','12,345','12,34,56','1234']
for num_i in num:
    num_1=num_regex.search(num_i)
    if num_1:#如果字符串不符合正则表达式则返回none，但是none是没有group这个属性的，所以要加上这个if判断来筛掉不符合的字符串
        print(num_1.group())


name_regex=re.compile(r'[A-Z][a-z]*[A-Z]*[a-z]*[A-Z]*\sNakamoto')
name=['Satoshi Nakamoto','Alice Nakamoto','RoboCop Nakamoto','satoshi Nakamoto','Mr. Nakamoto','Nakamoto','Satoshi nakamoto',]

for name_i in name:
    name_1=name_regex.search(name_i)
    if name_1:#如果字符串不符合正则表达式则返回none，但是none是没有group这个属性的，所以要加上这个if判断来筛掉不符合的字符串
        print(name_1.group())

#22
char=['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.','ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']
char_regex=re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)(\.)$',re.I)

for char_i in char:
    char_1=char_regex.search(char_i)
    if char_1:#如果字符串不符合正则表达式则返回none，但是none是没有group这个属性的，所以要加上这个if判断来筛掉不符合的字符串
        print(char_1.group())





