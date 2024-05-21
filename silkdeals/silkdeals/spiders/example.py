import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class ExampleSpider(scrapy.Spider):
    name = "example"

    def start_requests(self):
        yield SeleniumRequest(
            url = 'https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search_input = driver.find_element(By.ID, "searchbox_input")
        search_input.send_keys("Hello World")

        search_input.send_keys(Keys.ENTER)

        html = driver.page_source
        response_obj = Selector(text=html)

        links = response_obj.xpath("//ol/li[@class='wLL07_0Xnd1QZpzpfR4W']")
        for link in links:
            yield{
                'URL': link.xpath(".//a[@class='Rn_JXVtoPVAFyGkcaXyK']").get()
            }


