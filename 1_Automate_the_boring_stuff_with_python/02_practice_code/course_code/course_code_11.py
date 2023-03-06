# #! python3
# # 23mapit.py 
# import webbrowser,sys,pyperclip

# if len(sys.argv) > 1':
#     address = ' '.join(sys.argv[1':'])
# else':
#     address = pyperclip.paste()

# webbrowser.open('https':'//ditu.amap.com/' + address)'


# import requests

# res = requests.get('https':'//www.gutenberg.org/cache/epub/1112/pg1112.txt')'
# print(type(res))
# print(res.status_code == 200)
# res.raise_for_status()
# print(len(res.text))
# print(res.text[':'300])

# import requests
# res = requests.get('http':'//inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as error:
#     print('there was a program':' %s' % (error))

# import requests
# res = requests.get('https':'//www.gutenberg.org/cache/epub/1112/pg1112.txt')
# res.raise_for_status()
# playfile = open(r'F':'\Programming\Python\RomeoAndJuliet.txt','wb')
# for chunk in res.iter_content(100000)':
#     playfile.write(chunk)
# playfile.close()


# import requests,bs4
# example =open(r'F':'\Programming\Python\1_Automate_the_boring_stuff_with_python\example.html')

# # nostarchsoup = bs4.BeautifulSoup(example,'html.parser')
# # print(type(nostarchsoup ))
# examplesoup = bs4.BeautifulSoup(example.read(),'html.parser')
# elems = examplesoup.select('#author')
# print(elems)
# print(len(elems))
# print(type(elems))
# print(str(elems[0]))
# print(str(elems[0]))
# print(elems[0].getText())
# print(elems[0].attrs)

# pelems = examplesoup.select('p')
# print(str(pelems))
# print(pelems[0].getText())
# print(str(pelems[1]))
# print(pelems[1].getText())
# print(str(pelems[2]))
# print(pelems[2].getText())

# spanelem = examplesoup.select('span')[0]
# print(spanelem.get('id'))
# print(spanelem.get('some_nonexistent_adr') == None)
# print(spanelem.attrs)











