'''适用于selenium控制浏览器访问12306,自动化订票'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import csv
import time

class TrainSpider():
    '''定义初始化方法，在实例化的对象的时候把三个参数传入'''
    def __init__(self,from_station,to_station,train_date,ticket_info,passengers) -> None:
        '''
        :param from_station: 出发地
        :param to_station: 目的地
        :param train_date: 出发日期
        :param ticket_info: 车次以及坐席信息
        :param passenger: 乘车人
        '''
        self.from_station = from_station
        self.to_station = to_station
        self.train_date = train_date
        self.ticket_info = ticket_info
        self.passengers = passengers
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        # 配置浏览器设置
        # 关闭自动化测试窗口
        self.option.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.option.add_experimental_option('useAutomationExtension', False)
        self.option.add_argument('disable-infobars')
        # 屏蔽保存密码提示框
        self.prefs = {'credentials_enable_service':False,'profile.password_manager_enabled':False}
        self.option.add_experimental_option('prefs',self.prefs)
        # 反爬虫特性处理
        self.option.add_argument('--disable_blink_features=AutomationControlled')
        # 传入配置信息
        self.driver = webdriver.Chrome(options=self.option)
        

        # 第一步登录的url
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        # 第一步个人界面的url
        self.person_url = 'https://kyfw.12306.cn/otn/view/index.html'
        # 第二步查票的url
        self.query_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        # 第四步确认信息的url
        self.confirm_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        
        # 存放字典和代号，可以跨函数调用，相当于全局，有站台名称可以随时调用
        self.stations_dict = {}
        # 初始化stations_dict，调用stations_code函数
        self.stations_code()
        self.select_info = None
        
    def stations_code(self):
        '''得到站台及其对应代号的字典'''
        with open(r"test_project\res\csv\stations_code.csv",'r',encoding='utf-8') as f:
            read_data = csv.DictReader(f)
            for line in read_data:
                name = line['车站']
                code = line['代号']
                self.stations_dict[name] =code

    def logib(self):
        '''实现登录'''
        self.driver.get(self.login_url)
        # 显示等待，直到网页跳转成功，即url改变
        WebDriverWait(self.driver,1000).until(
            EC.url_contains(self.person_url)
        )
        print('登录成功')

    def query_ticket(self):
        '''查询传入参数的需要的车片'''
        self.driver.get(self.query_url)
        self.driver.implicitly_wait(2)
        # 设定关于出发地的信息
        from_station_input = self.driver.find_element(By.ID,value='fromStation')
        from_station_code = self.stations_dict(self.from_station)
        # 设定关于目的地的信息
        to_station_input = self.driver.find_element(By.ID,value='toStation')
        to_station_code = self.stations_dict(self.to_station)
        # 设定关于出发日期的信息
        date_input = self.driver.find_element(By.ID,value='train_date')
        date_code = self.stations_dict(self.train_date)

        # 执行JS把需要查询的信息传入
        self.driver.execute_script('arguments[0].value="{}";arguments[1].value="{}";arguments[2].value="{}";'.format(from_station_code,to_station_code,self.train_date),from_station_input,to_station_input,date_input)

        # 点击查询
        self.driver.find_element(By.ID,value='query_ticket').click

        # 显示等待，直到出现检索结果的信息框
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#queryLeftTable'))
        )
        # 获取车次列表
        # 过滤掉无效的tr标签，tr标签有两种，一种含有车次信息，一种无车次信息
        train_trs = self.driver.find_element(By.XPATH,'.//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        
        # 定义标志位，用来判断是否找到用户需要购买的车次和坐席，如果找到就改为True
        # False的默认值为0
        flag = False
        for train_tr in train_trs:
            train_infos = train_tr.text.replace('\n',' ').split(' ')
            # 移除掉车次信息中的无用信息，复兴号的简写"复"
            if train_infos[1] == "复":
                train_infos.remove("复")
                # 车次号就是train_infos列表的第一个值
            train = train_infos[0]
            if train in self.ticket_info:
                # 如果该车次为查询的车次，则获取后面的信息
                seat_types = self.ticket_info[train]
                # 遍历坐席类型
                for seat_type in seat_types:
                    if seat_type == 'O':
                    # 如果seat_type等于O，判断二等座是否有票
                    # 检查二等座对应的位置是否有余票
                        o_count = train_infos[9]
                        # 判断二等票的位置的内容是 “有”或者是数字
                        if o_count == '有' or o_count.isdigit():
                            
                            self.select_info = seat_type
                            # 如果找到了，就把标志位改为True
                            flag = True
                            # 退出判断坐席有无的操作
                            break
                    elif seat_type == 'M':
                        m_count = train_infos[8]
                        if m_count == '有' or m_count.isdigit():
                            
                            self.select_info = seat_type
                            # 如果找到了，就把标志位改为True
                            flag = True
                            # 退出判断坐席有无的操作
                            break
                if flag :
                    train_tr.find_element(By.CSS_SELECTOR,'//a[@class = "btn72"]').click()
                    # 如果找到了就进行点击
                    break


    def confirm_passengers(self):
        '''确认乘客信息'''
        # 显示等待，判断网页是否跳转成功
        WebDriverWait(self.driver,1000).until(
            EC.url_contains(self.confirm_url)
        )
        # 定位账号中存储的乘车人所在的标签
        passenger_lables = self.driver.find_element(By.XPATH,'//*[@id="normal_passenger_id"]/li/label')
        # 遍历所有乘车人
        for passenger in passenger_lables:
            # 获取乘车人名字，方便后面与传入的参数比较
            name = passenger.text
            if name == self.passengers:
                passenger.click()

        # 定位到席别选择框
        seat_tag = self.driver.find_element(By.ID,'passenger')
        # 把定位到的选择框座位参数传入到Select类里才能进行操作
        seat_select = Select(seat_tag)
        # 上个函数已经把坐席类别传给了self.select_info
        # 之后select通过选定的坐席进行选择
        seat_select.select_by_value(self.select_info)
        # 提交订单
        self.driver.find_element(By.ID,'submitOrder_id').click()

        # 用显示等待 判断核对信息框是否出现,传入核对框的ID。
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.ID, 'content_checkticketinfo_id'))
        )
        # 如果消息框出现，点击确认按钮
        # time.sleep(2)
        self.driver.find_element_by_id('qr_submit_id').click()

    """功能模块的使用，封装基本的功能,如果把登录，查询，确认的内容都写在一个函数里，
    就会特别臃肿，可以封装不同的函数实现不同的功能，在一个函数中进行调用
    so 封装就是把函数在另一个函数中调用????或者说就给外部一个数据接口
    """
    def run(self):
        # 第一步 登录
        self.login()   # 调用函数
        # 第二步 车次及余票的查询，第三步 车票数据解析
        self.query_ticket()
        # 第四步 确认乘客信息和席别
        self.confirm_passengers()

if __name__ == '__main__':
    # 通过创建的类去实例化对象，需要传递三个参数到init里
    # 注意日期的格式 yyyy-xx-xx
    spider = TrainSpider('长沙', '北京', '2021-09-15', {"G534": ['O', 'M']}, ['乘客姓名1', '乘客姓名2'])
    spider.run()
