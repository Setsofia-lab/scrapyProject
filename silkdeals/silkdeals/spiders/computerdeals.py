import scrapy
from scrapy_selenium import SeleniumRequest


class ComputerdealsSpider(scrapy.Spider):
    name = "computerdeals"

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals/',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//ul[@class='bp-p-filterGrid_items']/li")
        for product in products:
            yield {
                'name': product.xpath(".//a[@class='bp-c-card_title bp-c-link']/text()").get(),
                'link': product.xpath(".//a[@class='bp-c-card_title bp-c-link']/@href").get(),
                'store_name': product.xpath(".//span[@class='bp-c-card_subtitle']/text()").get(),
                'price': product.xpath(".//span[@class='bp-p-dealCard_price']/text()").get()
            }

        next_page = response.xpath("//span[@class='bp-c-icon bp-i-arrowRight']").get()
        if next_page:
            absolute_url = f"https://slickdeals.net{next_page}"
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )
