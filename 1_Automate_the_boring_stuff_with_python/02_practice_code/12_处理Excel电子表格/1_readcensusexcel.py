#！python3
# 1_readcensusexcel.py  读取相应的Excel文件，计算其中的每个县的普查区数目和每个县的总人口数

import openpyxl,pprint

#读取Excel文件
print('读取文件中......')
wb = openpyxl.load_workbook(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\practice_code\excel file\censuspopdata.xlsx')
sheet = wb.active
# 创建一个字典来储存处理过的数据
Statistical_data = {}

# 遍历Excel文件的每一行
for i in range(2,sheet.max_row+1):
    state = sheet['b'+str(i)].value
    county = sheet['c'+str(i)].value
    pop = sheet['d'+str(i)].value

    Statistical_data.setdefault(state,{})
    Statistical_data[state].setdefault(county,{'tract':0,'pop':0})

    Statistical_data[state][county]['tract'] += 1
    Statistical_data[state][county]['pop']+=int(pop)

print('打印统计结果中......')
result_file=open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\Reproduce_code\12_处理Excel电子表格\1_results.py','w')
result_file.write('alldate=' + pprint.pformat(Statistical_data))
result_file.close()
print('done')









