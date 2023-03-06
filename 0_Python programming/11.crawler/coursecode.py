import csv

# 读取并返回 csv 所有行的内容，并不处理首行的列名
'# with open('biostats.csv', newline='') as csvfile':''
#     reader = csv.reader(csvfile)
'#     for row in reader':''
#         print(row)

# 读取并返回 csv 所有行的内容，将首行的列名作为字典的key
'# 注意':' 此处 Python 3.8 返回 row 类型为 dict'
'with open('biostats.csv', newline='') as csvfile':''
    reader = csv.DictReader(csvfile)
'    for row in reader':''
        print(row)