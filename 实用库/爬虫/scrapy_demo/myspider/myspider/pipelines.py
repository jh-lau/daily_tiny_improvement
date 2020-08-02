# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

logger = logging.getLogger(__name__)


class MyspiderPipeline:
    def process_item(self, item, spider):
        # print(item)
        item['hello'] = 'world'
        logger.warning('==' * 10)
        return item


class MyspiderPipeline1:
    def process_item(self, item, spider):
        print(item)
        return item
