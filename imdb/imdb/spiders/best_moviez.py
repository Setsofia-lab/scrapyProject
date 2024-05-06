import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviezSpider(CrawlSpider):
    name = "best_moviez"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title"]/a[@class="ipc-title-link-wrapper"]'), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths='//button[@class="ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-base ipc-btn--theme-base ipc-btn--on-accent2 ipc-text-button ipc-see-more__button"]')),
    )

    def parse_item(self, response):
        # yield(response)
        yield{
            'title': response.xpath('div[@class="sc-b7c53eda-0 dUpRPQ"]/h1/span/text()').get(),
            'year': response.xpath('//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt"]/li[1]/a/text()').get(),
            'duration': response.xpath('//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt"]/li/text()').get(),
            'genre': response.xpath('//a[@class="ipc-chip ipc-chip--on-baseAlt"]/span/text()').get(),
            'rating': response.xpath('//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt"]/li[2]/a/text()').get(),
            'movie_url': response.url,
            # 'user-agent': response.request.headers['User-Agent']
        }
        
