import scrapy

class GlassesShopSpider(scrapy.Spider):
    name = 'glasses_shop'
    allowed_domains = ['www.glassesshop.com']

    start_urls = [
        'https://www.glassesshop.com/eyeglasses'
    ]

    def parse(self, response):
        for product in response.xpath('//div[@class="row pt-lg-5 product-list column-1"]'):
            yield {
                'product' : product
                # 'Product Name' : product.xpath('.//div[@class="p-title"]/a[1]/text()').get(),
                # 'Product URL' : product.xpath('.//div[@class="p-title"]/a[1]/@href').get(),
                # 'Product Price' : product.xpath('.//div[@class="p-price"][1]/div[1]/span/text()').get(),
                # 'Product Image' : product.xpath('.//div/a[1]/img[@class="lazy d-block w-100 product-img-default"]').get(),
            }