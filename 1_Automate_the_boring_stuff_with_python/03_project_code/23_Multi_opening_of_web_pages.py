# ! python3
# 同时打开必应搜索的前五个网页

import requests,sys,bs4,webbrowser


# 使用requests模块获取信息
print('同时打开百度搜索的前五个网页')
res = requests.get('https://www.baidu.com/search?wd=' + ' '.join(sys.argv[1:]))
if res.status_code != 200:  #判断网页是否获取成功，成功的状态码是200'
    print('获取网页失败')

# 获取网页链接
bd_soup = bs4.BeautifulSoup(res.text,'html.parser')
linkelems = bd_soup.select('#container a')
print(bd_soup)
print(len(linkelems))

# 打开网页链接
numopen = min(5,len(linkelems))
for i in range(numopen):
    urlToOpen = 'https://www.baidu.com/search?wd=' + linkelems[i].get('href')
    print('opening', urlToOpen)
    webbrowser.open(urlToOpen)

























