'''使用selenium控制浏览器爬取猫眼电影top100(https://www.maoyan.com/board/4?offset=0)'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv

# def configuration_driver():
option = webdriver.ChromeOptions()
# 设置无界面功能
# ---headless 浏览器无界面
# option.add_argument('---headless')
# 浏览器常开
option.add_experimental_option("detach", True)
# 配置浏览器设置
# 关闭自动化测试窗口
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('disable-infobars')
# 屏蔽保存密码提示框
prefs = {'credentials_enable_service':False,'profile.password_manager_enabled':False}
option.add_experimental_option('prefs',prefs)
# 反爬虫特性处理
option.add_argument('--disable_blink_features=AutomationControlled')
# 传入配置信息
driver = webdriver.Chrome(options=option)


def get_data():
    '''获取每一个电影的数据'''
    dd_tags = driver.find_elements(By.CSS_SELECTOR,'#app > div > div > div.main > dl > dd')
    info_list = []
    for dd_tag in dd_tags:
        dict_dd = {}
        list_dd = dd_tag.text.split('\n')
        # list_dd ['1', '我不是药神', '主演：徐峥,周一围,王传君', '上映时间：2018-07-05', '9.6']
        index_header = ['排名','电影名','主演','上映时间','评分',]
        index_key = range(5)
        # 从list_dd中依次取出放入字典中
        for t,i in zip(index_header ,index_key):
            dict_dd[t] = list_dd[i]
        # 将获取的单个电影的信息放入list
        info_list.append(dict_dd)
    # 返回的list存储的电影的信息，index_title用作csv的表头
    return info_list, index_header

def write_to_csv(data,index_header):
    '''将解析得到的数据写入csv文件'''
    with open(r'test_project\res\csv\maoyan.csv','a',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=index_header)
        writer.writeheader()
        writer.writerows(data)

def main():
    driver.get('https://www.maoyan.com/board/4?offset=0')
    time.sleep(1)
    _, index_header = get_data()

    # 定义一个计数器用于显示爬取的页码
    i = 1
    while True:
        # 写一个循环，自动跳转到下一页，
        # 因为跳转到下一页url以及其中的电影信息会发生改变，so要在循环内调用
        info_list, _ = get_data()
        write_to_csv(info_list,index_header)
        time.sleep(2)
        try:
            # for i in range(1,100)
            if driver.find_element(By.LINK_TEXT,'下一页'):
                driver.find_element(By.LINK_TEXT,'下一页').click()
                print(f"正在爬取第{i}页的数据")
                i += 1
            time.sleep(3)
        except:
            print('done')
            driver.quit()
            break

if __name__ == "__main__":
    main()