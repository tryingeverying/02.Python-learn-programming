import scrapy
import sys
sys.path.append(r'F:\Programming\02.Python-learn-programming\6_Python3_Web_Crawler_Development_Practice\test_project\scrapyFamousSaying')
from scrapyFamousSaying.items import ScrapyfamoussayingItem

class FamoussayingspiderSpider(scrapy.Spider):
    name = 'famousSayingSpider'
    allowed_domains = ['so.gushiwen.cn']
    start_urls = ['https://so.gushiwen.cn/mingjus/']

    def parse(self, response):
        divs = response.xpath('//div[@class="left"]//div[@class="cont"]')
        items = ScrapyfamoussayingItem()
        for div in divs:
            text = div.xpath('./a/text()').getall()
            items['content'] = text[0]
            if len(text)>1:
                items['quote_from'] = text[1]
            else:
                items['quote_from'] = ' '
            yield items
        next_page_url =response.xpath('//a[@class="amore"]/@href').get()
        print(next_page_url)
        if next_page_url:
            yield scrapy.Request(
                'https://so.gushiwen.cn'+next_page_url
            )