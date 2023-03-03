import scrapy
from scrapy.spiders import CrawlSpider, Rule


class AircraftSpider(CrawlSpider):
    name = "aircraft"
    allowed_domains = ["aerocorner.com"]
    start_urls = ["https://aerocorner.com/aircraft-categories/jumbo-passenger-jets/"]

    rules = (Rule(callback='parse_item', follow=True),)

    def parse_item(self, response):

        item = {}
        item["model"] = response.xpath("//h1/text()").get()

        performance = {}
        for i in range(1,12):
            key = response.xpath(f'//*[@id="performance"]/div/dl/dt[{i}]/text()').get()
            val = response.xpath(f'//*[@id="performance"]/div/dl/dd[{i}]/text()').get()
            performance[key] = val

        weights = {}
        for i in range(1,6):
            key = response.xpath(f'//*[@id="weights"]/div/dl/dt[{i}]/text()').get()
            val = response.xpath(f'//*[@id="weights"]/div/dl/dd[{i}]/text()').get()
            weights[key] = val

        dimensions = {}
        for i in range(1,12):
            key = response.xpath(f'//*[@id="dimensions"]/div/dl/dt[{i}]/text()').get()
            val = response.xpath(f'//*[@id="dimensions"]/div/dl/dd[{i}]/text()').get()
            dimensions[key] = val

        item.update(performance)
        item.update(weights)
        item.update(dimensions)
        
        return item