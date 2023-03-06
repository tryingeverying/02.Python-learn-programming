#! python3
# 让文件的后缀名按序排列，若有空缺则更改后面文件的后缀名

import os,shutil,re

wenjianming_bian={}

def gaiming():
    regex=re,compile(r'('+wenjian_qianzhui+')(\d+)(\.?'+wenjian_houzhui+')')
    for a in os.listdir(chazhao_mulu): #依次取出文件夹里的文件名称
        mo = regex.search(a)            # 提取出符合要求的文件名
        if mo != None: # 文件名是否符合要求
            wenjianming_bian[a]=mo.group(2) # 将符合要求的文件名和数字编号储存到字典中
        else:
            continue
    if len(wenjianming_bian)==0: #判断是否有符合要求的文件名
        print('没有符合要求的文件')
        os._exit(0) #结束后面的程序
    else:
        bianhao_zuida = int(max(wenjianming_bian.values())) # 找出字典中的最大编号
        list_biaohao =[]
        list_biaohao_kong =[]
        for c in wenjianming_bian.values(): #遍历字典中的数字编号
            list_biaohao.append(int(c))     # 将数字编号前面的零给去掉，并将之存入一个list
        for i in range(1,bianhao_zuida+1):  #遍历低于最大编号的所有编号
            if i not in list_biaohao:       # 判断是否存在文件编号空缺
                list_biaohao_kong.append(i) # 将空缺的编号存入list
            else:
                continue
        
        if len(list_biaohao_kong)==0:       # 判断缺号列表是否为空
            print('文件名称中无空缺编号')
        else:
            print('文件名称中空缺的编号为：',list_biaohao_kong)

        panduan = input('是否进行重新排序(Y/N):')   #是否对文件名进行重新编号
        if panduan == 'Y':
            chongbian()
        else:
            os._exit(0)

def chongbian():
    while True:
        bianhao_weishu=input('请输入重新编码的位数：')
        if bianhao_weishu.isdecimal() == False or len(bianhao_weishu)==0:   #str.isdecimal() 判断前面的字符串是否为十进制的数字
            print('位数需要是整数且不为0')
        else:
            break
    wenjianming_bian_2 =sorted(wenjianming_bian.items(), key=lambda item:item[1])   
    #字典按value进行排序
    # 返回一个以字典item为tuple为元素的列表
    bianhao = 1
    for b in wenjianming_bian_2:    # 遍历排序之后的文件编号的list
        wenjian_new=b[0].replace(b[1],str(bianhao).rjust(int(bianhao_weishu),'0')) #用新编号替代旧编号
        bianhao +=1
        shutil.move(os.path.join(chazhao_mulu,b[0]),os.path.join(chazhao_mulu,wenjian_new))# 可以实现在不同文件夹下的移动和重命名
        #os.rename(os.path.join(chazhao_mulu,b[0]),os.path.join(chazhao_mulu,wenjian_new)) #在同一个文件夹下对文件进行重命名可以用os.rename()
    print('文件以重新编码')


while True:
    chazhao_mulu=input('请输出待处理的文件目录')
    if os.path.isdir(chazhao_mulu):
        break
    else:
        print('输入的文件路径不存在')

wenjian_qianzhui = input('输入本次查找的文件前缀')
wenjian_houzhui = input('输入本次查找的文件后缀')

gaiming()

















