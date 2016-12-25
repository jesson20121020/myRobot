import scrapy

class ShareditorSpider(scrapy.Spider):
    name = "shareditor"
    allowed_domains = ["shareditor.com"]
    start_urls = [
        "http://www.shareditor.com/"
    ]
    
	def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
