#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
if len(sys.argv)<3:
    print "Usage: ./%s inputfile outputfile" % (sys.argv[0],)
geo = re.compile(ur"[\u10d0-\u10f0]+", re.UNICODE)
with open(sys.argv[2], "a") as wordlist:
    for line in open(sys.argv[1], "r"):
        for word in geo.findall(unicode(line, "utf-8")):
            #print type(word), word
            wordlist.write(word.encode('utf-8')+"\n")
