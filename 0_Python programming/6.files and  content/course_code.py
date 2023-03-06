#二进制数据
# python里对于二进制数据处理有两种类型对象bytes和bytearray，bytes是不可变序列，bytearray是可变序列
# bytes 形式 b'n' 如果n为一个数据对应的二进制文件所对应的ASCII码表数据则会被翻译为他本身
from binascii import a2b_hex
from hashlib import new
from unittest import result


num_1=b'a'
print(num_1)
num_2=b'000\x30\n'
print(num_2)


# bytes和bytearray都是序列。他们支持切片，索引，查找之类的操作
# 此外还有hex()和fromhex()
# b.hex()是将二进制数据转换为对应的十六进制的字符串
num_3=bytes.fromhex('2030ff') #将16进制的字符串(长度需为二的整数倍)数据转换为对应的二进制类型
#20的十六进制数据对应的ASCII对应的是space 30十六进制数据对应的ASCII的是0
print(num_3)


#字符集和编码
a='文本'.encode()#将文本依照某种方式进行编码，默认utf-8
print(a)
print(a.decode()) #对编码进行解析，默认utf-8



#目录操作
import os

# 通过递归调用 os.listdir() 来实现目录遍历，得到一个包含所有文件的列表
def walk_dir(path):
    result = []
     # os.listdir(path)会读取path中的每一个文件名，但是不会往下一级读取
    for filename in os.listdir(path):
        #os.path.join(path, *paths) 返回对path和paths的拼接路径值
        file_path = os.path.join(path, filename)
        # os.path.isdir(path) 判断path是否为dir，并返回True/Flase
        if os.path.isdir(file_path):
            result += walk_dir(file_path)#递归调用，如果path是dir则继续调用该函数
        # os.path.isfile(path) 判断path是否为file，并返回True/Flase
        if os.path.isfile(file_path):
            result.append(file_path)

    return result

print(walk_dir(r'C:\Users\Fing-trying\Desktop\new'))
#r是原始字符串标记，即后面的所有\不识别为转义符
#r后面的字符不能以奇数个\结尾


root = input('请输入你要遍历的目录: ')

# 遍历用户指定的目录
files = walk_dir(root)

# 按文件大小由大到小命名的新目录
output_dir = input('请输入你要新建的目录: ')

# 新目录不存在时自动创建这个目录
#os.path.exists(path) 路径是否存在，返回相应的True/Flase
if not os.path.exists(output_dir):
    # os.mkdir(path) 创建一个path路径
    os.mkdir(output_dir)

# 使用 os.stat() 获取文件大小
file_dict = {}
for file in files:
    # os.stat(path) 返回path下文件的所有消息
    st = os.stat(file)
    file_dict[file] = st.st_size#在st的所有消息中读取size信息

print(file_dict)
# 用 数据类型进阶 一节学过的方法排序
sorted_files = {
    k: v
    for k, v in sorted(file_dict.items(), key=lambda x: x[1], reverse=True)
}
# 按照由大到小的顺序，给文件名前面加上数字前缀并移动到新的目录


filename = 1
for file in sorted_files.keys():
    # os.path.basename(path) 获取文件名的部分（不包括前面的路径），并返回
    basename = os.path.basename(file)
    #os.path.splitext(filename) 将文件名拆分成名字和后缀,并依次返回
    name, ext = os.path.splitext(basename)

    # 组合新的目录和新文件名
    new_basename = str(filename) + '_' + name + ext
    newfilename = os.path.join(output_dir, new_basename)

    # 调用 os.rename() 实现移动文件的效果
    # os.rename(file, newfilename) 将路径from  file to newfilename
    os.rename(file, newfilename)

    filename += 1

# 另一种遍历目录的方法。

def walk_dir(path):
    result = []
    #  os.walk(path)访问path下的所有文件，并依次root(返回访问的路径),dirs(root下的文件夹)，file(root下的文件)
    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.join(root, file)
            result.append(filename)

    return result

#pathl标准库

from pathlib import Path

root = input('请输入你要遍历的目录: ')

# 遍历用户指定的目录，如果想偷懒，可以用 Path.rglob('*')
# Path.rglob('*') 相当于自动给参数加上 '**/' 的 glob
# Path(path).glob('**/*') 返回path下所有的子目录/文件的生成器
files = Path(root).glob('**\*')

# 按文件大小由大到小命名的新目录
output_dir = input('请输入你要新建的目录: ')

#Path(path).mkdir(exist_ok=True)新建一个path， exist_ok=True如果该路径存在不报错
Path(output_dir).mkdir(exist_ok=True)

# 使用 Path.stat() 获取文件大小
file_dict = {}
for file in files:
    if Path(file).is_file():
        st = Path(file).stat()
        file_dict[file] = st.st_size

# 用 数据类型进阶 一节学过的方法排序
sorted_files = {
    k: v
    for k, v in sorted(file_dict.items(), key=lambda x: x[1], reverse=True)
}

# 按照由大到小的顺序，给文件名前面加上数字前缀并移动到新的目录
filename = 1
for file in sorted_files.keys():
    old_file = Path(file)

    # 组合新的目录和新文件名
    # PurePath.parent	获取一个路径中目录的部分
    # PurePath.name	获取一个路径中文件名的部分
    # PurePath.stem	获取不包含后缀的文件名，os.path 模块没有此类方法
    # PurePath.suffix	将一个路径分割成扩展名和非扩展名两个部分
    new_basename = str(filename) + '_' + old_file.stem + old_file.suffix
    #/ 拼接前后两个路径
    newfilename = Path(output_dir) / Path(new_basename)
    
    # Path.unlink(missing_ok=False)	删除文件
    # Path.rmdir()	删除目录
    # Path.rename(target)	重命名目录或者文件，相当于剪切并黏贴
    # 调用 Path.rename() 实现移动文件的效果
    old_file.rename(newfilename)

    filename += 1





























































