#pathl标准库

from pathlib import Path

root = input('请输入你要遍历的目录: ')

# 遍历用户指定的目录，如果想偷懒，可以用 Path.rglob('*')
# Path.rglob('*') 相当于自动给参数加上 '**/' 的 glob
# Path(path).glob('**/*') 返回path下所有的子目录/文件的生成器
files = Path(root).glob('**')

# 按文件大小由大到小命名的新目录
output_dir = input('请输入你要新建的目录: ')

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
    new_basename = str(filename) + '_' + old_file.stem + old_file.suffix
    newfilename = Path(output_dir) / Path(new_basename)

    # 调用 Path.rename() 实现移动文件的效果
    old_file.rename(newfilename)

    filename += 1
