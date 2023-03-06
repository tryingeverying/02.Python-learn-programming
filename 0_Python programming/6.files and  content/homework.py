from os import rename
from pathlib import Path

path_old = input('输入一个路径：')
path_new = input('输入一个新路径：')

file_1 = Path(path_old).glob('**\*')

Path(path_new).mkdir(exist_ok=True)

#读取其中的文件
file_dict={}
for file_i in file_1:
    if Path(file_i).is_file():
        s_t = Path(file_i).stat()
        file_dict[file_i] = s_t.st_size
#按照文件的大小排序
sorted_file ={
    k:v
    for k,v in sorted(file_dict.items(),key=lambda x:x[1],reverse=True)
}
#按照文件大小给文件加上1,2,3,
file_add = 1
for file in sorted_file.keys():
    old_path = Path(file)

    new_filename = str(file_add)+'_' + old_path.stem + old_path.suffix
    new_path = Path(path_new)/Path(new_filename)
    file_add+=1
# 移动文件
    old_path.rename(new_path)





