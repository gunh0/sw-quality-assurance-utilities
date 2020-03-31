import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy


class RedCrawlerSpider(CrawlSpider):
    name = 'RedCrawler'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.allowed_domains = [self.domain]
        self.category_dict = {
            'Defects' : 1,
            'TestSupport' : 2,
            'QualityInspection' : 3
        }