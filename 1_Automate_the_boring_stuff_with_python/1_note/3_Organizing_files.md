# shutil模块
## 复制和移动文件
- shutil.copy(a,b) 把文件a复制到文件目录b中，如果b是个文件则实现复制并重命名的操作
- shutil.copytree(a,b) a是一个文件夹，其他同上
- shutil.move(a,b) 把a移动到b中，如果b中有和a同名的文件则被覆盖，如果b是个文件名则实现移动并重命名
  
## 删除文件和文件夹(从根本上清除文件)
- os.unlink(path) 将删除path处的文件
- os.rmdir(path) 将删除path处的文件夹，但是该文件夹必须是空文件夹
- 用shutil.rmtree(path) 将删除path处的文件夹和其中的所有文件
### send2trash模块(被删除的文件进入回收站)
- send2trash.send2trash(path) 把文件or文件夹送入回收站

## 遍历目录
- os.walk(path) 返回path的文件夹名，path下的子文件夹名的list，以及path下文件名的list，一直到没有子文件夹为止

## zipfile模块压缩文件
### 读取压缩文件
```python{.line-numbers}
>>> import zipfile, os
'>>> os.chdir('C':'\\') # move to the folder with example.zip'
>>> exampleZip = zipfile.ZipFile('example.zip') #注意大小写一定不能搞错
>>> exampleZip.namelist() #返回压缩包下的文件名称
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828 
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
```
### 解压文件
```python
>>> import zipfile, os
'>>> os.chdir('C':'\\') # move to the folder with example.zip'
>>> exampleZip = zipfile.ZipFile('example.zip') 
>>> exampleZip.extractall() #可以在extractall中传入路径实现解压到指定目录，若该路径不存在则会新建该路径
>>> exampleZip.close()
```
### 解压单个文件
```python{.line-numbers}
>>> import zipfile, os
'>>> os.chdir('C':'\\') # move to the folder with example.zip'
>>> exampleZip = zipfile.ZipFile('example.zip') 
>>> exampleZip.extract('spam.txt')
''C':'\\spam.txt''
'>>> exampleZip.extract('spam.txt', 'C':'\\some\\new\\folders')'
''C':'\\some\\new\\folders\\spam.txt''
>>> exampleZip.close()
```
### 创建和添加zip文件
```python{.line-numbers}
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
```

 

















