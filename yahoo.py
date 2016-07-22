#coding:utf-8
import	urllib2
import	urllib
import re
import time
from random import choice
iplist  = ['27.24.158.153:81','46.209.70.74:8080','60.29.255.88:8888']

ip= choice(iplist)
# gjc = urllib.quote("XXX")
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

proxy_support = urllib2.ProxyHandler({'http':'http://'+ip})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener( opener )

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
