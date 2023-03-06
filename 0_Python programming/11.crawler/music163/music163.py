from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://music.163.com/#/discover/playlist')

driver.switch_to.frame("contentFrame")

result = []

try:
    ul = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "m-pl-container")))

    li_list = ul.find_elements_by_css_selector('li')

    for li in li_list:
        song_list = {}
        a = li.find_elements_by_css_selector('div.u-cover.u-cover-1 > a.msk')
        song_list['title'] = a[0].get_attribute('title')
        song_list['url'] = a[0].get_attribute('href')

        result.append(song_list)
finally:
    driver.quit()

print(result)