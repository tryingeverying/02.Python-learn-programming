import scrapy
import sys 
sys.path.append(r'F:\Programming\02.Python-learn-programming\6_Python3_Web_Crawler_Development_Practice\test_project\scrapyPotery')
from scrapyPotery.items import ScrapypoteryItem

class PoteryspiderSpider(scrapy.Spider):
    name = 'poterySpider'
    allowed_domains = ['so.gushiwen.cn']
    start_urls = ['https://so.gushiwen.cn/shiwens/']

    def parse(self, response):
        divConts = response.xpath('//div[@id="leftZhankai"]/div[@class="sons"]/div[@class="cont"]')
        item = ScrapypoteryItem()

        for div in divConts:
            item['title'] = div.xpath('./div/p/a/b/text()').get()
            text = div.xpath('./div/p[@class="source"]/a/text()').getall()
            item['author'] = text[1].strip('\n')
            item['dynasty'] = text[-1].strip('\n')
            item['content']  = div.xpath('./div/div[@class="contson"]//text()').getall()
            yield item
        next_page_url = 'https://so.gushiwen.cn' + response.xpath('//div[@class="pagesright"]/a/@href').get()
        yield scrapy.Request(
            next_page_url
        )

