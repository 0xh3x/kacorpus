#monkey patching :)
import scrapy.utils.url
scrapy.utils.url._canonicalize_url = scrapy.utils.url.canonicalize_url
def canonicalize_url_patched(url, keep_blank_values=True, keep_fragments=False,\
        encoding=None):
        """removes last '=' char wich is appended by original
         function to urls like http://example.com/?234"""
        oldurl = scrapy.utils.url._canonicalize_url(url, keep_blank_values, keep_fragments, encoding)
        return oldurl[:-1] if oldurl.endswith("=") else oldurl
scrapy.utils.url.canonicalize_url = canonicalize_url_patched

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

class MySpider(CrawlSpider):
    name = 'lib.ge'
    allowed_domains = ['lib.ge']
    start_urls = ['http://lib.ge']

    rules = (
        Rule(SgmlLinkExtractor(allow=('body_text\.php\?\d+', )), callback='parse_topic'),
        Rule(SgmlLinkExtractor(allow=('authors\.php\?\d+', ))),
        Rule(SgmlLinkExtractor(allow=('cat_listing\.php\?\d+', ))),
    )

    def parse_topic(self, response):
        hxs = HtmlXPathSelector(response)
        texts = hxs.select('//div[@align="justify"]/p/text()').extract()
        open('libgetext.txt', 'a').write(' '.join([text.encode('utf-8') for text in texts]))
        #open('libgeurls.txt','a').write(response.url+"\n")

