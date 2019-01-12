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
            
            content = earch.xpath("./div[@class='views-field-phpcode-1']/a/text()").extract()
            content = len(content)>0?contents[0]:''
            sources = earch.xpath("./div[@class='xqjulistwafo']/a/text()").extract()
            source = len(content)>0?sources[0]:''
            likes = earch.xpath("./div[@class='views-field-ops']/a/text()").extract()
            like = len(content)>0?likes[0]:''
            jujis = earch.xpath("./div[@class='views-field-field-addtoalbum-value']/div/a/text()").extract()
            juji = len(content)>0?jujis[0]:''
            comments = earch.xpath("./div[@class='views-field-comment-count']/a/text()").extract()
            comment = len(content)>0?comments[0]:''
            authors = earch.xpath("./div[@class='views-field-name']/div/a/text()").extract()
            author = len(content)>0?authors[0]:''
            print ('......................%s, %s, %s, %s, %s'%(content, like, juji, comment, author))
            


