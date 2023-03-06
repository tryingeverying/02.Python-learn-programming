# os模块
- os.path.join('A', 'B', 'C') 按照系统连接成对应的文件路径格式
  
```python{.line-numbers}
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'
```
- os.getcwd() 返回当前的工作路径
- os.chdir(x) 把当前的工作路径改成x
- os.makedirs(x) 创建一个路径为x的文件夹
## os.path()模块
- os.path.basename(x) 返回路径中的除文件名外的路径
- os.path.dirname(x) 返回路径中的文件名
```python{.line-numbers}
'>>> path = 'C':'\\Windows\\System32\\calc.exe''
>>> os.path.basename(path)
'calc.exe'
>>> os.path.dirname(path)
''C':'\\Windows\\System32''
```
- os.path.split(x) 返回目录名称和基本名称的列表
```python{.line-numbers}
'>>> calcFilePath = 'C':'\\Windows\\System32\\calc.exe''
>>> os.path.split(calcFilePath)
'('C':'\\Windows\\System32', 'calc.exe')'
```
- os.path.getsize(x) 返回路径下文件的大小
- os.listdir(x) 返回该路径下的所有文件的列表
















