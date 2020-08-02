import scrapy


class YangguangSpider(scrapy.Spider):
    name = 'yangguang'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://www.sun0769.com/']

    def parse(self, response):
        pass
