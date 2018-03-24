from bs4 import BeautifulSoup
import urllib2
import os
import socket
import socks
from urlparse import urlparse
import sqlite3
import sqlite3


def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050, True)
socket.socket = socks.socksocket
socket.create_connection = create_connection


resp = urllib2.urlopen("http://torwikignoueupfm.onion").read()

def next_url():
    conn = sqlite3.connect(r"database.db")
    c = conn.cursor()
    c.execute(
        "")
    conn.commit()
    conn.close()
#def work_on_url(url):
