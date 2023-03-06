#! python3
# 2_updateproduce.py 批量更改Excel文件中的指定内容

import openpyxl
from sklearn.metrics import max_error

# 读取目标文件的内容
wb = openpyxl.load_workbook(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file\produceSales.xlsx')
sheet = wb.active

# 待修改的内容
price_update = {
    'Gralic':3.07,
    'Celery':1.19,
    'lemon':1.27
}

#遍历文件，修改相应内容
for row in range(2,sheet.max_row+1):
    row_value = sheet['a'+str(row)].value

    if row_value in price_update:
        sheet['b'+str(row)].value = price_update[row_value]

wb.save(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\Reproduce_code\12_处理Excel电子表格\2_update.xlsx')











