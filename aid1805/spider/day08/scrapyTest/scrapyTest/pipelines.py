# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class ScrapytestPipeline:
    def process_item(self, item, spider):
        # 把爬虫抓取到的数据写入数据库或者本地的文件系统中
        with open("tencent.json", "ab") as f:
            text = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(text.encode('utf-8'))
        return item
