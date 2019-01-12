# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DuanziSpider(CrawlSpider):
    name = 'duanzi'
    allowed_domains = ['www.juzimi.com']
    start_urls = ['https://www.juzimi.com/tags/400766']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        for earch in response.xpath("//div[@class='view-content']/div/div"):
            
            content = earch.xpath("./div[@class='views-field-phpcode-1']/a/text()").extract()[0]
            source = earch.xpath("./div[@class='xqjulistwafo']/a/text()").extract()[0]
            like = earch.xpath("./div[@class='views-field-ops']/a/text()").extract()[0]
            juji = earch.xpath("./div[@class='views-field-field-addtoalbum-value']/a/text()").extract()[0]
            comment = earch.xpath("./div[@class='views-field-comment-count']/a/text()").extract()[0]
            author = earch.xpath("./div[@class='views-field-name']/a/text()").extract()[0]
            print ('......................%s, %s, %s, %s, %s, %s'%(content, source, like, juji, comment, author))
            


