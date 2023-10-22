# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyautohomeItem(scrapy.Item):
    '''定义数据结构'''
    # define the fields for your item here like:
    # name = scrapy.Field()
    describe = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
