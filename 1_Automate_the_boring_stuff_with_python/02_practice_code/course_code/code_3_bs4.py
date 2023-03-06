# # 和教程类似的网址的数据获取
# import csv,requests
# from bs4 import BeautifulSoup

# # 使用requests模块获取网页信息
# url = 'http://zhongdapeng.com/shucaijiage/964.html'

# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
# }
# res = requests.get(url,headers= header)
# res.encoding='utf-8'
# # 将网页信息交由bs4处理
# page = BeautifulSoup(res.text,"html.parser")
# table = page.find('table',attrs={'cellpadding':"0" ,'cellspacing':"0", 'height':"603" ,'width':"562"})
# # 创建存储信息的csv文件
# f = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\每日菜价.csv',mode='w',encoding = 'utf_8',)
# csvwrite = csv.writer(f)
# # 定位存储每个蔬菜信息的标签
# trs = table.find('tbody').find_all('tr')[1:] #只有在这个地方把tr标签给变成list才能在后面使用列表提取
# # 单独取出每个蔬菜的信息
# for tr in trs:
#     tds = tr.find_all('td')
#     num = tds[0].text
#     kind = tds[1].text
#     yesterday_price = tds[2].text
#     tody_price = tds[3].text
#     change_num = tds[4].text
#     # print(num,kind,yesterday_price,tody_price,change_num)
#     csvwrite.writerow([num,kind,yesterday_price,tody_price,change_num])

# f.close()
# print('over')
# res.close()




# import requests,csv
# from bs4 import BeautifulSoup

# #通过request获取网页信息
# url = 'http://www.vegnet.com.cn/Price/list_ar110000.html?marketID=30'
# header = {
#  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
# }
# res = requests.get(url,headers=header)

# # 使用bs4解析request获取的网页信息 生成bs对象
# page_content = BeautifulSoup(res.text,'html.parser')
# # print(page_content)
# # 从bs对象中查找数据
# #div = page_content.find('div',class_="jxs_list price_l") # 因为class在python中是关键词，bs4为了做区分可以在class后面加_来加以区分
# div = page_content.find('div',attrs={'class':"jxs_list price_l"}) #也可以用这种写法替代上面的class_
# #获取所有的数据行
# p = div.find_all('p')[1:]

# # 将数据存储到csv文件中
# f = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\菜价.csv',mode='w',encoding = 'utf-8')
# csvwriter = csv.writer(f)
# for spans in p:
#     span = spans.find_all('span')# 
#     # result =[i.get_text() for i in span] # 遍历所有的span，使用.get_text()获取每个span里的数据
#     # csvwriter.writerow(result)
#     kind = span[1].text
#     lowest_price = span[3].text
#     highest_price = span[4].text
#     average_price = span[4].text
#     # print([kind,lowest_price,highest_price,average_price])
#     csvwriter.writerow([kind,lowest_price,highest_price,average_price])
# print('over')
# f.close()
# res.close()



# import requests , os ,time
# from bs4 import BeautifulSoup

# url = 'http://bizhi360.com/weimei/'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
# }

# res = requests.get(url , headers=header)
# res.encoding= "UTF-8"

# page = BeautifulSoup(res.text,'html.parser')
# a_list = page.find('div',attrs={'class':"pic-list"}).find_all('a')

# for a in a_list:
#     href = ('http://bizhi360.com/' + a.get('href')) # 可以通过get方法获得对应的属性值，因为得到的不是完整的网页地址，所以自己拼接
#     child_res = requests.get(href) 
#     child_res.encoding = 'utf-8'
#     child_res_text = child_res.text
#     child_page = BeautifulSoup(child_res_text,'html.parser')
#     img = child_page.find('div',attrs={'id':"main"}).find('img')
#     # 获取图片的下载地址
#     src = img.get('src')

#     # 下载图片
#     img_res = requests.get(src)
#     img_name = src.split('/')[-1] 
#     with open(os.path.join(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\img',img_name),'wb') as f:
#         f.write(img_res.content)
#     print('over' , img_name)
#     time.sleep(1)
#     child_res.close()

# print('all over !!!')
# res.close()

''' 使用抓取数据包的方式获取新发地的菜价信息'''

# import requests,json 

# url = 'http://www.xinfadi.com.cn/getCat.html'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
# }
# res = requests.post(url,headers=header)

# f = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\菜价_抓包.json','w',encoding='utf-8')
# json.dump(res.json(),fp= f,ensure_ascii=False)
# print('over')
# f.close()
# res.close()

'''获取三国演义的章节名称'''
import requests,os
from bs4 import BeautifulSoup

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}
res = requests.get(url,headers=header)
res.encoding='utf-8'
page = BeautifulSoup(res.text,'lxml')
li_lists = page.select('.book-mulu > ul > li') #可以用 空格实现跳层，即不用一层一层往下走

f = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\三国.txt','w',encoding='utf-8')
for li in li_lists:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com' + li.a['href']
    child_res = requests.get(detail_url,headers=header)
    child_res.encoding = 'utf-8'
    child_res_text = child_res.text
    child_page = BeautifulSoup(child_res_text,'lxml')
    child_tag = child_page.find('div',class_ = 'chapter_content')
    content = child_tag.text
    f.write(title + ':' + content + '\n')
    print(title,'爬取成功')
    child_res.close()
f.close()
res.close()





