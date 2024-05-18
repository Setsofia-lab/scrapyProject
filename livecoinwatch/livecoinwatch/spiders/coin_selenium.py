from typing import Any
import scrapy
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = "coin_selenium"
    allowed_domains = ["livecoinwatch.com"]
    start_urls = ["https://livecoinwatch.com"]

    def __init__(self):
        option = Options()
        option.add_argument("--headless")

        chrome_path = which("chromedriver")

        service = Service(executable_path=chrome_path)
        driver = webdriver.Chrome(service=service, options=option)
        driver.get("https://livecoinwatch.com")

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
