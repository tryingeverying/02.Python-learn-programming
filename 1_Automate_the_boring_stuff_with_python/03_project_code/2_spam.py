spam = {'cat':'animal'}
print('cat' in spam)
print('cat' in spam.keys())

# if 'color' not in spam:
#     spam['color']='black'
#     print(spam)
spam.setdefault('color','black')#当字典中没有前面那个字符的key时，自动添加该键且赋予该键后面那个值的value
print(spam)