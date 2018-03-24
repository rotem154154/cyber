from bs4 import BeautifulSoup
import urllib2
import os
import socket
import socks
from urlparse import urlparse
import sqlite3

queue = []
crawledarr = []

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

def open_url2(url):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection

    return urllib2.urlopen(url).read()

def open_url(url):
    return urllib2.urlopen(url).read()
def Test_page(url):
    print "@@@@@" + str(len(queue))
    print url
    try:
        site = open_url2(url)
        soup = BeautifulSoup(site, "html.parser")
        for link in soup.findAll('a'):
            href = fix_link(str(link.get('href')))
            #print href
            if href != "" and ".onion" in href:
                # print 1
                if not link_in_queue(href) and not link_in_crawled(link_to_domain(href)):
                    queue.append(href)

        crawledarr.append(url)
        if not page_info(url):
            print "error"
        new_link = link_from_queue()
        #print new_link
        if new_link != "":
            Test_page(new_link)
        else:
            print "DONE!"
    except:
        #print "error"
        new_link = link_from_queue()
        if new_link != "":
            Test_page(new_link)
        else:
            print "DONE!"

def fix_link(href):
     if len(href) > 2:
         while href[0] == "/":
             href = href[1:]
         return href
     return ""
def link_to_domain(href):
    parsed_uri = urlparse(href)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

def link_in_domain(href):
    if href.startswith("http://"):
        href[8:]
    if href.startswith("www."):
        href[4:]
    if href.startswith(href):
        return True
    return False

def link_in_queue(href):
    for line in crawledarr:
        if line == href:
            return True
    for line in queue:
        if line in href:
            return True
    return False

def link_in_crawled(href):
    for c in crawledarr:
        if href in c:
            return True
    return False
def page_info(url):
    site = open_url2(url)
    soup = BeautifulSoup(site, "html.parser")
    title = soup.title.string.encode('UTF-8')
    descriptiontest = soup.find('meta', attrs={'name': 'og:description'}) or soup.find('meta', attrs={
        'property': 'description'}) or soup.find('meta', attrs={'name': 'description'})
    if descriptiontest:
        description = descriptiontest.get('content')
    keywordstest = soup.find('meta', attrs={'name': 'og:keywords'}) or soup.find('meta', attrs={
        'property': 'Keywords'})
    '''if keywordstest:
        keywords = keywordstest.get('content')

    update_database(url, title, description, keywords)'''
    print title
    try:
        site = open_url2(url)
        soup = BeautifulSoup(site, "html.parser")
        title = soup.title.string.encode('UTF-8')
        descriptiontest = soup.find('meta', attrs={'name': 'og:description'}) or soup.find('meta', attrs={
            'property': 'description'}) or soup.find('meta', attrs={'name': 'description'})
        if descriptiontest:
            description = descriptiontest.get('content')
        keywordstest = soup.find('meta', attrs={'name': 'og:keywords'}) or soup.find('meta', attrs={
            'property': 'Keywords'})
        if keywordstest:
            keywords = keywordstest.get('content')

        update_database(url,title,description,keywords)

        return True
    except:
        return False

def update_database(url,title,description,keywords):
    conn = sqlite3.connect(r"database.db")
    c = conn.cursor()
    print  "INSERT INTO links VALUES ("+url+","+title+","+description+","+keywords+")"

    c.execute("INSERT INTO links VALUES ("+url+","+title+","+description+","+keywords+")")
    conn.commit()
    conn.close()
def link_from_queue():
    if len(queue) == 0:
        return ""
    line0 = queue[0]
    queue.remove(line0)
    return line0


#http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page
#domain = raw_input('domain to scan: ')

queue.append("https://onion.cab/list.php")
queue.append("https://www.reddit.com/r/onions/comments/2epckb/new_huge_onion_link_list/")
queue.append("http://torwikignoueupfm.onion")
queue.append("http://zqktlwi4fecvo6ri.onion")
queue.append("http://torlinkbgs6aabns.onion")


crawled = open("crawled.txt", "a")
crawled.close()

Test_page(link_from_queue())