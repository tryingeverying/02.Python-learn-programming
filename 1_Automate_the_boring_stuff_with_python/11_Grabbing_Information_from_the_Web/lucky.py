#! python3
# 在命令行中输入查找主题，让计算机自动打开浏览器，在新的选项卡中显示前面几项查询结果

import requests, sys, webbrowser, bs4, logging ,xml

print("bing searching")

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s  - %(message)s")
if len(sys.argv) > 1:
    logging.debug(f"此时传入的参数为{sys.argv[1]}")
    # 使用requests获取网址信息
    res = requests.get('https://cn.bing.com/search?q=' + ' '.join(sys.argv[1:]))
    logging.debug(f"此时的res为{res}")
    try:
        res.raise_for_status()
    except Exception as error:
        print(f'程序出现问题:{error}')
    
    # 使用bs4解析网址
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    linkelems = soup.select(r"#b_results .b_algo")
    # linkelems = soup.select(r"#b_results > li.b_algo.b_vtl_deeplinks > h2 > a")
    logging.debug(f"此时的linkelems的数量为{len(linkelems)}{linkelems}")
    
    numopen = min(2,len(linkelems))
    # for i in range(numopen):
    #     webbrowser.open(linkelems[i].get("href"))







else:
    print("请输入要检索的参数")
    



