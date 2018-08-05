# -*- coding: utf-8 -*-
'''
Have fun.

python 3

@author: B1u3Buf4
'''
import hashlib
import base64
import requests
import re
import sys
import os
import time


def none_md5():
    with open('None.jpg','rb') as f:
        res = hashlib.md5(f.read()).hexdigest()
    return res

def FirstReq():
    nonemd5 = none_md5()
    print(nonemd5)
    nonemd5 = '9fb3b83b96c82eb08412279e4c0fa539'
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
        with open('hash.txt', 'r') as log:
            allurls = list(set(log.readlines()))
        r = requests.get('http://jandan.net/ooxx/', headers = headers)
        maxpage = int(re.findall('current-comment-page">\[(\d*?)\]', r.text)[0])
        for i in range(maxpage, 0, -1):
            print(i)
            stime = time.time()
            r = requests.get('http://jandan.net/ooxx/page-' + str(i) + '#comments', headers=headers)
            total = re.findall('img-hash">.*?<', r.text)
            for j in total:
                tmp = base64.b64decode(j[10:-1]).decode('utf-8')
                tmp = re.sub('cn/.*?/','cn/large/', tmp)
                tmp = 'http:' + tmp
                rr = requests.get(tmp, headers = headers)
                tmphash = hashlib.md5(rr.content).hexdigest()
                if tmphash is nonemd5:
                    print('[x]', tmp)
                    continue
                if tmphash + '\n' not in allurls:
                    print('[+]', tmp)
                    with open('./pics/' + tmp[tmp.rfind('/') + 1:], 'wb') as f:
                        f.write(rr.content)
                    with open('hash.txt', 'a') as log:
                        log.write(tmphash + '\n')
                else:
                    print('[-]', tmp)
            sptime = time.time() - stime
            if sptime < 5:
                time.sleep(5 - sptime)
    except Exception as e:
        print('[x] Error!',e)

if __name__ == '__main__':
    if not os.path.exists('./pics/'):
        os.mkdir('pics')
    if len(sys.argv) == 1:
        FirstReq()
