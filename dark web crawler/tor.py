import socket
import socks
import urllib2
import os
import time

import sys


def connectTor():
    os.system('open startTor.command')
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",9050,True)
    socket.socket = socks.socksocket
    time.sleep(3)

def newip():
    os.system('echo "125412541" | sudo -S killall tor')
    os.system("killall Terminal")
    os.system('open startTor.command')
    time.sleep(0.8)

def openurl(url):
    proxySupport = urllib2.ProxyHandler({"http":"127.0.0.1:8118"})
    opener = urllib2.build_opener(proxySupport)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    return opener.open(url).read()

def clearList():
    f = open('tor ip list.txt', 'w').close()
def updatelist(ip):
    f = open('tor ip list.txt', 'r')
    output = []
    num = 1
    for line in f:
        if ip in line:
            numezer = line.split(' ')
            num = 1 + int(numezer[0])
        else:
            output.append(line)
    f.close()
    f = open('tor ip list.txt', 'w')
    f.writelines(output)
    f.close()
    f = open('tor ip list.txt', 'a')
    f.write('\n' + str(num) + ' ' + ip)

def changeInFile(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return
    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

def ipToList():
    connectTor()
    while True:
        try:
            ip = openurl('https://enabledns.com/ip')
        except:
            ip = "error"
        print(ip)
        updatelist(ip)
        newip()

def onionTest():
    #connectTor()
    #newip()
    #t = urllib2.urlopen('http://zqktlwi4fecvo6ri.onion/wiki/index.php/').read()
    t = openurl('https://dirnxxdraygbifgc.onion.to')
    print(t)
    #except:
    #    print(sys.exc_info()[0])


onionTest()

