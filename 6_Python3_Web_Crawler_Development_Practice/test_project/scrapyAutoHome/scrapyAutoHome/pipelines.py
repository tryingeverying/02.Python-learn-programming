# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv,json
import os
import requests
from urllib import request

class ScrapyautohomePipeline:
    def process_item(self, item, spider):
        item_list = []
        item_list.append(dict(item))
        print(item_list)
        # item_json = json.dumps(dict(item), ensure_ascii=False)
        
        # 定义全局变量，使得表头只被写入一次
        # global i 
        i = True
        with open('autohome.csv','a',encoding='utf-8',newline='') as f:
            header = ['describe','url','img_url']
            write = csv.DictWriter(f,fieldnames=header)
            if i :
                write.writeheader()
                i = False
            # 写入内容
            write.writerows(item_list)
            
        
        # 下载图片
        src = item['img_url']
        image_name = src.split('__')[-1]
        # 打印当前运行的py文件的完整路径
        # print(__file__)   # D:/PycharmProjects/爬虫/day25/pic/demo.py
        # #os.path.dirname() 返回文件的路径，简单理解为往上退了以及目录
        # print(os.path.dirname(__file__))  # D:/PycharmProjects/爬虫/day25/pic
        # # 再往上退一级目录
        # print(os.path.dirname(os.path.dirname(__file__)))
        # 图片存储的文件夹路径
        # file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'res',image_name)
        # # # 图片的存储路径
        # # image_path = os.path.join(file_path,image_name)
        # print(f"正在下载{file_path}")
        # res = requests.get(src)
        # with open(file_path,'wb') as f:
        #     f.write(res.content)

        return item
