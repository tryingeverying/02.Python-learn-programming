'''
采用多线程通过面向对象的方法获取数据接口解析小米应用商店里的消息
'''

import requests 
from requests.exceptions import RequestException
import time
import csv
import threading
from queue import Queue

app_data = []
class XiaomiShop():
    def __init__(self) -> None:
        self.url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=6&pageSize=30'
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
        'Cookie':'t_id=noimeiweb_5b2c6e3e-1db5-4752-be0c-994d2fc3f87a; Hm_lvt_765fefc2c357bae3970cea72e714811b=1697383462; __utma=127562001.1723608702.1697383462.1697383462.1697383462.1; __utmc=127562001; __utmz=127562001.1697383462.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_765fefc2c357bae3970cea72e714811b=1697383757; JSESSIONID=8C40BC78EE94B904673BA968C3EA01D6',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'https://app.mi.com/category/6'
    }
        # 创建队列
        self.q = Queue()
        # 创建线程锁
        self.lock = threading.Lock()
        self.app_data = []

    def put_url(self):
        '''把目标url放入队列'''
        for page in range(3):
            new_url = self.url.format(page)
            # 创建队列
            self.q.put(new_url)

    def get_one_page_data(self,url):
        '''获取单个链接中的数据信息'''

        response = requests.get(url,headers=self.headers)
        try :
            if response.status_code == 200:
                return response
        except RequestException as e:
            print(f'网页获取失败,出现{e}错误')


    def parse_page(self,json_text):
        '''解析获得的json数据，提取需要的数据'''
        res_list = json_text.get('data')
        data_list = []
        # return (res_list)
        for i in res_list:
            aim_data = {}
            # pic_data['date'] = i['descr']
            aim_data['name'] = i.get('displayName')
            aim_data['category'] = i.get('level1CategoryName')
            aim_data['url'] = 'https://app.mi.com/details?id=' + i.get('packageName')

            data_list.append(aim_data)
        return data_list

    def write_to_csv(self,data,header):
        '''将获取的信息写入csv文件中'''
        with open(r'test_project\res\csv\threadxiaomishop.csv','a',encoding='utf-8',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=header)
            if i == 0:
                # 只有全局变量i等于第一个迭代值的时候才写入header
                writer.writeheader()
            writer.writerows(data)

    # 发起请求，获取响应，解析数据
    # 创建并启动多线程的时候调用这个函数，把可能出现资源争抢的内容放入这个函数
    def parse_url(self):
        '''使用多线程的方法爬去所需数据'''
        while True:
            # 把线程上锁
            self.lock.acquire()
            # 队列不空则进入后面的程序
            if not self.q.empty():
                # 获取队列中的第一个url
                url = self.q.get()
                # 取出后就和队列无关了，需要解锁
                self.lock.release()
                header = ('name','category','url')
                json_text = self.get_one_page_data(url).json()
                data = self.parse_page(json_text)
                self.write_to_csv(data,header)
            else:
                # 在else处也要进行解锁，否则会在上锁状态堵塞
                self.lock.release()
                break

    def main(self):
        # 调用函数把需要处理的url放入队列
        self.put_url()
        # 定义一个全局变量，确保header只写入一次
        global i
        # 创建2个多线程，如果线程多的话，可以放到列表里，逐个取出
        thread_list = []
        for i in range(2):
            t = threading.Thread(target=self.parse_url)
            thread_list.append(t)
            t.start()

        print('done')

if __name__ == "__main__":
    start_time = time.time()
    xiaomi = XiaomiShop()
    xiaomi.main()
    end_time = time.time()
    print('程序运行时间：%s' % (end_time - start_time))