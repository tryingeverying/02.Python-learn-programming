str_1='mixuebingchengtianmimi'
print(len(str_1))
change_str = ''
for char_str in str_1:
    split_str=ord(char_str)
    change_str+=hex(split_str)[2:]
print(change_str)


#代码目的把上述的16进制的数字转换为字符
'''
实现上述目的需要完成下面几部
1.把字符串给分成两个两个的字符，即实现字符串的拆分
2.把拆分出来的字符串加上16的前缀0x
3.把加上16进制的字符利用chr函数给变为字符，并实现字符串的连接
'''
# num_str=len(change_str)
# print(num_str)
answer_str=''
answer_1=''
#看了老师讲的一个每次两个两个的取的方法
#for i in range(0,len(change_str),2):
    #answer_str=change_str[i,i+1]
for num_str in range(int(len(change_str)/2)):
    
    answer_str=change_str[num_str*2:num_str*2+2]
  

    #print(answer_str)
    add_str=''
    add_str='0x'+answer_str
    #print(add_str)
    answer_1+=chr(int(add_str,base=16))
    
print(answer_1)

