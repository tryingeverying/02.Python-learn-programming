#! python3
# 更改日期格式from MM-DD-YYYY to DD-MMYYYY

import shutil,os,re

# 查找MM-DD-YYYY 格式的正则表达式

datepattern = re.compile(r'''
    ^(.*?)          #匹配前面的内容，以任意个非换行字符开头
    ((0|1)?\d)-     #匹配月份是01 o r1这种格式的月份
    ((0|1|2|3)?\d)- #匹配日期是01 or 1 or 11 or 21 or 31的月份
    ((19|20)?|d|d)  #匹配年份可以是19or20开头的1998or2001 or22
    (.*?)$          #匹配后面的内容，以任意个非换行字符结尾
''',re.VERBOSE)

#遍历文件夹
for amerfilename in os.listdir('.'):
    mo=datepattern.search(amerfilename)

    if mo==None:
        continue
    #获取日期内容
    beforepart = mo.group(1) # group的嵌套，从外到里依次排序 
    monthpart = mo.group(2)  # 首先匹配最外层的()
    daypart = mo.group(4)    # 然后依次匹配里层的()
    yearpart = mo.group(6)
    afterpart = mo.group(8)

    # 生成新的文件名
    eurofilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart
    # 获取路径
    absworkingdir = os.path.abspath('.')
    amerfilename = os.path.join(absworkingdir,amerfilename)
    eurofilename = os.path.join(absworkingdir,eurofilename)
    # 重命名文件
    print('renaming "%s" to "%s"'%(amerfilename,eurofilename))
    # shutil.move(amerfilename,eurofilename) #刚开始的时候把他给注释掉，等print出来的结果确定没问题之后再取消注释开始运行








