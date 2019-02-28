#!/usr/bin/python
"""mapper.py"""
import sys
import nltk
import string

def clean(s):
    return ''.join(c for c in s if not c in string.punctuation)

STOPWORDS = nltk.corpus.stopwords.words('english')
topten = ["site","health","food","awareness","artificial","search","opinion","dangerous","2018"]
todays
for line in sys.stdin:
    line = unicode(clean(line.lower()), errors='ignore')
    line = line.strip()
    words = line.split()
    for word in words:
       if word in STOPWORDS:
                continue
       else:
	    for occur in topten:
		if(word==occur)
                  term = "<"+word+","+occur+">"
       print '%s\t%s' % (term, 1)