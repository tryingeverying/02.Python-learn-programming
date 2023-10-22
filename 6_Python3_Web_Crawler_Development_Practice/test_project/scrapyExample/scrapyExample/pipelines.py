# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ScrapyexamplePipeline:
    def open_spider(self,spider):
        '''创建文件并打开'''
        self.f = open(r'quote.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        '''将数据写入文件'''
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.f.write(item_json + '\n')
        return item
    def close_spider(self,spider):
        '''关闭文件'''
        self.f.close()



# 这种写法的写入方法只能是'a',如果是'w'则前面的数据会被最后一个数据覆盖掉
    # def process_item(self, item, spider):
    #     '''将数据写入文件'''
    #     with open(r'quote.txt','a',encoding='utf-8') as f:
    #         item_json = json.dumps(dict(item),ensure_ascii=False)
    #         # item传过来是对象，要先强转为字典，
    #         # 再转为json格式的字符串，nsure_ascii=False处理中文的
    #         f.write(item_json + '\n')
    #         return item    
        
