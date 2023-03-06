import openpyxl

list_txt = [open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file\1.txt'),open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file\2.txt')]

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(len(list_txt)):
    read_line_text = list_txt[i].readlines()
    for j in range(len(read_line_text)):
        sheet.cell(row = j+1 ,column= i+1).value = read_line_text[j]
    list_txt[i].close()

wb.save(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file\1_example.xlsx')












