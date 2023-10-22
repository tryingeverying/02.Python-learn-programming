'''
爬取百度贴吧中图片吧每日一图中的图片，使用数据接口从json数据里爬取
'''

import requests 
from requests.exceptions import RequestException
import time
import csv

def get_one_page_data(url):
    '''获取单个链接中的数据信息'''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
        'Cookie':'BDUSS=hqUXV-THJiNU56NnJIaDNkR3h5U0gzd2hVdnVXM3EtaHMwN2ZjTX44ZE4tbGxqSVFBQUFBJCQAAAAAAAAAAAEAAAB4yDdhdG-24LbByukAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE1tMmNNbTJjen; BDUSS_BFESS=hqUXV-THJiNU56NnJIaDNkR3h5U0gzd2hVdnVXM3EtaHMwN2ZjTX44ZE4tbGxqSVFBQUFBJCQAAAAAAAAAAAEAAAB4yDdhdG-24LbByukAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE1tMmNNbTJjen; BIDUPSID=BF8F786065DEBBEF1E5CCC7DA1A24F58; PSTM=1671983185; MCITY=-315%3A; BAIDUID=5846D84877F06E48F1BCBE599AC992AA:FG=1; __bid_n=1876e346915718415a32f1; wapbaikedeclare=showed; BAIDUID_BFESS=5846D84877F06E48F1BCBE599AC992AA:FG=1; STOKEN=593825ed8f7333af2dcf02cbe7868e0927415e69f06546257e06318431fcac4d; BAIDU_WISE_UID=wapp_1696309767630_327; USER_JUMP=-1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1696309767; st_key_id=17; arialoadData=false; ZFY=XPhvQ1LPdVSsv:B:Am5nkNX3SDaGT2L:AvsoDLERINYE6I:C; wise_device=0; XFI=ff494d80-61ab-11ee-82e1-2fffcb4b59ff; XFCS=A1DF65622C2E754C0B0402C056199BC37A141DCB9E0EF565C59DCF97A85CC9C0; XFT=7LFzerOs0kYBO7KbLc4e0kcCgnXudqg9J8pk6x7+uTA=; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_ZjU1MTdiOGRhNDNjNzNkZjFlZGY0ZWE2NjQzMzQ0ZDUwNWY3Y2M5NzY2ZThhMWU1ODU0ZjMzMTMzMzdmMjIyY2RiMDAwODVkNmZkNzc2NTAwZGNmYTZlYzdiNTY4ZmQyNDQzYTc2MzkxZTQzYmQ1YTZjMmRhNTgxMTA5MmVjNGI4MDE1OGI5YjMyNTI1OGE0ZGVjZTI1NDU1MTdjYzQ4NWQyZDc4YzA5YTE4MjcwYjZhOWIxMTdlZTBjODQ4ZGMw; st_data=6d05ba0638ebdd8bd212165197531fe6896c63e0da4936f3f35a150baa39272db1466ad5d726bbfd6bc82e11b7944c04c2fb236114ecb1394a156afe5fdc3125f39883966419aa46758bc03f49764c135940da7aa45240cb37be535ea2008037a86ea62ac42a42d7914d82eabdaa1a36192a4815cb9be3bb16cd3f38531405b506e4e7f6712d9058f2e04e14c8d403c7; st_sign=47aca8cb; RT="z=1&dm=baidu.com&si=f05f1bc1-c5f4-42ce-bdc6-a1c3dc75279c&ss=ln9v1alx&sl=1q&tt=44q9&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1d39g&ul=4b4w3&hd=4b5zj"; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1696317004; BA_HECTOR=2g8ha58ga185al81ah2081ad1ihnfid1p',
        'X-Requested-With':'XMLHttpRequest'
    }
    response = requests.get(url,headers=headers)
    try :
        if response.status_code == 200:
            return response
    except RequestException as e:
        print(f'网页获取失败,出现{e}错误')


def parse_page(json_text):
    '''解析获得的json数据，提取需要的数据'''
    pic_list = json_text.get('data').get('pic_list')
    data_list = []
    # return (pic_list)
    for i in pic_list:
        pic_data = {}
        # pic_data['date'] = i['descr']
        pic_data['date'] = i.get('descr')
        pic_data['id'] = i.get('pic_id')
        pic_data['url'] = i.get('purl')

        data_list.append(pic_data)
    return data_list


def write_to_csv(data,header):
    '''将获取的图片信息写入csv文件中'''
    with open(r'test_project\res\csv\tieba.csv','a',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writerows(data)

def download_to_file(id,url):
    '''根据获取的链接下载图片'''
    file_name = r"test_project\res\img\{}.jpg".format(id)

    res = get_one_page_data(url)
    
    with open(file_name,'wb') as f:
        f.write(res.content)


def main():

    for i in range(1,81,40):
        # 网址的规律可以从Ajax数据接口中的负载中查看
        url = f'https://tieba.baidu.com/photo/g/bw/picture/list?kw=%E5%9B%BE%E7%89%87&alt=jview&rn=200&tid=1433290932&pn=1&ps={i}&pe={i+39}&info=1&_=1696311856699'
        time.sleep(2)
        json_text = get_one_page_data(url).json()
        data = parse_page(json_text)
        header = ('date','id','url')

            
        write_to_csv(data,header)
        
            # time.sleep(2)
            # download_to_file(one_url_data['id'],one_url_data['url'])
        print(f'正在写入第{(i//40)+1}个链接中的数据')

    print(data)
    print('done')

if __name__ == "__main__":
    main()