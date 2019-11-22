# -*- coding: utf-8 -*-
import scrapy


class GushiwenSpider(scrapy.Spider):
    name = 'gushiwen'
    allowed_domains = ['www.gushiwen.org/']
    start_urls = ['https://www.gushiwen.org//']

    def parse(self, response):
        local = response.xpath('/html/body/div[2]/div[1]/div[2]/div[4]/a[3]')
        print("adasdaaaaaadsadadaaasdasdasas")
        for l in local:
            print(l.extract())
        pass
