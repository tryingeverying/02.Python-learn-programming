#! python3 
# 编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf或.jpg）。
# 不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。

import os, shutil

def selCopy(folder):
    # 获取目标文件夹的绝对路径
    folder = os.path.abspath(folder)
    
    for folders,subfolder, filenames in os.walk(folder):
        print(f"正在检查{folders}文件夹")
        for filename in filenames:
            if filename.endswith('.txt'):
                filename = os.path.join(folders,filename)
                shutil.copy(filename,r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\9_organize_file\toolFile")
                print(f"复制了{filename}")


selCopy(r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\9_organize_file\toolFiles")





