import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from doutu.items import DoutuItem



class Myspider(CrawlSpider):
    name = 'doutu'
    allowed_domanin = []
    start_urls = ['http://www.doutula.com/photo/list/']
    rules = (
        Rule(LinkExtractor(allow=(''),restrict_xpaths=('//*[@id="pic-detail"]/div/div[1]/div[3]/ul')),
            callback='parse_item',follow=True),
    )
    def parse_item(self,response):
        self.logger.info('hi,this is an item page! %s',response.url)
        item = DoutuItem()
     #   item['url'] = []
        item['file_urls'] = response.xpath('//*[@id="pic-detail"]/div/div/div//@data-original').extract()
        return item
