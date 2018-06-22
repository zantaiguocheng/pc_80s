# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from s80.items import S80Item
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.pipelines.files import FilesPipeline
class DianyingSpider(RedisCrawlSpider):
    name = 'dianying'
    allowed_domains = ['www.80s.tw']
    # start_urls = ['https://www.80s.tw/movie/list']
    redis_key = 'dianyingspider:strat_urls'
    rules = (
        Rule(LinkExtractor(allow=r'-----p\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/movie/\d+'),
             callback='parse_item', follow=False),
    )

    def __init__(self, *args, **kwargs):
        self.allowed_domains = ['www.80s.tw']
        super(DianyingSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        response = Selector(response)
        itme = S80Item()
        itme['电影'] = response.xpath('//h1/text()').extract()
        itme['类型'] = response.xpath(
            '//span[@class="span_block"][1]/a/text()').extract()
        itme['演员'] = response.re('a href="/actor/.*?>([\u4e00-\u9fa5·]+)<')
        itme['地区'] = response.xpath(
            '//div[@class="clearfix"]/span[2]/a/text()')[0].extract()
        itme['语言'] = response.xpath(
            '//div[@class="clearfix"]/span[3]/a/text()').extract()
        itme['导演'] = response.xpath(
            '//div[@class="clearfix"]/span[4]/a/text()').extract()
        itme['片长'] = response.xpath(
            '//div[@class="clearfix"]/span[6]/text()').extract()
        itme['上映时间'] = response.xpath(
            '//div[@class="clearfix"]/span[5]/text()').extract()
        itme['下载链接'] = list(set(response.re('"(thunder://.*?)"')))
        return itme
