# -*- coding: utf-8 -*-
import json
from crawler_head.items import CrawlerHeadItem
from scrapy.spiders import Spider
from scrapy.selector import Selector
from crawler_model import Modelzhua

data_from = Modelzhua.messagedata
data = json.loads(data_from)
demo = str(data['datas'])
datas = json.loads(demo)
start_url = str(data['url'])
data_xxpath = str(data['xxpath'])


class Okooo_jczqSpider(Spider):
	name = "spider"
	allowed_domain = ["okooo.com"]
	start_urls = [start_url]

 	def parse(self,response):
		sel = Selector(response)
		sites = sel.xpath(data_xxpath)
		for site in sites:
			item = CrawlerHeadItem()
			for data in datas:
				item[data['name']] = site.xpath(data['xpath']).extract()[0].strip()
			yield item
			

