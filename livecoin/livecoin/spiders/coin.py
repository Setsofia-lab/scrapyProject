from typing import Iterable
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

    def reset_filter(self, spider):
        self.crawler.engine.slot.scheduler.df.fingerprints = set()

    #overriding the default from_crawler class method to access scrapy core components
    @classmethod    
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(CoinSpider, cls).from_crawler(crawler, *args, **kwargs)
        #initiate an event signal when spider is idle
        crawler.signals.connect(spider.reset_filter , signal=any)
        return spider

    def start_requests(self):
        yield SplashRequest(url="https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })


    def parse(self, response):
        for currency in response.xpath('//div[contains(@class, "ReactVirtualized__Table__row tableRow___3EtiS ")]'):
            yield {
                'currency_pair' : currency.xpath(".//div[1]/div/text()").get(),
                'volume(24)' : currency.xpath(".//div[2]/span/text()").get(),
                'last_price' : currency.xpath(".//div[3]/span/text()").get()
            }
