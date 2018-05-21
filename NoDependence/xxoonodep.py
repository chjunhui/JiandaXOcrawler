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
import time


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}  
record = ['http://jandan.net/ooxx/'+'\n']
flag = True
with open('record.txt', 'r') as f:
    record.extend(f.readlines())

def FirstReq():
    banner = 0
    with open('allurls.txt', 'r') as log:
	allurls = list(set(log.readlines()))
    while banner < len(record):
	r = requests.get(record[banner][:-1], headers=headers)
	for i in re.findall('jandan.net/ooxx/page-.*?#comments', r.text):
	    if 'http://' + i + '\n' not in record:
		record.append('http://' + i + '\n')
	total = re.findall('img-hash">.*?<', r.text)
	print len(total)
	for j in total:
	    tmp = base64.b64decode(j[10:-1])
	    tmp = re.sub('cn/.*?/','cn/large/',tmp)
	    tmp = 'http:' + tmp
	    if tmp + '\n' not in allurls:
		print(tmp)
		rr = requests.get(tmp, headers = headers)
		with open('./pics/' + tmp[tmp.rfind('/') + 1:], 'wb') as f:
		    f.write(rr.content)
		with open('allurls.txt', 'a') as log:
		    log.write(tmp + '\n')
	banner += 1
	time.sleep(5)

if __name__ == '__main__':
    if not os.path.exists('./pics/'):
	os.mkdir('pics')
    if len(sys.argv) == 1:
        FirstReq()
    #if len(sys.argv) == 3:
    #    GetHash(sys.argv[1],sys.argv[2])
