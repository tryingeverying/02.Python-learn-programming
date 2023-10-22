'''
获取豆瓣排名前100的电影信息
'''
import requests
from bs4 import BeautifulSoup
import time
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            'Cookie':'ll="118323"; bid=X3K6tu8ZSFg; gr_user_id=21e2ef27-f67f-4cab-8ac5-96d4f9554749; __utmv=30149280.17478; _vwo_uuid_v2=DAE7F280B0C7F8818E5FF5D1CA40C3AD5|55fe8c0e36941ddb4354b48b41728560; _pk_id.100001.4cf6=71eb22faf78caec2.1667632105.; viewed="30175598_27061630_4882056_4233354_26883450_26851683_35501177_25947310_30411849_1032803"; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1694876017; loc-last-index-location-id="118323"; _vwo_uuid_v2=D8F4622458BF7E057FFC082FBF09E460D|714bb46f7b46955dc9f32bf92cc9ff98; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1694952434%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.2039379131.1664245339.1694875989.1694952434.51; __utmb=30149280.0.10.1694952434; __utmc=30149280; __utmz=30149280.1694952434.51.10.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.679551200.1667632105.1694875993.1694952434.8; __utmb=223695111.0.10.1694952434; __utmc=223695111; __utmz=223695111.1694952434.8.6.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="174787235:/ceju6+AYLo"; ck=TR8_; push_noty_num=0; push_doumail_num=0',
            'Host':'movie.douban.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81'
        }
        
        response = requests.get(url,headers=headers )
        if response.status_code == 200:
            # return response.text
            resSoup = BeautifulSoup(response.text,features='lxml')
            numElems = resSoup.select('#content > div > div.article > ol > li > div > div.pic > em')
            titleElems = resSoup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            directorElems = resSoup.select("#content > div > div.article > ol > li > div > div.info > div.bd > p:nth-child(1)")
            return numElems, titleElems, directorElems
    except RequestException:
        return None

def write_to_file(content):
    with open(r'F:\Programming\02.Python-learn-programming\6_Python3_Web_Crawler_Development_Practice\Chapter_3_Using_the_Basic_Library\res_file\douban_ressult.txt', 'a', encoding='utf-8', ) as f:
        f.write(content + '\n')

def main():
    for i in range(0,100,25):
        url = 'https://movie.douban.com/top250?start='+str(i)+'&filter='
        num,title,director = get_one_page(url)
        time.sleep(0.5)
        for i,j,k in zip(num,title,director):
            write_to_file(' '.join([i.getText(),j.getText(),k.getText().replace(' ','').replace('\n','\t')]))
            # print([i.getText(),j.getText(),k.getText().strip()])
    print('Done')

if __name__ == "__main__":
    main()