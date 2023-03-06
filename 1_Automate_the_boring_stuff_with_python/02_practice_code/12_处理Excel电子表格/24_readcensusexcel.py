#! python3

import openpyxl ,pprint

# 读取Excel数据
print('opening workbook......')
wb = openpyxl.load_workbook(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countydata= {}

#读取每个州的数据情况
print('reading rows...')
for row  in range(2,sheet.max_row + 1):
    state = sheet['B'+str(row)].value
    county =sheet['C'+str(row)].value
    pop =sheet['D'+str(row)].value

    countydata.setdefault(state,{}) #.setdefault 如果字典中不存在该key则创建该key，
                                    #这个也是实现不同州数据在不同字典中的关键，
                                    # 如果州的名称发生改变则在字典中创建一个新的子字典
    countydata[state].setdefault(county,{'tracts':0,'pop':0})

    
    countydata[state][county]['tracts']+=1
    countydata[state][county]['pop'] += int(pop)

print('writing results ....')
resultfile = open('census2010.py','w')
resultfile.write('alldata = ' + pprint.pformat(countydata))
resultfile.close()
print('done')






