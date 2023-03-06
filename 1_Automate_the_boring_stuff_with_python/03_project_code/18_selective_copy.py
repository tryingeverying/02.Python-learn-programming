#! python
# 选择性拷贝特定文件下的特定后缀的文件

import  os,shutil

def beifen():
    if not os.path.isdir(beifen_mulu):
        os.mkdir(beifen_mulu)
    for foldername,subfolder,filenames in os.walk(chazhao_mulu):
        for filename in filenames:
            if filename.endswith('.%s' % wenjian_type) and foldername !=beifen_mulu:
                wenjian_mulu = os.path.join(foldername,filename)
                shutil.copy(wenjian_mulu,beifen_mulu)
            else:
                continue

while True:
    chazhao_mulu =input('请输入一个待备份的路径')    
    if os.path.isdir(chazhao_mulu):
        break
    else:
        print('输入的待备份目录不存在')


wenjian_type=input('请输入一个待备份的扩展名')
beifen_mulu=input('请输入备份到的路径')

beifen()

# import os
# for foldernames,subfolders,filenames in os.walk(r'F:\Programming\测试目录'):
#         for foldername in foldernames:
#             print(foldername)
#         for filename in filenames:
#             print(filename)











