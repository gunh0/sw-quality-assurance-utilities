# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RedmineScraperItem(scrapy.Item):
    number = scrapy.Field()
    project = scrapy.Field()
    proj_type = scrapy.Field()
    proj_status = scrapy.Field()
    priority = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    master = scrapy.Field()
    category = scrapy.Field()
    target_version = scrapy.Field()
    change = scrapy.Field()
    start_time = scrapy.Field()
    deadline = scrapy.Field()
    pass
