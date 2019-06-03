# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstpjtItem(scrapy.Item):
    # define the fields for your item here like:
    fenlei_name = scrapy.Field()
    fenlei_url =  scrapy.Field()
    tupianwenjianjia_name = scrapy.Field()
    tupian_url = scrapy.Field()
    pass
