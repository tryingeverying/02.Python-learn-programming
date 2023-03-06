confession = 'I Love You'

message = ""
for char in confession:
    number = ord(char)
    message += hex(number)[2:]

print(message)

split_char = [] #用来放分开之后且加上十六进制的标志0x后的列表
int_char = [] #用来放将十六进制的字符转化为十进制的数字的列表  老感觉这个可以省略，毕竟chr函数能读十六进制的数字
answer_char = [] #用来放转化后的字符列表
answer = '' #将列表转化为字符串
split_char = ['0x'+message[i*2:(i+1)*2] for i in range(int(len(message)/2))] 
#分离字符的时候每一个其实都是每一个起始字符的index都是上一个的终止字符的index加一，所以用乘法要更好一点
#完成了第一个和第二个问题 

int_char = [int(char,base=16) for char in split_char] #完成第三个问题
answer_char = [chr(int(answer)) for answer in int_char] # 完成第四个问题
for j in answer_char: # 列表转变为字符串
    answer += j
print(answer)
