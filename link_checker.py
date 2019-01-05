import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
class MyItem(Item):
    url= Field()
class MySpider(CrawlSpider):
    j= open("2urls.txt", "rt") 
    start_urls = [url.strip() for url in j.readlines()]
    name = 'link_checker'
    rules = (Rule(LinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self, response):
        f = open("2urls.txt",'a+')
        item = MyItem()
        item['url'] = response.url
        if "http" in item['url']:
            f.write(str(item['url'])+'\n')
        return item