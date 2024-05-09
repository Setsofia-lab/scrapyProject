import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = "coin"
    allowed_domains = ["livecoinwatch.com"]
    start_urls = ["https://livecoinwatch.com"]

    script = '''
        function main(splash, args)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(5))
            coin_tab = assert(splash:select_all(".table-row filter-row"))
            assert(splash:wait(5))
            splash:set_viewport_full()
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest (url="https://livecoinwatch.com", callback=self.parse, endpoint="execute", args={
            'lua_source' : self.script
        })

    def parse(self, response):
        print(response.body)
