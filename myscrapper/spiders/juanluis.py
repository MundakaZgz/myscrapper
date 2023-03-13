import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JuanluisSpider(CrawlSpider):
    name = "juanluis"
    allowed_domains = ["juanlu.is"]
    start_urls = ["https://juanlu.is/"]

    rules = (Rule(LinkExtractor(allow=r"/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["page"] = response.xpath('//h1[@id="page-title"]/a').get()
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//h1[@id="page-title"]/a').get(),
        #item["url"] = response.xpath('//h1[@id="page-title]/a::attr(href)').get()
        #item["description"] = response.xpath('').get()
        return item
