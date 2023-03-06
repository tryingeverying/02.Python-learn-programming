s="我就是想试试\
是不是真的"
a="""横空出世
莽昆仑"""
print(s)
print("电影 %s" %a)
print(a)

# 字符串的操作
str_1='python'
#str_1[0]='p'
print(str_1[0])
print(str_1[-5])

#报错可知字符串不可以被更改
str_2=['python']
str_2[0]='nohtyp'
print(str_2[0])
print(str_2[0][-5])
#但是把字符串变更为列表中的元素就可以更改了，但是对于列表中的字符串中的元素依旧是不能更改，只能更改列表中的元素

#字符串的切片
str_3='python'
print(str_3[:])
print(str_3[0:])
print(str_3[-5:])
print(str_3[1:4])

#字符串的拼接
first_str='first'
last_str='last'
str_4=first_str+' '+last_str
print(str_4)
str_5=str_3
print(str_5[::2])  #将字符串str_3从头到尾以步长为2切片

#打印多个字符串
num_1=2
str_6='听这个教程了'
print('这是我第%d次%s'%(num_1,str_6))

#数据类型转换
a=int(44626546)
print(a)
b=int('0b111110111',base=2)
#上面这个int的用法可以把任意进制的数字的字符串变为十进制 
c=int(0b111110111)
print(b)
print(c)
d=65
e=hex(d)
f=oct(d)
g=bin(d)
print(e,f,g)
#上述三个函数可以把整数转变为对应的进制
h=str(d)
j=str(e)
k=str(f)
l=str(g)
print(h,g,k,l)

m=ord('a')
n=chr(d)
print(m,n)
o=0x6d
print(chr(o))
# ord函数就是把传入的数字字符串转变为对应的十进制数字
# chr函数就是把传入的任意进制的数字转换为对应的ASCII码的字符
# 千万注意的是chr里传入的参数必须是数字，进制可以变，但是不能是数字字符串


#列表
list_1=list()
#这样只能创建一个空列表,不能在list里自己添加列表中的元素
list_2=list(range(6))
list_3=list(range(0,6,2))
list_4=[x*x for x in range(10)]
print(list_2,list_3,list_4)
#但是可以在list里调用range函数生成等差数列的列表
list_x.append(y)
# 把元素y添加到list_x的最后










































