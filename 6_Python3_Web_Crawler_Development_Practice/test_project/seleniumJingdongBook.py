'''使用selenium控制浏览器爬取京东图书(https://book.jd.com/)检索java的数据'''
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

def access_to_search_page():
    '''通过登录进入检索结果网页'''
    input_search = driver.find_element(By.CSS_SELECTOR,value='#key')
    time.sleep(2)
    input_search.send_keys('java')
    search_button = driver.find_element(By.CSS_SELECTOR,value='#search-2014 > div > button')
    time.sleep(2)
    search_button.click()
    # 之后手动扫码进入了检索结果页
    # 等之后技术好了再研究一下自动填账号密码，然后通过验证的方法


def get_data():
    '''获取每一个书籍的数据'''

    li_tags = driver.find_elements(By.CSS_SELECTOR,'#J_goodsList > ul > li')

    # 每一个商品的信息都在一个li中
    info_list = []
    for li_tag in li_tags:
        dict_li = {}
        try:
            dict_li['价格'] = li_tag.find_element(By.CSS_SELECTOR,value='#J_goodsList > ul > li > div > div.p-price > strong').text.strip()
            dict_li['介绍'] = li_tag.find_element(By.CSS_SELECTOR,value='#J_goodsList > ul > li > div > div.p-name.p-name-type-2 > a').text.strip()
            dict_li['评论量'] = li_tag.find_element(By.CSS_SELECTOR,value='#J_goodsList > ul > li > div > div.p-commit > strong').text.strip()
            dict_li['店铺名称'] = li_tag.find_element(By.CSS_SELECTOR,value='#J_goodsList > ul > li > div > div.p-shop > span > a').text.strip()
        
        # 将获取的单个商品的信息放入list
            info_list.append(dict_li)
        except Exception as e:
            print(f"出现错误{e}")
    return info_list

def write_to_csv(data,index_header):
    '''将解析得到的数据写入csv文件'''
    with open(r'test_project\res\csv\jingdongbook.csv','a',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=index_header)
        writer.writeheader()
        writer.writerows(data)

def main():
    driver.get('https://book.jd.com/')
    time.sleep(2)
    access_to_search_page()
    i = 1
    if driver.find_element(By.CSS_SELECTOR,value='#key'):
        print(f"正在爬取第{i}页的数据")
        i+=1
    header = ('价格','介绍','评论量','店铺名称',)
    data = get_data()
    write_to_csv(data,header)
    # 暂时就爬一页

    # while True:
    #     # 写一个循环，自动跳转到下一页，
    #     # 因为跳转到下一页url以及其中的电影信息会发生改变，so要在循环内调用
    #     info_list, _ = get_data()
    #     write_to_csv(info_list,index_header)
    #     time.sleep(2)
    #     try:
    #         # for i in range(1,100)
    #         if driver.find_element(By.LINK_TEXT,'下一页'):
    #             driver.find_element(By.LINK_TEXT,'下一页').click()
    #             print(f"正在爬取第{i}页的数据")
    #             i += 1
    #         time.sleep(3)
    #     except:
    #         print('done')
    #         driver.quit()
    #         break

if __name__ == "__main__":
    main()