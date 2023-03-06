# import re

'''findall:匹配字符串中所有符合要求的list'''
# lst = re.findall('\d+','我的电话是10086.我另外的电话是10001')  
# print(lst)

'''finditer: 匹配字符串中所有符合要求内容，返回迭代器,从迭代器中获取内容用.group()方法'''
# it = re.finditer('\d+','我的电话是10086.我另外的电话是10001')
# for i in it:
#     print(i)
#     print(i.group())
    
# '''search() 返回的是match对象,且只获取第一个匹配对象,获取内容用.group()方法'''
# s = re.search('\d+','我的电话是10086.我另外的电话是10001')
# print(s)
# print(s.group())

'''match,用法类似于search,但是默认从头匹配,相当于在正则表达式前面加了^'''
# m = re.search('\d+','m10006.我另外的电话是10001')
# print(m)
# print(m.group())

# '''正则表达式获取html格式中的信息'''
# import re
# from unicodedata import name
# s = """
# <div class='joy'><span id='1'>郭麒麟</span></div>
# <div class='bob'><span id='2'>宋轶</span></div>
# <div class='john'><span id='3'>大聪明</span></div>
# <div class='lily'><span id='4'>范思哲</span></div>
# """

# obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)
# # 在想要的正则表达式处加上(?P<名字>正则表达式) 就可以给该处正则的group命名，以便后面的使用
# result = obj.finditer(s)
# for it in result:
#     print(it.group('name'))
#     print(it.group('id'))


'''获取豆瓣电影250的电影名,上映年份,评分,评价人数'''

# import re,requests,csv


# url = 'https://movie.douban.com/top250?start=50&filter='

# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
# }

# res = requests.get(url,headers=header)
# page_content = res.text

# obj= re.compile(
#     r'<li>.*?<span class="title">(?P<name>.*?)</span>'
#     r'.*?<div class="bd">.*?<br>(?P<year>.*?)&nbsp'
#     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
#     r'.*?<span>(?P<num>.*?)人评价</span>'
#     ,re.S
# )

# result = obj.finditer(page_content) 
# f = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\data.csv',mode='a',encoding='utf-8')
# csvwrite = csv.writer(f)
# for it in result :
#     # print(it.group('name'))
#     # print(it.group('year').strip())
#     # print(it.group('score'))
#     # print(it.group('num'))
#     dic = it.groupdict() # 将正则表达式获取的内容与其group名存为字典，key是group名，value是正则获得的内容
#     dic['year'] = dic['year'].strip()
#     csvwrite.writerow(dic.values()) # .writerow(dic.values()) 将参数的值以csv的格式写在一行
# f.close()
# print('over')
# res.close()


"""" 天影天堂爬取 使用bs4"""
import requests,csv,time,os
from bs4 import BeautifulSoup
# 使用request获取网页内容
url = 'https://dy.dytt8.net/index2.htm'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}
res = requests.get(url,headers=header)
res.encoding = 'gbk'

# 使用bs4进行数据解析

page = BeautifulSoup(res.text,'html.parser')

a_lists = page.find('div',attrs={'class':"co_content2"}).find_all('a')[1:]

for a in a_lists:
    # 获取子页面的url，并对子页面进行解析
    child_url = 'https://dy.dytt8.net' + a.get('href')
    child_res = requests.get(child_url)
    child_res.encoding = 'gbk'
    child_res_text = child_res.text
    
    child_page = BeautifulSoup(child_res_text , 'html.parser')
    img_lists = child_page.find('div',attrs={'id':'Zoom'}).find('img')
    img_url = img_lists.get('src')
    img_content = requests.get(img_url)
    img_name = img_url.split('/')[-1]
    
    with open(os.path.join(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\img_bs4',img_name),'wb') as f:
        f.write(img_content.content)
    print('over' , img_name)
    time.sleep(1)
    child_res.close()
print('all over!!!')
res.close()









