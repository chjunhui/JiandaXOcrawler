# -*- coding: utf-8 -*-
'''
Have fun.

@author: B1u3Buf4
'''

import hashlib
import base64
import requests
import re
import sys
import os


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}  
key = ''
jsname = ''


def FirstReq():
    r = requests.get('http://jandan.net/ooxx/',headers=headers)
    tmps = re.findall('current-comment-page">\[.*?\]',r.text)[0]
    tmps = int(tmps[tmps.find('[') + 1:-1])
    global jsname
    jsname = "http://" + re.findall('cdn.jandan.net/static/min.*?\.js', r.text)[0]
    return tmps


def GetHash(start = 1, end = FirstReq()):
    r = requests.get(jsname,headers=headers)
    global key
    key = re.findall('"[0-9a-zA-Z]{32}"', r.text)[0][1:-1]
    for i in range(int(start), int(end) + 1):
        print(i)
        r = requests.get('http://jandan.net/ooxx/page-' + str(i), headers = headers)
        for j in re.findall('img-hash">.*?<',r.text):
            tmp = CryptoPwnd(j[10:-1],key)
	    tmp = re.sub('cn/.*?/','cn/large/',tmp)
	    print(tmp)
            rr = requests.get(tmp, headers = headers)
            with open('./pics/' + tmp[tmp.rfind('/') + 1:], 'wb') as f:
                f.write(rr.content)
    
    
def CryptoPwnd(pichash, key):
    r = hashlib.md5(key).hexdigest()
    o = hashlib.md5(r[:16]).hexdigest()
    n = hashlib.md5(r[16:]).hexdigest()
    l = pichash[:4]
    c = o + hashlib.md5(o + l).hexdigest()
    h = [i for i in range(256)]
    b = [ord(j) for j in c * 4]
    m = pichash[4:]
    if len(m) % 4 == 2:
        m += '=='
    elif len(m) % 4 == 3:
        m += '='
    else:
        pass
    k = [i for i in base64.b64decode(m)]
    f = 0
    for g in range(256):
        f = (f + h[g] + b[g]) % 256
        tmp = h[g]
        h[g] = h[f]
        h[f] = tmp
    t = ''
    p = 0
    f = 0
    for g in range(len(k)):
        p = (p + 1) % 256
        f = (f + h[p]) % 256
        tmp = h[p]
        h[p] = h[f]
        h[f] = tmp
        t += chr(ord(k[g]) ^ (h[(h[p] + h[f]) % 256]))
    return "http:" + t[26:]

if __name__ == '__main__':
    if not os.path.exists('./pics/'):
	os.mkdir('pics')
    if len(sys.argv) == 1:
        GetHash()
    if len(sys.argv) == 3:
        GetHash(sys.argv[1],sys.argv[2])
