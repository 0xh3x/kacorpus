import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

class MySpider(CrawlSpider):
    name = 'nplg.gov.ge'
    allowed_domains = ['www.nplg.gov.ge']
    start_urls = [
        'http://www.nplg.gov.ge/dlibrary/coll/0001/',
        'http://www.nplg.gov.ge/dlibrary/coll/0002/'
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('dlibrary/coll/\d+/page-\d+/', ))),
        Rule(SgmlLinkExtractor(allow=('dlibrary/coll/\d+/\d+/', ))),
        Rule(SgmlLinkExtractor(allow=(re.compile(r'dlibrary/collect/\d+/\d+/.+\.pdf', re.IGNORECASE), )), callback='save_file'),
    )

    def save_file(self, response):
        filename = '-'.join(response.url.split("/")[-3:])
        self.log('Saving %s' % filename)
        open(filename, 'wb').write(response.body)
