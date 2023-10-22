# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ScrapyfamoussayingPipeline:
    def open_spider(self,spider):
        '''创建文件并打开'''
        self.f = open(r'famousSaying.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        '''将数据写入文件'''
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.f.write(item_json + '\n')
        return item
    def close_spider(self,spider):
        '''关闭文件'''
        self.f.close()