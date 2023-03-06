from openpyxl import load_workbook

# 载入文件
wb = load_workbook(filename='biostats.xlsx')

# 获取表格当前激活的表单
ws = wb.active

# 打印所有行，每行一个元组
'for row in ws.values':''
    print(row)