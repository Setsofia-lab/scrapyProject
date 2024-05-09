# from typing import Iterable
import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = "coin"
    allowed_domains = ["web.archive.org"]


    script = '''
        function main(splash, args)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(5))
            rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb "))
            rur_tab[5]:mouse_click()
            assert(splash:wait(5))
            splash:set_viewport_full()
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url="https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })


    def parse(self, response):
        # print(response.body)
        currencies  = response.xpath('//div[contains(@class, "ReactVirtualized__Table__row tableRow___3EtiS ")]')
        for currency in currencies:
            yield {
                'currency_pair' : currency.xpath(".//div[1]/div/text()").get(),
                'volume(24)' : currency.xpath(".//div[2]/span/text()").get(),
                'last_price' : currency.xpath(".//div[3]/span/text()").get()
            }

# import scrapy
# from scrapy_splash import SplashRequest
 
 
# class CoinSpider(scrapy.Spider):
 
#     name = 'coin'
 
#     allowed_domains = ['web.archive.org']
#     script = '''
 
#         function main(splash, args)
#             splash.private_mode_enabled = false
#             url = args.url
#             assert(splash:go(url))
#             assert(splash:wait(3))
#             splash:set_viewport_full()
 
#             return splash:html()
#         end
#     '''
 
#     def start_requests(self):
#         yield SplashRequest(url="https://web.archive.org/web/20191115082436/https://www.livecoin.net/en", callback=self.parse, endpoint="execute", args={
#             'lua_source': self.script
#         })
 
#     def parse(self, response):
#        currencies = response.xpath("//div[contains(@class, 'tableRow___3EtiS ')]")
#        for currency in currencies:
#            yield {
#                'name': currency.xpath(".//div[contains(@class, 'tableRowColumn___rDsl0')]/div[1]/text()").get(),
#                'v 24h': currency.xpath(".//div[contains(@class, 'tableRowColumn___rDsl0')][5]//text()").get()
        #    }