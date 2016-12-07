# -*- coding: utf-8 -*-
# http://query.sse.com.cn/security/stock/getStockListData2.do?
# &stockCode= 股票代码
# &csrcCode= 行业代码
# &areaName= 地区代码
# &stockType=1 A股B股
# &pageHelp.cacheSize=1
# &pageHelp.beginPage=1
# &pageHelp.pageSize=1500
# &pageHelp.pageNo=1
# &pageHelp.endPage=11

import scrapy
import json
from stock.items import StockItem

class SzasSpider(scrapy.Spider):
    name = "szas"
    allowed_domains = ["sse.com.cn"]
    start_urls = (
        'http://query.sse.com.cn/security/stock/getStockListData2.do?&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.beginPage=1&pageHelp.pageSize=1200',
    )
    custom_settings = {
    	'DEFAULT_REQUEST_HEADERS':{
			'Host': 'query.sse.com.cn',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0',
			'Accept': '*/*',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate',
			'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/',
			'Connection': 'keep-alive',
    	},
    }
    SNAP_URLAPI='http://yunhq.sse.com.cn:32041/v1/sh1/snap/{}?&select=name,last,chg_rate,change,amount,volume,open,prev_close,ask,bid%2Chigh,low,tradephase'
    LINE_URLAPI='http://yunhq.sse.com.cn:32041/v1/sh1/line/{}?&begin=0&end=-1&select=time,price,volume'


    def parse(self, response):
        for stock in json.loads(response.body)['result']:
        	item=StockItem()
        	item['COMPANY_ABBR']=stock['COMPANY_ABBR']
        	item['COMPANY_CODE']=stock['COMPANY_CODE']
        	SNAP_URL=self.SNAP_URLAPI.format(item['COMPANY_CODE'])    	
        	yield scrapy.Request(SNAP_URL,callback=self.parse_snap,meta={'item':item})


    def parse_snap(self, response):
    	item=response.meta['item']
    	item['STOCK_DAYSNAP']=json.loads(response.body.decode('gbk'))['snap']
    	LINE_URL=self.LINE_URLAPI.format(item['COMPANY_CODE'])   
        return scrapy.Request(LINE_URL,callback=self.parse_line,meta={'item':item})

    def parse_line(self, response):
    	item=response.meta['item']
    	item['STOCK_DAYLINE']=json.loads(response.body)['line']
    	item['STOCK_DATE']=json.loads(response.body)['date']
    	item['STOCK_TIME']=json.loads(response.body)['time']
    	return item