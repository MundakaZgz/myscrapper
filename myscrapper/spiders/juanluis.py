import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JuanluisSpider(CrawlSpider):
    name = "juanluis"
    allowed_domains = ["juanlu.is"]
    start_urls = ["https://juanlu.is/"]

    rules = (Rule(LinkExtractor(), callback="parse_item", follow=True),)

    def parse_item(self, response):
        yield {
            "status": response.status,
            "url": response.url
        }
