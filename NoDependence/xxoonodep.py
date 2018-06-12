# -*- coding: utf-8 -*-
'''
Have fun.

python 2

@author: B1u3Buf4
'''
import hashlib
import base64
import requests
import re
import sys
import os
import time


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}  
record = ['http://jandan.net/ooxx/'+'\n']
flag = True


def FirstReq():
    with open('allurls.txt', 'r') as log:
        allurls = list(set(log.readlines()))
    r = requests.get('http://jandan.net/ooxx/',headers = headers)
    maxpage = int(re.findall('current-comment-page">\[(\d*?)\]',r.text)[0])
    for i in range(maxpage,0,-1):
        print i
        stime = time.time()
        r = requests.get('http://jandan.net/ooxx/page-' + str(i) + '#comments', headers=headers)
        total = re.findall('img-hash">.*?<', r.text)
        for j in total:
            tmp = base64.b64decode(j[10:-1])
            tmp = re.sub('cn/.*?/','cn/large/',tmp)
            tmp = 'http:' + tmp
            if tmp + '\n' not in allurls:
                print '[+]',tmp
                rr = requests.get(tmp, headers = headers)
                with open('./pics/' + tmp[tmp.rfind('/') + 1:], 'wb') as f:
                    f.write(rr.content)
                with open('allurls.txt', 'a') as log:
                    log.write(tmp + '\n')
        sptime = time.time() - stime
        if sptime < 5:
            time.sleep(5 - sptime)

if __name__ == '__main__':
    if not os.path.exists('./pics/'):
        os.mkdir('pics')
    if len(sys.argv) == 1:
        FirstReq()
