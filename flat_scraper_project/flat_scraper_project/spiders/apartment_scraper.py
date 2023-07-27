import scrapy
from pathlib import Path
class ApartmentScraper(scrapy.Spider):
    name = 'apartments'

    def start_requests(self):
        urls = [
            'https://www.sreality.cz/en/search/for-sale/apartments',
            "https://www.sreality.cz/en/search/for-sale/apartments?page=2",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")