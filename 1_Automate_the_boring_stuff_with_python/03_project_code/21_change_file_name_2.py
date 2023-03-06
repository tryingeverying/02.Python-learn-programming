#! python3
# 检查文件的编号，如果出现缺失则后面的编号发生更改
# 该代码的优势是代码量小，但是只能处理一层文件夹的文件，对于更深层的子文件夹下的文件无法实现改名，但是人家貌似没有要求让你遍历目录树

import re,os,shutil

wenjian_mulu = input('请输入要检查的目录：')
qianzhui_name = input('请输入文件的前缀：')

qianzhui_regex=re.compile(r'%s\d{3}' %qianzhui_name) #文件名的正则表达式，前缀加上三位数字
biaohao_regex=re.compile(r'\d{3}') #编号的正则表达式，三位数字

wenjianming_list=[] #储存文件名的list

for filename in os.listdir(wenjian_mulu): #遍历待检查目录下的所有文件，并且按序排列(文件在系统中是排好顺序的)
    #判断是文件且文件名是按要求的前缀和具有编号
    if os.path.isfile(os.path.join(wenjian_mulu,filename)) and qianzhui_regex.search(filename):
        #将符合要求的文件名存入list
        wenjianming_list.append(filename)
print(wenjianming_list)

for i in range(len(wenjianming_list)):#遍历符合要求的文件名list
    if i==0:
        continue
        # 文件名的序号满足要求后一个比前一个大一
    elif (int(biaohao_regex.search(wenjianming_list[i])).group()-int(biaohao_regex.search(wenjianming_list[i-1]).group()))>1:
        #对于不符合要求的文件名序号改为前面的序号加一
        num=int(biaohao_regex.search(wenjianming_list[i-1]).group())+1
        #os.path.splitext(path) 将文件路径分为前面路径和后缀名，0是前面的路径即basename 1是后缀名
        houzhui_name=os.path.splitext(os.path.join(wenjian_mulu,wenjianming_list[i]))[1]
        #使用格式化输出整合新的文件名
        wenjian_name=r'%s%3d%s'%(qianzhui_name,num,houzhui_name)
        #重命名文件，应该能用os.rename()实现
        shutil.move(os.path.join(wenjian_mulu,wenjianming_list[i]),os.path.join(wenjian_mulu,wenjian_name))
        wenjianming_list[i]=wenjian_name

print(wenjian_name)











