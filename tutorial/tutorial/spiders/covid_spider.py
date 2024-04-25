import scrapy

#This is a spider that crals a given website.
#It does this by crawilg the site and saving the detisls specified in the objects that have been created

#The defined class spcifies the name of the spider and the domains it will be crawling for data
class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains= ['www.worldometers.info']
    start_urls= ['https://www.worldometers.info/coronavirus/#countries']

    #The parse method specifies the path to access the doamins and also tha specific data to be collected when crawling.
    # In this case the countries data from the covid19 table
    def parse(self, response):
        countries = response.xpath("//td/a") # This countires variable specifies exactly the table that contains the details countries to be collected
        for country in countries:
            name = country.xpath(".//text()").get() # Using the defined for loop, collect the names of the countries and the link attached to the names. this links provides further data on the country, like those recovered etc  
            link = country.xpath(".//@href").get()


            # absolute_url = f"https://www.worldometers.info/{link}" This allows to follow the links attached the names of the country. I prefer to use response .follow
            # absolute_url = response.urljoin(link)

            yield response.follow(url=link, callback=self.parse_country, meta={'country':name}) # The callback allows scrapy to send response to the parse-contry method


    def parse_country(self, response):
        name = response.request.meta['country']
        covid_stats = response.xpath('.//div[@class="maincounter-number"]/span/text()').getall()
        cases = covid_stats[0]
        deaths = covid_stats[1]
        recovered  = covid_stats[-1]
        yield{
            'Country': name,
            'Cases' : cases,
            'Deaths' : deaths,
            'Recovered' : recovered,
        }


















    # def parse_country(self, response):
    #     cases = response.xpath('.//div[@class="maincounter-number"]/span/text()').get()
    #     deaths = response.xpath('.//div[@class="maincounter-number"]/span/text()')[1].getall()
    #     recovered  = response.xpath('.//div[@class="maincounter-number"]/span/text()')[-1].getall()
    #     yield{
    #         'Cases' : cases,
    #         'Deaths' : deaths,
    #         'Recovered' : recovered,
    #     }