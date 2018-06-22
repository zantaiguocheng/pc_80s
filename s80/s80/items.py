# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class S80Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    电影=scrapy.Field()
    类型=scrapy.Field()
    演员=scrapy.Field()
    地区=scrapy.Field()
    语言=scrapy.Field()
    导演=scrapy.Field()
    片长=scrapy.Field()
    上映时间=scrapy.Field()
    下载链接=scrapy.Field()