from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

class MySpider(CrawlSpider):
    name = 'buki.ge'
    allowed_domains = ['buki.ge']
    start_urls = ['http://buki.ge/library-list.html']

    rules = (
        Rule(SgmlLinkExtractor(allow=('index\.php\?.+p=library-list.+page=\d+', ))),
        Rule(SgmlLinkExtractor(allow=('uploads/library/.+\.doc[x]?', )), callback='save_file'),
    )

    def save_file(self, response):
        filename = response.url.split("/")[-1]
        self.log('Saving %s' % filename)
        open(filename, 'wb').write(response.body)
