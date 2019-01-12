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
            
            contents = earch.xpath("./div[@class='views-field-phpcode-1']/a/text()").extract()
            content = ''; if len(contents)>0 content = contents[0]
            sources = earch.xpath("./div[@class='xqjulistwafo']/a/text()").extract()
            source = ''; if len(sources)>0 source = sources[0]
            likes = earch.xpath("./div[@class='views-field-ops']/a/text()").extract()
            like = ''; if len(likes)>0 like = likes[0]
            jujis = earch.xpath("./div[@class='views-field-field-addtoalbum-value']/div/a/text()").extract()
            juji = ''; if len(jujis)>0 juji = jujis[0]
            comments = earch.xpath("./div[@class='views-field-comment-count']/a/text()").extract()
            comment = ''; if len(comments)>0 comment = comments[0]
            authors = earch.xpath("./div[@class='views-field-name']/div/a/text()").extract()
            author = ''; if len(authors)>0 author authors[0]
            print ('......................%s, %s, %s, %s, %s'%(content, like, juji, comment, author))
            


