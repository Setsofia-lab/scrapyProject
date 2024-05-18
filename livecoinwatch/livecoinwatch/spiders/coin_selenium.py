from typing import Any
import scrapy
from scrapy.selector import Selector
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = "coin_selenium"
    allowed_domains = ["web.archive.org"]
    start_urls = [
        "https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/"
    ]

    def __init__(self):
        option = Options()
        option.add_argument("--headless")

        chrome_path = which("chromedriver")

        service = Service(executable_path=chrome_path)
        driver = webdriver.Chrome(service=service, options=option)
        driver.set_window_size(1920, 1080)
        driver.get("https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/")

        coin_tab = driver.find_element(By.CLASS_NAME, "filterPanelItem___2z5Gb")
        coin_tab.click()

        self.html = driver.page_source
        driver.close()
        
    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath('//div[contains(@class, "ReactVirtualized__Table__row tableRow___3EtiS ")]'):
            yield {
                'currency_pair' : currency.xpath(".//div[1]/div/text()").get(),
                'volume(24)' : currency.xpath(".//div[2]/span/text()").get(),
                'last_price' : currency.xpath(".//div[3]/span/text()").get()
            }
