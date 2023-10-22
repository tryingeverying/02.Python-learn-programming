'''
爬起中国天气网(http://www.weather.com.cn/textFC/hb.shtml)
的各个省份城市的最低气温信息，并将之写入到一个csv文件中
'''



import requests
from bs4 import BeautifulSoup
import time 
from requests.exceptions import RequestException
import csv

def get_one_page(url):
    """获取单个网页中的信息"""
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43'
    }

    response = requests.get(url,headers=headers)
    try:
        if response.status_code == 200:
            html = response.content.decode('utf-8')
            return html
    except RequestException as e:
        print(f'网页获取失败,出现{e}错误')
    

def parsing_data(html):
    '''从获取的网页信息中获取需要的数据'''
    weaSoup= BeautifulSoup(html,features='html5lib')

    # 获取数据所在的区块
    div_class = weaSoup.find(attrs={'class', 'conMidtab'})

    # 定义一个list用以存放每个城市的天气信息
    city_list = []

    # 在上面定位的区块下进一步获取每一个省份的数据区块
    tables = div_class.find_all('table')

    # 遍历所有的省份区块信息，从而获取其中的地级市的天气信息
    for table in tables:
        # 获取每个table标签下代表城市的tr标签，tr标签的前两个是表头和日期，故洗去
        tr_tags = table.find_all('tr')[2:] 
        # city_data = {}
        # 从每个tr标签里获取需要的城市名，天气情况，最低气温等信息
        for index, tr in enumerate(tr_tags):

            # 定义一个字典用以存放每个城市的具体信息
            # 字典必须放到遍历每个城市具体信息的循环里面，
            # 如果到外面的循环会导致每次字典不重置，而list的append存储的是指针，
            # 因此后面list中存储的值每一次都会改变因此会导致只写入了每一个table中的最后一个值
            # 可以手工写一个程序验证一下
            city_data = {}

            # 从代表城市的tr标签中获取含有具体信息的td标签
            td = tr.find_all('td')

            # 如果是列表中的第一个则td的第一个text是省份名，第二个值才是省会名，故有下面的判断
            if index == 0:
                city = list(td[1].stripped_strings)[0]
            # stripped_strings：用来获取目标路径下所有的子孙非标签字符串，
            # 会自动去掉空白字符串，返回的是一个生成器
            # 如果获取到的是生成器，一般都是把它转换成list，不然你看不出那是什么玩意
            # 具体信息详见该网页https://blog.csdn.net/qq_22592457/article/details/100597190
            
            else:
                city = list(td[0].stripped_strings)[0]
            maxTemp = list(td[-5].stripped_strings)[0]   
            weaPheno = list(td[-4].stripped_strings)[0]
            minTemp = list(td[-2].stripped_strings)[0]
            
            # 存储单个城市的天气信息
            city_data['city'] = city
            city_data['maxTemp'] = maxTemp
            city_data['weaPheno'] = weaPheno
            city_data['minTemp'] = minTemp

            # 将每个城市的所有天气信息放入list中
            city_list.append(city_data)
    return city_list


def write_to_csv(city_list,header):
    '''将得到的数据写入csv文件'''
    with open(r'test_project\res\csv\weather.csv','a',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        if i == 1:
            writer.writeheader()
        writer.writerows(city_list)


def main():
    regions = ['hb','db','hd','hz','hn','xb','xn','gat']
    global i

    for i in regions:
        time.sleep(3)
        url = f'http://www.weather.com.cn/textFC/{i}.shtml'
        html = get_one_page(url)
        city_list = parsing_data(html)
        header = ('city','maxTemp','weaPheno','minTemp')
        write_to_csv(city_list,header)

if __name__ == "__main__":
    main()

