import scrapy
import sys
sys.path.append(r'F:\Programming\02.Python-learn-programming\6_Python3_Web_Crawler_Development_Practice\test_project\scrapyTencent')
from scrapyTencent.items import ScrapytencentItem
import json

class TencentspiderSpider(scrapy.Spider):
    name = 'tencentSpider'
    allowed_domains = ['careers.tencent.com']

    start_url_format = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1697899799040&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=1&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    start_urls = [start_url_format.format(1)]
    detail_url_format = 'https://careers.tencent.com/tencentcareer/api/post/ByRelated?timestamp=1697942417299&postId={}&num=7&language=zh-cn'

    def parse(self, response):
        '''解析初始页的数据'''
        posts= response.json()['Data']['Posts']
        for post in posts:
            item = ScrapytencentItem(
                CategoryName=post['CategoryName'],
                ComName=post['ComName'],
                LastUpdateTime=post['LastUpdateTime'],
                LocationName=post['LocationName'],
                RecruitPostName=post['RecruitPostName'],
                RequireWorkYearsName=post['RequireWorkYearsName'],
                PostURL=post['PostURL'],
                Responsibility=post['Responsibility']
                )
            yield item
            # 获取详情页的工作职责
            postId = post['PostId']
            new_detail_url = self.detail_url_format.format(postId)
            yield scrapy.Request(
                url=new_detail_url,
                # callback=self.parse_detail,
                # meta={'items':item}
                # 用字典的格式进行数据传输，字典的value就是要传输的数据
                # key值是自己定义的变量，在函数中接收的时候就用key值接收
            )
        # 自动爬取下一页
        for i in range(2,5):
            next_url = self.start_url_format.format(i)
            yield scrapy.Request(
                url=next_url,
                # callback=self.parse
                # 默认调用上面的parse解析，如果使用其他解析方法自己改                
            )

    # def parse_detail(self, response):
    #     '''解析详情页的数据'''
    #     item = response.meta.get('items')
    #     data=json.loads(response.text)
    #     item['Responsibility'] = data['Data']['Responsibility']
    #     # print(item)
    #     yield item
        
    