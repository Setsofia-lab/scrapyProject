import scrapy

class GlassesShopSpider (scrapy.Spider):
    name = 'glasses_shop'
    allowed_domains = ['www.glassesshop.com']

    start_urls = [
        'https://www.glassesshop.com/eyeglasses'
    ]

    def parse(self, response):
        for product in response.xpath('//div[@class="row pt-lg-5 product-list column-1"]'):
            yield {
                'Product Name' : product.xpath('.//div/div/div/div/div/div[@class="p-title"]/a/text()').get(),
                'Product URL' : product.xpath('.//div/div/div/div/div/div[@class="p-title"]/a[1]/@href').get(),
                'Product Price' : product.xpath('.//div/div/div/div/div/div[@class="p-price"][1]/text()[1]').get(),
            }