#print

# print(*object,[,sep=' ',end='\n',file=sys.stdout,flush=Flash])
# sep='间隔符'，
# end='转义符'，
# file='print输出的对象是中的还是在特定文件中'
# flush='True/Flase'是否将内容写入内存


#f-string方法，在字符串前面加上f/F,就可以对后面的变量算出来
# name='虚竹'
# feature='盗号'
# print(f'天龙里头的挂逼有{name}，他是{feature}的')
# print(F'天龙里头的挂逼有{name[0:1]}，他是{feature}的')#也可以是一些需要计算的表达式

# #.format()方法
# print('天龙里头的挂逼有{}，他是{}的'.format(name,feature))
# print('天龙里头的挂逼有{1}，他是{0}的'.format(name,feature))#默认的是0到n，但是可以改
# print('天龙里头的挂逼有{n}，他是{f}的'.format(n=name,f=feature))# 也可以赋值给变量，在{}中使用变量名
# print('天龙里头的挂逼有{0}，他是{f}的'.format(name,f=feature))#混用也OK

# #格式规格迷你语言
# from fileinput import filename
# import random

# from sympy import content

# scores=[random.randint(60,100) for x in range(10)]
# student=[1+x for x in range(10)]
# transcript = dict(zip(student,scores))

# ranked_transcript={
#     k:v
#     for k,v in sorted(transcript.items(),key=lambda item:item[1],reverse=True)
# }
# print(ranked_transcript)

# students = []
# for x in range(10):
#     #利用ASCII码自动起名
#     name='小'+chr(ord('A')+x)
#     student={
#     'name':name,
#     'id':1+x,
#     'score':random.randint(60,100)
#     }
#     students.append(student)#将生成的student放入students中

# print(students)

# students.sort(key=lambda x:x['score'],reverse=True)
# rank=1
# for student in students:
#     print(f"{rank:02d}.{student['name']:>5} {student['score']:<3d}")#0是前面填充0,2是两个字符，d是数字类型，>右对齐，<左对齐
#     rank+=1


# #文件读写
# # f=open('filename.md','r')
# # filename即文件名(文件路径)，mode为打开模式
# # 'r' 读取（默认的，可不写明）
# # 'w' 写入，并先截断文件
# # 'x' 排他性创建，如果文件已存在则创建失败
# # 'a' 写入，如果文件内有东西则在末尾追加
# # 'b' 二进制模式
# # 't' 文本模式
# # '+' 打开用于更新(读取并写入)

# f =open('log.txt','w')
# name='虚竹'
# feature='盗号'
 
# print(name,feature,file=f)

# f.close()

# f=open('log.txt','r+')
# content = f.read()
# print(content)
# f.write('天龙二挂')
# f.close()


#f.readlines()

f=open('log.txt')

f.seek(28) #从n处开始访问文件内容
content =f.readline()#f.readlines()返回一个字符串or二进制byte组成的list
while content:
    print(content,end=',')
    content =f.readline()# f.readline(),返回字符串，包含换行符\n
    print(f.tell()) # 返回目前访问的文件位置在多少字节处
    
f.close()

with open('log.txt','w') as n:
#打开文件并将返回值给n，之后close文件
    print(n)























