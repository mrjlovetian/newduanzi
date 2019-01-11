# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DuanziSpider(CrawlSpider):
    name = 'duanzi'
    allowed_domains = ['www.360wa.com']
    start_urls = ['http://www.360wa.com/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        for earch in response.xpath("//div[@class='p1']/div[@class='p_left']/a"):
            
            contents = earch.xpath('./p/text()').extract()
            content = contents[0]
            if contents.length > 1:
                content = contents[1]
            print ('......................%s'%(content))
            


