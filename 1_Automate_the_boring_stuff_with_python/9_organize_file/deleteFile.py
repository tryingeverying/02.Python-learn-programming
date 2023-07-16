#! python3 
# 编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，
# 比方说，超过100MB的文件（回忆一下，要获得文件的大小，
# 可以使用 os 模块的os.path.getsize()）。
# 将这些文件的绝对路径打印到屏幕上。

import os,send2trash

def deleteBigFile(folder):
    folder = os.path.abspath(folder)

    for folders, subfolder, filenames in os.walk(folder):
        print(f"正在遍历{folder}文件夹")

        for filename in filenames:
            filesize = os.path.getsize(os.path.join(folder,filename))
            print(f"{filename}的大小为{filesize}")
            # 判断大小删除文件
            # if filesize > 100:
            #     send2trash(os.path.join(folder,filename))
            
deleteBigFile(r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\9_organize_file\toolFiles")












