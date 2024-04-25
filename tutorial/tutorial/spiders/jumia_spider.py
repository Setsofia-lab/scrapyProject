from pathlib import Path
import scrapy

class JumiaPhonesSpider(scrapy.Spider):
    name = "jumiaphones"

    def start_requests(self):
        urls = [
            "https://www.jumia.com.gh/android-phones/#catalog-listing"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"jumiaphones-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")