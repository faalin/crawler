# -*- coding: utf-8 -*-

# Define here the models for your scraped items
import json
from scrapy.item import Item,Field
from spiders.crawler_model import Modelzhua

data_from = Modelzhua.messagedata
data = json.loads(data_from)
demo = str(data['datas'])
datas = json.loads(demo)

class CrawlerHeadItem(Item):
	id = Field()
	names = locals()
	for data in datas:
		names[data['name']] = Field()