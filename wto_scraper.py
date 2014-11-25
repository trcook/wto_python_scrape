from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
import os

# IN the special case of the wto disputes, we need to get the list of all disputes, so we run this script preliminarily:
execfile("./fetchjson.py")


# Now we build the scraper:



# First we define a box to put information into (an object to recieve scrapted info)
class WTO_Dispute(scrapy.Item):
    url = scrapy.Field()
    # name = scrapy.Field()
    # description = scrapy.Field()


# Then we define a class which will be used to direct scrapy as to what to gather from the web.
class WTO_Dispute_Link_Spider(CrawlSpider):
	name = 'wtodisputes'
	# allowed_domains=['wto.org']
	start_urls = ['http://wto.org/english/tratop_e/dispu_e/dispu_status_e.htm']
	def parse(self,response):
		dispute=WTO_Dispute()
		dispute['url']= response.xpath("//a/text()").extract()
		# dispute['name']= # fill in here
		# dispute['description']= # fill in here
		return dispute
# based on http://doc.scrapy.org/en/0.24/intro/overview.html

# to run: run $ scrapy runspider wtoscraper.py -o wto_disputes.json

