str_1='mixuebingchengtianmimi'
print(len(str_1))
change_str = ''
for char_str in str_1:
    split_str=ord(char_str)
    change_str+=hex(split_str)[2:]
print(change_str)

answer=bytes.fromhex(change_str)#因为change_str是十六进制数据，所以可以使用bytes.fromhex()将之转换为对应的ASCII数据
print(answer)