# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, csv

class ScrapytencentPipeline:
    def process_item(self, item, spider):
        item_list = []
        item_list.append(dict(item))
        print(item_list)
        # item_json = json.dumps(dict(item), ensure_ascii=False)
        header = ['CategoryName',
                  'ComName ',
                  'LastUpdateTime',
                  'LocationName',
                  'RecruitPostName',
                  'RequireWorkYearsName',
                  'Responsibility',
                  'PostURL']
        # with open('tencent.csv','a',encoding='utf-8',newline='') as f:
        #     write = csv.DictWriter(f,fieldnames=header)
        #     write.writeheader()
        #     write.writerows(item_list)
        return item
