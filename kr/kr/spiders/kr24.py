# -*- coding: utf-8 -*-
import scrapy
import json
from kr.items import KrItem
class Kr24Spider(scrapy.Spider):
    name = "kr24"
    allowed_domains = ["36kr.com"]
    # custom_settings = {
    # 	'DEFAULT_REQUEST_HEADERS':{
    # 		'Host':'36kr.com',
    # 		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0',
    # 		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    # 		'Accept-Encoding':'gzip, deflate',
    # 		'Referer':'http://36kr.com/',
    # 		'Cookie':'aliyungf_tc=AQAAAHobtTkDkwIAwtfz20HReDFTRk/G; ktm_ab_test=t.6_v.12; kr_stat_uuid=NfHpQ24661871; Hm_lvt_713123c60a0e86982326bae1a51083e1=1479712264; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1479715706; krnewsfrontss=36362e0f6d92fc4d7cb038da9be2652e; device-uid=c7aa34d0-afb9-11e6-b3fa-73855e8eb9dd',
    # 		'Connection':'keep-alive',
    # 		'Cache-Control':'max-age=0',
    # 	},
    # }
    start_urls = (
        'http://36kr.com/api/newsflash?per_page=1',
    )
    page=20

    def parse(self, response):
    	b_idlast=json.loads(response.body)['data']['items'][0]['id']
    	for b_id in xrange(b_idlast,b_idlast-1000,-self.page):
    		url='http://36kr.com/api/newsflash?b_id={}&per_page={}'.format(str(b_id),self.page)
    		yield scrapy.Request(url,callback=self.parse_page)


    def parse_page(self, response):
    	for news_item in json.loads(response.body)['data']['items']:
    		item=KrItem()
    		item['title']=news_item['title']
    		item['b_id']=news_item['id']
    		item['description']=news_item['description']
    		item['news_url']=news_item['news_url']
    		item['published_at']=news_item['published_at']
    		item['column_id']=news_item['column_id']
    		yield item



