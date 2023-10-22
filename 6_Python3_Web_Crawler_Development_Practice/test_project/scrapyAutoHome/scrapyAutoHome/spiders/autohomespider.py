import scrapy
import sys
sys.path.append(r'F:\Programming\02.Python-learn-programming\6_Python3_Web_Crawler_Development_Practice\test_project\scrapyAutoHome')
from scrapyAutoHome.items import ScrapyautohomeItem

class AutohomespiderSpider(scrapy.Spider):
    name = 'autohomespider'
    allowed_domains = ['car.autohome.com.cn']
    url_format = 'https://car.autohome.com.cn/jingxuan/list-0-p{}.html'
    start_urls = [url_format.format(1)]

    def parse(self, response):
        li_list = response.xpath('//ul[@class="content"]/li')
        item = ScrapyautohomeItem()
        for li in li_list:
            item['describe'] = li.xpath('./a/p/text()').get()
            item['url'] = li.xpath('./a/@href').get()
            item['img_url'] = li.xpath('./a/img/@src').get()
            
            yield item
        for i in range(2,11):
            next_url = self.url_format.format(i)
            yield scrapy.Request(
                url=next_url
            )

        

