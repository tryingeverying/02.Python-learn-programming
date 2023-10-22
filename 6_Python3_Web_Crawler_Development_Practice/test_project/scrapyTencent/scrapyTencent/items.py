# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CategoryName = scrapy.Field()
    ComName = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    LocationName = scrapy.Field()
    RecruitPostName = scrapy.Field()
    RequireWorkYearsName = scrapy.Field()
    Responsibility = scrapy.Field()
    PostURL = scrapy.Field()

