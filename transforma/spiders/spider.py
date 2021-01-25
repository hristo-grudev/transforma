import re

import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import TransformaItem


class TransformaSpider(scrapy.Spider):
	name = 'transforma'
	start_urls = ['https://transforma.bg/novini/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="fusion-post-content post-content"]/h2/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		pagination_links = response.xpath('//div[@class="pagination clearfix"]/a[@class="pagination-next"]/@href')
		yield from response.follow_all(pagination_links, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="post-content"]').getall()
		description = [remove_tags(re.sub('<style[\S\s]*?</style>', '', p)).strip() for p in description]
		date = response.xpath('(//div[@class="fusion-meta-info-wrapper"]/span)[3]/text()').get()

		item = ItemLoader(item=TransformaItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)
		print(title)
		return item.load_item()
