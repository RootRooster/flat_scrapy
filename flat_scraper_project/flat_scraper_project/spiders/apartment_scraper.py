import scrapy
from pathlib import Path
from time import sleep


class ApartmentScraper(scrapy.Spider):
    name = 'apartments'

    def start_requests(self):
        url = 'https://www.sreality.cz/en/search/for-sale/apartments'
        yield scrapy.Request(url=url, callback=self.parse, meta={"playwright": True})
        self.crawler.stats.set_value('apartments_scraped', 0)
    
    def parse(self, response):
        sleep(5)
        for apartment in response.css('.property.ng-scope'):
            title = apartment.css('.name.ng-binding::text').get()
            self.log(title)
            location = apartment.css('.locality.ng-binding::text').get()
            self.log(location)
            price = apartment.css('.norm-price.ng-binding::text').get()
            self.log(price)
            images = []
            for image in apartment.css('preact.ng-scope.ng-isolate-scope a > img::attr(src)'):
                image_src = image.get()
                images.append(image_src)
                self.log(image_src)
            self.crawler.stats.inc_value('apartments_scraped')
            self.log('total apartments scraped: ' + str(self.crawler.stats.get_value('apartments_scraped')))
            self.log('------------------')
        
        if self.crawler.stats.get_value('apartments_scraped') < 500:
            button_href = response.css('a.btn-paging-pn.paging-next::attr(href)').get()
            next_button_url = 'https://www.sreality.cz' + button_href
            yield scrapy.Request(url=next_button_url, callback=self.parse, meta={"playwright": True})

                
            