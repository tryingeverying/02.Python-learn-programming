# # 抓取搜狗首页的信息
# import requests

# url='https://www.sogou.com/'
# res = requests.get(url=url)
# if res.status_code != 200:
#     print('获取成功')

# page_text = res.text
# print(page_text) 

# with open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code\sogou.html','w',encoding='utf-8') as fp:
#     fp.write(page_text)
# print('获取成功')


# 添加User—Agent爬取指定关键词的搜索结果
# import requests,os

# header = {
#     'User Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
#     }
# kw = input('请输入待搜索的关键词：')
# url = 'https://www.sogou.com/web?query=' + kw

# res=requests.get(url , headers=header)

# page_text = res.text
# filename = kw + '.html'
# treepath=r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code'
# with open(os.path.join(treepath,filename),'w',encoding='utf-8') as fp:
#     fp.write(page_text)
# print(filename,'保存成功')

# 抓取数据包来实现数据的获取
# import requests,json
# # 指定url
# post_url='https://fanyi.baidu.com/sug'
# # 使用UA伪装
# header={
#     'User Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'   
# }
# # 请求参数
# word = input('输入一个单词') 
# data = {
#     'kw':word
# }
# # 请求发送
# res = requests.post(url = post_url,data= data, headers= header)

# dict_obj = res.json()# 响应类型是json的才能使用.json()其他的情况下还是要用.text（
# # 存储
# filename = word + '.json'
# fp = open(filename,'w',encoding = 'utf-8')
# json.dump(dict_obj,fp=fp ,ensure_ascii=False)

# print('over!')


# 还是抓的数据包不对
import requests,json
url='https://movie.douban.com/j/chart/top_list'

param = {
    'type': '24',
    'interval_id':' 100:90',
    'action':'',
    'start': '0',
    'limit': '20',
}

header={
     'User Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'   
 }

res = requests.get(url=url,params =param,headers=header)

list_data = res.json()

fp = open('./douban.txt','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)

print('over!')






