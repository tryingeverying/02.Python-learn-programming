#! python3
# 将Excel文件中的内容以列为单位读取，每一列的内容逐行写入一个txt文档

import openpyxl

file_path = input(r'请输入待处理的文档')
# 打开待处理的Excel文档，并读取最大行号
wb = openpyxl.load_workbook(file_path)
sheet = wb.active
max_column_num = sheet.max_column

# 遍历每一行 并将内容写入对应的txt文档中
for i in range(max_column_num):
    txt_file = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\Reproduce_code\12_处理Excel电子表格\7_'+str(i+1)+'.txt','w')
    for j in list(sheet.columns)[i]: #这个list(sheet.columns)[i]用法是很巧妙的地方，直接就读取了这一行的所有内容，比使用row和column要简单的多
        txt_file.write(str(j.value))
    txt_file.close()