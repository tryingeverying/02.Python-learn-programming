'''
爬取新发地菜市场中的菜价，使用数据接口从json数据里爬取
'''

import requests 
from requests.exceptions import RequestException
import time
import csv

def get_one_page_data(i,url):
    '''获取单个链接中的数据信息'''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
        'X-Requested-With':'XMLHttpRequest'
    }
    # data信息来自于数据接口中负载里
    data = {
        'limit': 20,
        'current':{i} ,
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': ''
    }
    response = requests.post(url,headers=headers,data=data)
    try :
        if response.status_code == 200:
            return response
    except RequestException as e:
        print(f'网页获取失败,出现{e}错误')

def parse_page(json_text):
    '''解析获得的json数据，提取需要的数据'''
    data_list = json_text.get('list')

    res_list = []
    for i in data_list:
        res_dict = {}
        # 这个数据的格式是标准的字典，因此用字典的取值方式即可,
        # 原来的.get()方法也可以
        res_dict['编号'] = i.get('id')
        res_dict['一级分类'] = i['prodCat']
        res_dict['二级分类'] = i['prodPcat']
        res_dict['品名'] = i['prodName']
        res_dict['平均价'] = i['avgPrice']
        res_dict['最低价'] = i['lowPrice']
        res_dict['最高价'] = i['highPrice']
        res_dict['产地'] = i['place']
        res_dict['单位'] = i['unitInfo']
        res_dict['规格'] = i['specInfo']
        res_dict['发布日期'] = time.strftime(r"%Y/%m/%d", time.strptime(i['pubDate'], r"%Y-%m-%d  %H:%M:%S"))  
        # time.strptime(i['pubDate'], r"%Y-%m-%d  %H:%M:%S")
        # 意思是将前面的时间数据按照后面的格式转化为一个struct_time对象
        # time.strftime(r"%Y/%m/%d", struct_time) 
        # 意思是把后面的struct_time对象按照前面的数据结构取出
        # 对时间的处理，只保留年月日
        res_list.append(res_dict)
    
    return res_list

def write_to_csv(data,header):
    '''将获取的信息写入csv文件中'''
    with open(r'test_project\res\csv\xinfadi.csv','a',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        if i == 1:
            writer.writeheader()
        writer.writerows(data)

def main():
    global i

    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    for i in range(1,11):
        time.sleep(2)
        json_text = get_one_page_data(i,url).json()
        header = ['编号', '一级分类', '二级分类', '品名', '平均价', '最低价', '最高价', '产地', '单位', '规格', '发布日期', ]
        data = parse_page(json_text)
        write_to_csv(data ,header)
        print(f'正在写入第{i}个链接中的数据')
    print('done')

if __name__ == "__main__":
    main()
