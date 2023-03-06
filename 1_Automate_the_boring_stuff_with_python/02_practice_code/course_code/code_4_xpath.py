'''获取58二手房信息'''
# import requests
# from lxml import etree

# url = 'https://www.58.com/ershoufang/' 
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
# }

# res = requests.get(url,headers=header)
# res.encoding = 'utf-8'

# tree = etree.HTML(res.text)
# f = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\58.txt','w',encoding = 'utf-8')
# li_list = tree.xpath('//div[@class= "cb"]//tr') # // 表示从根目录开始，但是省略了若干目录，用@[属性值]来定位属性。// 省略若干目录
# for li in li_list:
#     title = li.xpath('./td[2]/a/text()')[0] #因为不是从根目录开始抓取的。所以要用.开头，类似于os里.代表当前目录
#     f.write(title + '\n')
# f.close()
# res.close()

'''4k图片爬取,因为反爬的原因爬取失败'''
# import requests
# from lxml import etree

# url = 'https://pic.netbian.com/4kfengjing/'
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
#     'Referer':'https://pic.netbian.com'
# }
# res = requests.get(url,headers=header)
# res_text = res.text
# print(res_text)
# tree = etree.HTML(res_text)

# li_lists = tree.xpath('//div[@id="main"]/div[3]/ul/li')
# for li in li_lists:
#     img_url = 'https://pic.netbian.com/4kfengjing' + li.xpath('./a/img/@src')[0]
#     print(img_url)
# res.close()


''' 全国城市爬取'''
# import requests
# from lxml import etree
# url = 'https://www.aqistudy.cn/historydata/'
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
#     'Referer':'https://www.aqistudy.cn'
# }
# res = requests.get(url,headers=header)
# res_text = res.text

# tree = etree.HTML(res_text)
# all_city_name = []
# li_lists = tree.xpath(' //div[@class="bottom"]//li/a ')
# for li in li_lists:
#     city_name = li.xpath('./text()')[0]
#     all_city_name.append(city_name)
# print(all_city_name,len(all_city_name))
# res.close()

'''站长素材简历爬取'''

# import requests,os,time
# from lxml import etree

# url = 'https://sc.chinaz.com/jianli/free.html'

# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
#     'Referer':'https://sc.chinaz.com'
# }

# res = requests.get(url,headers=header)
# res.encoding = 'utf-8'

# tree = etree.HTML(res.text)
# child_urls = tree.xpath('//div[@id="main"]//p/a')
# down_path = r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\简历'
# if not os.path.exists(down_path):
#         os.mkdir(down_path)
# for li in child_urls:
#     child_url = 'http:' + li.xpath('./@href')[0]
#     child_res = requests.get(child_url,headers=header)
#     child_res.encoding = 'utf-8'
#     child_tree = etree.HTML(child_res.text)
#     download_lists = child_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a')[0]
#     download_url = download_lists.xpath('./@href')[0]
#     content = requests.get(download_url)
#     file_name = download_url.split('/')[-1]
#     with open(os.path.join(down_path,file_name),'wb') as f:
#         f.write(content.content)
#     print('over' + file_name)
#     time.sleep(1)
#     child_res.close()
# print('all over')
# res.close()

