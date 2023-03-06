import requests
from bs4 import BeautifulSoup

r = requests.get('https://search.bilibili.com/all?keyword=python&from_source=webtop_search&spm_id_from=333.851')
# print(r.text)

soup = BeautifulSoup(r.text,'html.parser')

soup.select('li.video-item.matrix')


















