import openpyxl

wb = openpyxl.load_workbook(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file\1_example.xlsx')
sheet = wb.active

max_column_num = sheet.max_column

for i in range(max_column_num):
    txtfile = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file' + str(i+1) +'.txt','w')
    for j in list(sheet.columns)[i]: # 生成对于列value的元组
        txtfile.write(str(j.value))
    txtfile.close()







