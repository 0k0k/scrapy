# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    description=scrapy.Field()
    news_url=scrapy.Field()
    published_at=scrapy.Field()
    b_id=scrapy.Field()
    column_id=scrapy.Field()
