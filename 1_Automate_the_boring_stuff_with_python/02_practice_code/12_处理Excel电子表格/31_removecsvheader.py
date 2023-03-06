#! python3
# 31_removecsvheader.py 移除当前工作文件夹中所有csv文件的表头
import csv ,os
os.chdir(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\02_practice_code\csv文件')
print(os.getcwd())
os.makedirs('..\headerremoved',exist_ok=True)
# 获取目标文件夹中的所有csv文件
for csvfilename in os.listdir('.'):
    if not csvfilename.endswith('.csv'):
        continue

    print('remove header from ' + csvfilename + '...')

    # 遍历csv文件中的每一行，获取除了第一行外的信息
    csvrows = []
    csvfileobj = open(os.path.join(csvfilename))
    readerobj = csv.reader(csvfileobj)
    for row in readerobj:
        if readerobj.line_num == 1:
            continue
        csvrows.append(row)
    csvfileobj.close()

    # 将内容写入新文件中
    csvfileobj = open(os.path.join(r'..\headerremoved',csvfilename) ,'w' ,newline='')
    csvwriter = csv.writer(csvfileobj)
    for row in csvrows:
        csvwriter.writerow(row)
    csvfileobj.close()

