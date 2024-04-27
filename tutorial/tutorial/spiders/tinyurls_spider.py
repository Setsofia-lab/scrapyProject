import scrapy
 
 
class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
 
    start_urls = [
        'https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html'
    ]
 
    def parse(self, response):
        for product in response.xpath('//ul[@class="productlisting-ul"]/div/li'):
            yield {
                'Title' : product.xpath('.//a[@class="p_box_title"]/text()').get(),
                'Product Url' : product.xpath('.//a[@class="p_box_title"]/@href').get(),
                'Discounted price' : product.xpath('.//div[@class="p_box_price"]/span[@class="productSpecialPrice fl"]/text()').get(),
                'Original price' : product.xpath('.//div[@class="p_box_price"]/span[@class="normalprice fl"]/text()').get(),
            }

        next_page = response.xpath('//a[@class="nextPage"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)