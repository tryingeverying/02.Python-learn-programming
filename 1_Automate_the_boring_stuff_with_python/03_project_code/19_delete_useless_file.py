#! python3
# 删除那些内存过大的文件

import os,shutil,send2trash

def xuanze_shanchu():
    for foldername,subfolder,filenames in os.walk(chuli_mulu):
        for filename in filenames:
            file_path =os.path.join(foldername,filename)
            file_size=os.path.getsize(file_path)
            if file_size >= wenjian_size:
                print(file_path,'——文件大小',file_size,'K')
                #send2trash.send2trash(file_path)
            else:
                continue

while True:
    chuli_mulu=input(r'请输入要处理的路径')
    if os.path.isdir(chuli_mulu):
        break
    else:
        print('输入的路径不存在')

wenjian_size=float(input('请输入待处理的文件大小'))

xuanze_shanchu()







