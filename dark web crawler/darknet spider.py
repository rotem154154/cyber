import urllib2
from BeautifulSoup import BeautifulSoup
import urlparse
import threading
import signal
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

lastLink = ''
q = ['https://zqktlwi4fecvo6ri.onion.to/wiki/index.php/Main_Page']


def openurl(url):
    #return urllib2.urlopen(url + ":80").read()

    proxySupport = urllib2.ProxyHandler({"http":"127.0.0.1:8118"})
    opener = urllib2.build_opener(proxySupport)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    return opener.open(url).read()
    #return urllib2.urlopen(url)


def domainIsNew(domain):
    f = open('darknet list.txt', 'r')
    for line in f:
        if str(domain) in str(line):
            f.close()
            return False
    f.close()
    return True
def updatelist(url , description):
    domain = getdomain(url)
    if domainIsNew(domain) and not 'Hidden Service' in str(description):
        f = open('darknet list.txt', 'a')
        try:
            f.write(description + '\r\n' + url + '\r\n\r\n')
        except:
            r = 5
            #print 'error'
        f.close()
        return True

def getdomain(url):
    base_url = urlparse.urljoin(url,'/')
    return base_url

def spider(url):
    print url
    val = URLValidator()
    val(url)
    global lastLink
    global q
    if lastLink != url:
        lastLink = url
        try:
            code = openurl(url)
            soup = BeautifulSoup(code)
            try:
                title = soup.title.string
            except:
                return 'error'
            updatelist(url, title)
            for a in soup.findAll('a', href=True):
                link = a['href']
                if 'onion.to' in link:
                    if link.startswith('https://'):
                        if link.startswith('https://www') == False:
                            if domainIsNew(getdomain(link)):
                                print str(len(q)) + ' testing url: ' + link
                                q.append(link)

        except Exception, e:
            print str(e)



def mainSpider():
    while True:
        spider(q.pop(0))


for _ in range(2):
    t = threading.Thread(target=mainSpider())
    t.daemon = True
    t.start()

