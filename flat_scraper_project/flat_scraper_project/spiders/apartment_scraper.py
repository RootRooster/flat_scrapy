import scrapy
from pathlib import Path
from selenium import webdriver


class ApartmentScraper(scrapy.Spider):
    name = 'apartments'

    def __init__(self):
            self.driver = webdriver.Firefox()

    def start_requests(self):
        urls = [
            'https://www.sreality.cz/en/search/for-sale/apartments'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"flats-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")