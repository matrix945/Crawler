#coding:utf-8
import	urllib2
import	urllib


# gjc = urllib.quote("科技")
# print gjc
#swift utf-8 

url = "https://ca.search.yahoo.com/sugg/gossip/gossip-ca-sayt?output=yjsonp&l=1&command="
resultNum = "&nresults="

html = urllib2.Request('https://ca.search.yahoo.com/sugg/gossip/gossip-ca-sayt?output=yjsonp&l=1&command=/').read()
html.add_header('Referer' , '')

print html


