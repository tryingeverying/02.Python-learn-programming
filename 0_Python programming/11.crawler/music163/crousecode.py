from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get('https://music.163.com/#/discover/playlist')

print(driver,page_sourse)
# 打印返回结果，判断网页访问是否成功