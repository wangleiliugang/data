# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    positionName = scrapy.Field()
    # 职位详情链接
    positionLink = scrapy.Field()
    # 职位的类别
    positionType = scrapy.Field()
