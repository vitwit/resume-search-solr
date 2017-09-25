from __future__ import print_function
import urllib2
import simplejson

connection = urllib2.urlopen('http://localhost:8983/solr/temp/select?wt=json&q=*:*')
res = simplejson.load(connection)
print(res['response']['docs'])