#! python3
# 实现读取若干个txt文件逐行读取写入Excel的单元格中，一列对应一个txt文件

import openpyxl
# 打开文本文档的内容，并创建Excel文件
textlist = [open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\Reproduce_code\12_处理Excel电子表格\6_1.txt'),open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\Reproduce_code\12_处理Excel电子表格\6_2.txt')]

wb=openpyxl.Workbook()
sheet = wb.active

#逐行读取文本文档，并将之写入Excel中
for i in range(len(textlist)):
    read_line_text = textlist[i].readlines()
    for j in range(len(read_line_text)):
        sheet.cell(row=j+1,column=i+1).value = read_line_text[j]

    textlist[i].close()  

wb.save(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\Reproduce_code\12_处理Excel电子表格\6_result.xlsx') 








