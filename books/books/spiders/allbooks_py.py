import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllbooksPySpider(CrawlSpider):
    name = "allbooks"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a'), ),
    )

    def parse_item(self, response):
    #    yield(response.url)
       yield{
           'title' : response.xpath('//h3/a/text()').get(),
           'url': response.xpath('//h3/a/@href').get(),
           'product_price': response.xpath('//div[@class="product_price"]/p[1]/text()').get(),
        #    'availability' : response.xpath('//div[@class="product_price"]/p/i').get()
       }
