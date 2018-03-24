import socks
import socket
import urllib2

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

# Gotta' Monkey Patch 'Em Al
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050, True)
socket.socket = socks.socksocket
socket.create_connection = create_connection

req = urllib2.Request("http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page", headers={'User-Agent' : "Magic Browser"})
con = urllib2.urlopen( req )
print con.read()

resp = urllib2.urlopen("http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page").read()

print resp