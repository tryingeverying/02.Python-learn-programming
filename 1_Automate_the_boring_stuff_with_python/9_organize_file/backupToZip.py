#! python3
# backupToZip.py 备份当目标文件夹的文件有增加时，
# 将该文件夹写入到一个zip文件中用以备份

import zipfile, os

def backupTOZip(folder):

    # 获取目标文件夹的abspath
    folder = os.path.abspath(folder)

    # 找到没有备份的文件 
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFileName):
            break
        number += 1
    # 上面代码的意思是检查是否存在一个名称符合要求的文件，
    # 如果没有则创建，例如存在一个_1的zip文件，则number加一，
    # 此时文件不存在，跳出循环，创建该文件

    print(f"创建文件{zipFileName}")
    backupZip = zipfile.ZipFile(zipFileName,'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f"正在添加{foldername}中的文件")
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename("folder") + "_"
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            # 剔除之前备份的文件
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("done")

backupTOZip(r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\9_organize_file\toolFiles")













