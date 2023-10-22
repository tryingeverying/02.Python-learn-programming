from bs4 import BeautifulSoup
import requests
import time
from requests.exceptions import RequestException

def get_one_page(url):
    # 获取单个网页的内容
    try:
        headers = {
            'Cookie':'__mta=218862886.1694871369124.1695003216114.1695003220359.9; uuid_n_v=v1; uuid=FDCD6220549511EE8918A55CEC0D870985BAF6C6B9B84C779081F3D1293B4FF6; _lxsdk_cuid=18a9e34b412c8-0c649f3422ae51-7f5d5476-144000-18a9e34b412c8; _csrf=1d1adea316bce669acd084454bb721c9a056bc9e0af29bea8adeb44b6fcc614b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1694871369,1694952415; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk=FDCD6220549511EE8918A55CEC0D870985BAF6C6B9B84C779081F3D1293B4FF6; __mta=218862886.1694871369124.1694952415441.1695001719822.7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1695003220; _lxsdk_s=18aa5f9b307-28f-72c-c91%7C%7C8',
            'Host':'www.maoyan.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            resSoup = BeautifulSoup(response.text,features='lxml')
            titleElems = resSoup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.name > a')
            return titleElems
    except RequestException:
        return 'error'
    
def write_to_file(content):
    with open(r'F:\Programming\02.Python-learn-programming\6_Python3_Web_Crawler_Development_Practice\Chapter_3_Using_the_Basic_Library\res_file\maoyan_result.txt','+a',encoding='utf-8') as f:
        f.write(content + '\n')

def main():
    for i in range(0,100,10):
        new_url = 'https://www.maoyan.com/board/4?offset=' + str(i)
        time.sleep(0.2)
        title = get_one_page(new_url)
        for i in title:
            write_to_file(i.getText())
    print('Done')
    
if __name__ == "__main__":
    main()








