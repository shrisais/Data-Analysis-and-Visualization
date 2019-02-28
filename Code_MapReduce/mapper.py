#!/usr/bin/python
"""mapper.py"""
import sys
import nltk
import string

def clean(s):
    return ''.join(c for c in s if not c in string.punctuation)

STOPWORDS = nltk.corpus.stopwords.words('english')

for line in sys.stdin:
    line = unicode(clean(line.lower()), errors='ignore')
    line = line.strip()
    words = line.split()
    for word in words:
       if word in STOPWORDS:
                continue
       print '%s\t%s' % (word, 1)