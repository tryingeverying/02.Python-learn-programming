# import requests ,os
# from bs4 import BeautifulSoup

# url='https://xkcd.com'
# os.makedirs('xkcd',exist_ok=True)   #exist_ok=True 如果文件存在则不会报错
# while not url.endswith('#'):
#     print('downloading page %s' % url)
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text)
    
#     comicelem = soup.select('#comic img') # #后面跟的是ID属性
    
#     if comicelem == []:
#         print('未发现图片')
#     else:
#         comicurl = 'http:' + comicelem[0].get('src')

#         print('downloading images %s' % (comicurl))
#         res = requests.get(comicurl)

#         imagefile = open(os.path.join('xkcd',os.path.basename(comicurl)),'wb')
#         for chunk in res.iter_content(100000): #写入的文件最大是100000字节，写入后关闭文件
#             imagefile.write(chunk)
#             imagefile.close()
#     prevlink = soup.select('a[rel ="prev"]')[0]
#     url = 'http://xkcd.com' + prevlink.get('href')

# print('done')
# res.close()



import requests,os
from bs4 import BeautifulSoup

url = 'https://xkcd.com'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}


if  not os.path.exists('xkcd') :
    os.makedirs('xkcd')

while not url.endswith('#'):
    res = requests.get(url,headers=header)
    soup = BeautifulSoup(res.text,'html.parser')
    img_elem = soup.find('div',attrs={'id':"comic"}).find('img')
    
    if img_elem == [] :
        print('图片信息不存在')
    else:
        img_url = 'https:' + img_elem.get('src')
        print(f'正在下载图片{img_url}')
        child_res = requests.get(img_url)
        img_file = open(os.path.join('xkcd',os.path.basename(img_url)),'wb')
        for chunk in child_res.iter_content(1000000):
            img_file.write(chunk)
            img_file.close()
    prev_soup = soup.find('a',attrs={'rel':"prev"})
    url = 'https://xkcd.com' + prev_soup.get('href')

print('下载完毕')
res.close()



