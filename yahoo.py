#coding:utf-8
import	urllib2
import	urllib
import re

# gjc = urllib.quote("科技")
# print gjc
#swift utf-8 

resultNum = "&nresults="
keyword = "hello"
url = "https://ca.search.yahoo.com/sugg/gossip/gossip-ca-sayt?output=yjsonp&l=1&command="+ keyword #+ resultNum + "15"

#header of the yahoo 
headers = {
			"GET"  : url,
			"HOST" : "ca.search.yahoo.com",
			"Referer" : "https://ca.yahoo.com",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
		
		   }



req = urllib2.Request(url)
for i in headers:
	req.add_header(i,headers[i])


html = urllib2.urlopen(req).read()


# print html
# print html[69]

# print html.find("\"r\":")

ss = re.findall("\"(.*?)\"",html)
# print ss
# print ss.index("r")

if ss.index("r") != -1:
	FinResult = ss[ss.index("r")+1:]

print FinResult
for i in FinResult:
	print i
