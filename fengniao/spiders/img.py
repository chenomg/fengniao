# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FengniaoItem
import re


class ImgSpider(CrawlSpider):
    name = 'img'
    allowed_domains = ['bbs.fengniao.com']
    start_urls = ['http://bbs.fengniao.com/forum/10438463.html',
                  'http://bbs.fengniao.com/forum/10435123.html',
                  'http://bbs.fengniao.com/forum/10434464.html']
    download_delay = 1
    rules = [
        Rule(LinkExtractor(allow=("^http\:\/\/bbs\.fengniao\.com\/forum\/.*\.html$"), restrict_xpaths=("//div[@class='cont']/div[@class='pageSmall']")), callback='parse_item', follow=True),
    ]


    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = FengniaoItem()
        sels = response.xpath("//div[@class='cont']/div[@class='img']")
        for sel in sels:
            image_url_ = sel.xpath("a/img/@src").extract_first()
            image_url = re.findall(r"(.+?)\?", image_url_)
            item['image_urls'] = image_url
            yield item
