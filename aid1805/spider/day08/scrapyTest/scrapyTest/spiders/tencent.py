import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # 这里来确定哪些urls会被抓取
    start_urls = ['https://careers.tencent.com/search.html?keyword=python']

    def parse(self, response):
        '''
        接收到框架返回的抓取结果；
        提取真正要抓取的信息。
        '''

