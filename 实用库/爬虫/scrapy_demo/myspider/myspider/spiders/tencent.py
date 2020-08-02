import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        recruit_list = response.xpath("//div[@class='recruit-list']").extract()
        print(recruit_list)
        for position in recruit_list:
            result = {'duty': position.xpath(".//p[@class='recruit-text']/text()").extract_first()}
            print(result)
