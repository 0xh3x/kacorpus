import cgi
from urlparse import urlparse
from scrapy.exceptions import IgnoreRequest

class Ignoreduplicates(object):
    """Parse URL before download and ignore if it's dublicate"""
    def __init__(self):
        self._count = 0
        self._count_uni = 0
        self._crawled = set()
        self._crawled_url = {}
        
    def process_request(self, request, spider):
        """Parse url, get forum.ge topic identification data """
        self._count += 1
        #print self._count
        url = urlparse(request.url)
        params = cgi.parse_qs(url[4])
        if not params.has_key('showtopic'):
            return
        showtopic = params['showtopic'][0]
        st = params['st'][0] if params.has_key('st') else '0'
        #id for each topic is topic id and page id pair
        topic_id = (showtopic, st)
        print topic_id
        if topic_id not in self._crawled:
            self._crawled.add(topic_id)
            self._crawled_url[topic_id] = request.url
            self._count_uni += 1
            print self._count_uni
        else:
            #open('duplicates.txt', 'a').write("%s => %s\n" % (request.url, self._crawled_url[topic_id]))
            raise IgnoreRequest('Found duplicate!!')

