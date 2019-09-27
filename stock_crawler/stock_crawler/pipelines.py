# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class StockCrawlerPipeline(object):
    def process_item(self, item, spider):
        item = dict((k,v) for k,v in item.iteritems() if v is not None)
        return item
