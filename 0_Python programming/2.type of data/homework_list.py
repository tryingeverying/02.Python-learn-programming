str_1='mixuebingchengtianmimi'

change_list=[]
for char_list in str_1:
    split_list=ord(char_list)
    change_list.append(hex(split_list)[2:])
print(change_list)

answer_2=''
for answer_list in change_list:
    answer_list_split=''
    answer_list_split='0x'+answer_list
    answer_2+=chr(int(answer_list_split,base=16))
print(answer_2)
# 这个列表的使用其实是让代码简化了，毕竟在使用for循环遍历列表的时候直接就能把字符串两个两个的提取出来








