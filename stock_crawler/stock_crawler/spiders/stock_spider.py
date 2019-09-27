# -*- coding: utf-8 -*-
import scrapy
from ..items import StockCrawlerItem

class StockSpiderSpider(scrapy.Spider):
    name = 'stock_spider'
    api='http://api.scraperapi.com/?api_key=822da7f5e247570657b28227f6d782f1&url='
    link = 'https://www.moneycontrol.com/stocks/marketstats/bse-mostactive-stocks/all-companies-97/'
    start_urls=[api+link+'&render=true'] #&render=true renders the Javascipt

    def parse(self, response):
        items = StockCrawlerItem()
        holders = response.xpath('//*[@id="mc_content"]/section/section/div[1]/div[2]/div/div[2]/table/tbody').css('tr')

        for holder in holders:
                name=holder.css('td.PR > span.gld13.disin > a::text').extract()

                group=holder.xpath('td[2]/text()').extract()

                high=holder.xpath('td[3]/text()').extract()

                low=holder.xpath('td[4]/text()').extract()

                last_price=holder.xpath('td[5]/text()').extract()

                value=holder.xpath('td[7]/text()').extract()

                items['name']=name
                items['group']=group
                items['high']=high
                items['low']=high
                items['last_price']=last_price
                items['value']=value

                yield items
