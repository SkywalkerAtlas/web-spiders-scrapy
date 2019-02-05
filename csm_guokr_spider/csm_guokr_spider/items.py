# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CsmGuokrSpiderItem(Item):
    # define the fields for your item here like:
    title = Field()
    post_date = Field()
    content = Field()
    _id = Field()