import cgi
import urllib
from urlparse import urlparse, urlunparse, ParseResult
from scrapy.exceptions import IgnoreRequest

class Ignoreduplicates(object):
    """Parse URL before download and ignore if it's dublicate.
       change query string for getting all topics"""
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
        if params.has_key('showtopic'):
            showtopic = params['showtopic'][0]
            st = params['st'][0] if params.has_key('st') else '0'
            #id for each topic is topic id and page id pair
            topic_id = (showtopic, st)
            #print topic_id
            if topic_id not in self._crawled:
                self._crawled.add(topic_id)
                self._crawled_url[topic_id] = request.url
                self._count_uni += 1
                print self._count_uni
            else:
                #open('duplicates.txt', 'a').write("%s => %s\n" % (request.url, self._crawled_url[topic_id]))
                raise IgnoreRequest('Found duplicate!!')
        elif params.has_key('showforum') and not request.meta.has_key('fixed'):
            #if it's showforum view set prune_day param to 100 and reschedule url (by returning modified request object)
            #for getting list of all topics in forum
            if params.has_key('prune_day') and params['prune_day'] == ['100']: return
            unparse_qs = lambda x: '&'.join([k+'='+urllib.quote(str(v[0])) for (k,v) in x.items()])
            params['prune_day'] = ['100']
            new_qs = unparse_qs(params)
            new_url = ParseResult(scheme=url.scheme, netloc=url.netloc, path=url.path, params=url.params, query=new_qs, fragment=url.fragment)
            new_url = urlunparse(new_url)

            request = request.replace(url=new_url, dont_filter=True)
            request.meta['fixed'] = 1
            print "changed to %s" % (str(new_url),)
            return request
