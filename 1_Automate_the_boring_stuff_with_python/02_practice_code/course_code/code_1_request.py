'''获取搜狗检索内容'''
# import requests

# query = input('输入搜索词条：')

# url = f'https://www.sogou.com/web?query={query}' 
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
# }
# res = requests.get(url,headers=header )
# print(res.text)


'''获取百度翻译的英译中'''
# import requests
# url = 'https://fanyi.baidu.com/sug'

# valu = input('请输入要翻译的的英文单词：')

# dat ={
#     'kw' : valu
# }

# # 发送post请求的数据必须放在字典中
# res = requests.post(url,data=dat)
# print(res.json()) #使用text得到的数据是未经转码的数据，所以使用json进行转码


'''获取豆瓣电影喜剧分类的数据'''
# import requests,json
# url = 'https://movie.douban.com/j/chart/top_list'

# param = {
#     'type': '24',
#     'interval_id': '100:90',
#     'action':'', 
#     'start': 0,
#     'limit': 40
# }

# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
#  }

# res = requests.get(url,params=param,headers=header)
# list_data = res.json()

# fp = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code/douban.txt','w',encoding='utf-8')
# json.dump(list_data,fp=fp,ensure_ascii=False)

# print(res.json())
# res.close() # 关闭访问链接


'''获取一地KFC的店铺位置'''
import requests,json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

location = input('请输入待查询的城市')
kw = {
    'cname': '',
    'pid': '',
    'keyword': location,
    'pageIndex': 1,
    'pageSize': 10
    }
header = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
}

res = requests.post(url , data= kw , headers=header)
list_data = res.json()

fp = open(r'F:\Programming\Python\1_Automate_the_boring_stuff_with_python\course_code/KFC.txt','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)

print(res.json())
res.close() # 关闭访问链接







