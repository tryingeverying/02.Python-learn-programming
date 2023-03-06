## webbrowser模块
- 只有一个简单的操作就是webbrower.open('url')来实现打开网页

## requests模块
- requests.get('url')来返回一个request对象
```py{.line-numbers}
import requests

'res = requests.get('https':'//www.gutenberg.org/cache/epub/1112/pg1112.txt') #通过requests库获取网址信息并来返回一个request对象'
print(type(res))
print(res.status_code == 200) #检查网页获取是否获取成功，成功的状态码是200 失败的状态码是404
##上面的检查是否获取成功的语句可是使用下面的语句代替
res.raise_for_status() #如果获取成功不返回任何信息，未获取信息的报错
print(len(res.text))
'print(res.text[':'300])'
'playfile = open(r'F':'\Programming\Python\RomeoAndJuliet.txt','wb')  # 新建一个文件以二进制的方式写入'
'for chunk in res.iter_content(100000)':'  #res.iter_content()是一个迭代器，表示写入多少个字节的内容'
    playfile.write(chunk)
playfile.close()    # 一定要记得把文件给关上
```

## BeautifulSoup模块
### select方法
![selectfhfa](\beautifulsoup_select.png)








