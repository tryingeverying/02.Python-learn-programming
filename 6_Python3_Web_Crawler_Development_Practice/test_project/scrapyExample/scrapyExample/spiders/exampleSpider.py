import scrapy
import sys
sys.path.append('..')

from scrapyExample.items import ScrapyexampleItem
class ExamplespiderSpider(scrapy.Spider):
    name = 'exampleSpider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        '''解析获取的网页源码or数据包'''
        exampleitem = ScrapyexampleItem()
        for item in response.xpath('//div[@class="col-md-8"]/div[@class="quote"]'):
            # 从数据块中解析获取需要的文本，作者，标签
            exampleitem['text'] = item.xpath('./span[@class="text"]/text()').get()
            exampleitem['author'] = item.xpath('./span/small[@class="author"]/text()').get()
            exampleitem['tags'] = item.xpath('./div[@class="tags"]/a/text()').extract()
            yield exampleitem
        # 获取下一页的url信息
        next_page_url = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_url:
            # 通过回调爬取下一页的数据，默认的callback为上面的parse函数，也可以自己写新的解析函数后传入
            yield scrapy.Request(
                'http://quotes.toscrape.com/' + next_page_url,
            )