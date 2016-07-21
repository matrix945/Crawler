#coding:utf-8
import	urllib2
import	urllib

html = urllib2.urlopen('https://www.yahoo.com/').read()
#1)you have to put the http://
#2) you have to use google's api or Xgoogle
#3)https://ca.search.yahoo.com/sugg/gossip/gossip-ca-sayt?output=yjsonp&l=1&command=hello



print html


