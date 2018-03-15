#iterates through a list of items|urls and returns a list of dead links or links that should be checked manually.

import StringIO
import time
import urllib2

import urllib
import urllib2
from socket import error as SocketError
import errno

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Joel Franke',
          'location': 'London',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.urlencode(values)

## inFile is expected to be a double single column list of item name|URL to lookup
inFile=open('linksToCheck.txt')

## outFile writes url and the reason the url failed to open
outFile = open('DeadLinks.txt', 'w')
n = 1

for line in inFile:
	print n
	sLine = line.split('|')
	label = sLine[0]
	url = sLine[1]
	if url[0] != 'h':
		url = 'http://' + url	
	try:
		req = urllib2.Request(url, None, headers)
		res = urllib2.urlopen(req)
		n = n + 1
	except (urllib2.URLError, urllib2.URLError,SocketError) as e:
		if e.errno != errno.ECONNRESET:
			try:
				print url.strip(), e.code
				if e.code > 307:
					outFile.write(label+"|"+url.strip() + "|" +str(e.code)+"|"+ str(e.reason).replace('\n', '')+'\n')
					n = n + 1
					continue
			except:
				print url.strip(), e.reason
				outFile.write(label+"|"+url.strip() + "||" + str(e.reason).replace('\n', '')+'\n')
				n = n + 1
				continue
		outFile.write(label+"|"+url.strip() + "||" + str(e.errno).replace('\n', '')+'\n')
		n = n + 1
		continue
	
inFile.close()
outFile.close()
