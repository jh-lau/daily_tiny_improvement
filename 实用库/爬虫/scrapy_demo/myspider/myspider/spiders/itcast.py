import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # result = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(result)

        li_list = response.xpath("//div[@class='tea_con']//li")
        for index, li in enumerate(li_list, start=1):
            item = {'name': li.xpath(".//h3/text()").extract_first().strip(),
                    'title': li.xpath(".//h4/text()").extract_first().strip(),
                    'index': index}
            yield item
