from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from forumge.items import ForumgeItem

class MySpider(CrawlSpider):
    name = 'forum.ge'
    allowed_domains = ['forum.ge']
    start_urls = ['http://forum.ge/?showforum=87']
    #start_urls = ['http://forum.ge/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('.+showforum=\d+.+', ))),
        Rule(SgmlLinkExtractor(allow=('.+showtopic=\d+.+', ), restrict_xpaths="//td[@class='row4' and not(@align)]"), callback='parse_topic'),
    )

    def parse_topic(self, response):
        hxs = HtmlXPathSelector(response)
        posts = hxs.select('//div[@class="postcolor"]/text()').extract()
        posts = [post.strip().replace("\r\n"," ").encode('utf-8') for post in posts if post not in ("", " ")]
        posts_text = '\n'.join(posts)
        open('forumgetext.txt', 'a').write(posts_text)
        #open('forumgeurls.txt','a').write(response.url+"\n")
