'''
问题分解
1. 将字符串两个两个拆开
2. 将拆开的字符串前面加上十六进制的标志0x
3. 将十六进制的字符串用int函数给翻译为十进制的数字
4. 将字符串用chr函数把他给翻译回去
'''
a='49204c6f766520596f75'
split_char = []
int_char = []
answer_char = []
answer = ''
# split_char = ['0x'+a[i*2:(i+1)*2] for i in range(int(len(a)/2))] 
split_char = ['0x'+a[i:i+2] for i in range(0,len(a),2)] # 这个利用range函数里步长来改变列表index的方法可以呀
#分离字符的时候每一个其实都是每一个起始字符的index都是上一个的终止字符的index加一，所以用乘法要更好一点
#完成了第一个和第二个问题 
print(split_char)
int_char = [int(char,base=16) for char in split_char] #完成第三个问题
answer_char = [chr(int(answer)) for answer in int_char] # 完成第四个问题
for j in answer_char: # 列表转变为字符串
    answer += j
print(answer)

# for i in range(int(len(a)/2)):
#     add_char+='0x'+a[i:i+2]
# 完成了第二个问题把字符前面加上了十六进制的0x
# print(add_char)
# for j in range(int(len(a)/2)):  
#     #split_char[j]=add_char[j*4:(j+1)*4]
#     print(j)
# print(split_char)
