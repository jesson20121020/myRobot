# #coding:utf-8
# class A(object):
# 	def __init__(self):
# 		pass

# 	def test(self):
# 		print 'this is test fun of class A'

# class B(object):
# 	def __init__(self):
# 		pass

# 	def test(self):
# 		pass

# 	def tst2(self):
# 		pass

# b = B()
# b.test()

# a = A()
# a.test()

# -*- coding: utf-8 -*-
import scrapy


class ShareditorSpider(scrapy.Spider):
    name = 'shareditor'
    start_urls = ['http://www.shareditor.com/']

    def parse(self, response):
        for href in response.css('a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'link': response.url,
        }