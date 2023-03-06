#! python3
# 备份文件

import zipfile,os

def backuptozip(folder):
    # 确保文件路径为绝对路径
    folder = os.path.abspath(folder)
    os.chdir(folder)
    number=1
    # 判断文件是否存在
    while True:
        zipfilename = os.path.basename(folder) + '_' +str(number) + '.zip'
        if not os.path.exist(zipfilename):
            break
        number = number + 1
    # 创建zip文件
    print(f'creating {zipfilename}...')
    backupzip = zipfile.ZipFile(zipfilename,'w')

    # 遍历所有文件
    for foldername,subfolder,filenames in os.walk(folder):
        print('adding files in %s...'%(foldername))
        # 添加当前目录到zip文件
        backupzip.write(foldername)
    
        for filename in filenames:
            newbase = os.path.basename(folder) + '_'
            if filename.startswith(newbase) and filename.endswith('.zip')
                continue
            backupzip.write(os.path.join(foldername,filename))
    backupzip.colse()
    print('done')

backuptozip('path')








