#!/usr/bin/env python
import sys
from xml.etree import cElementTree as ET

if len(sys.argv)<3:
    print "Usage: ./%s wikidumpfile.xml output.txt" % (sys.argv[0],)
    sys.exit(-1)

with open(sys.argv[2], 'a') as wikifile:
    for event, elem in ET.iterparse(sys.argv[1]):
        if elem.tag == '{http://www.mediawiki.org/xml/export-0.5/}text':
            if elem.text:
                wikifile.write(elem.text.encode('utf-8') + '\n')
        elem.clear()
