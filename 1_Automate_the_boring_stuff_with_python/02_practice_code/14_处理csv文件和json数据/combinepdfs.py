#！ python3
# 合并指定文件夹中的所有PDF文档，要求不合并每个PDF文档的第一页

import PyPDF2 ,os 

#获取指定文件夹下的所有PDF文档
PDFfile = []
os.chdir(r'F:\Programming\Python-learn-programming\1_Automate_the_boring_stuff_with_python\02_practice_code\PDF文档')
for filename in os.listdir('.'):   #遍历当前目录下的所有PDF文件，并将文件名储存在list中
    if filename.endswith('.pdf'):
        PDFfile.append(filename)

PDFfile.sort()  #文件名按照文件名的首字母升序排列 
pdfwrite = PyPDF2.PdfWriter()


# 读取每一个PDF文档
for filename in PDFfile:
    pdffileobj = open(filename,'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)

    # 写入除第一页外的所有PDF文档
    for pagenum in range(1,pdfreader.numPages):
        pageobj = pdfreader.getPage(pagenum)
        pdfwrite.addPage(pageobj)

# 保存文件
pdfoutput = open('allminutes.pdf','wb')
pdfwrite.write(pdfoutput)
pdfoutput.close()










