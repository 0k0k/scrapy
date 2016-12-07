# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	COMPANY_ABBR = scrapy.Field()
	COMPANY_CODE = scrapy.Field()
	STOCK_DATE=scrapy.Field()
	STOCK_TIME=scrapy.Field()
	STOCK_DAYSNAP=scrapy.Field()
	STOCK_DAYLINE=scrapy.Field()
