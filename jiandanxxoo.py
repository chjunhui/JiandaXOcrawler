import requests,re,time,os,hashlib

def xxoopwn():
    url = 'http://jandan.net/ooxx'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    r = requests.get(url,headers = headers)
    if(r.status_code == 200):
        counts = re.findall('current-comment-page">.*</s',r.text)[0]
        cou = re.findall('[0-9]{1,4}',counts)
        cou = int(cou[0])
        for i in range(277,cou+1):#277
            url = 'http://jandan.net/ooxx/page-'+str(i)+'#comments'
            r = requests.get(url,headers = headers)
            pic = re.findall('(src="/.*?jpg|src="/.*?gif|src="/.*?png)',r.text)
            print i
            for j in pic:
                url = 'http://'+j[7:]
                r = requests.get(url)
                name1 = re.findall('([a-zA-Z0-9]*?.jpg|[a-zA-Z0-9]*?.gif|[a-zA-Z0-9]*?.png)',j[-36:])
                with open('./pics/'+name1[0], "wb") as code:
                    try:
                        code.write(r.content)
                    except:
                        pass
                code.close()
                time.sleep(0.5)
            time.sleep(1)
            
def uniqueset():
    Path = './pics/'
    hashlist = []
    
    files=os.listdir(Path)
    for i in files:
        curfile=open(Path + i,'rb')
        curmd5=hashlib.md5(curfile.read()).hexdigest()
        curfile.close()
        if curmd5 not in hashlist:
            hashlist.append(curmd5)
        else:
            print "[-]",i
            os.remove(Path + i)

xxoopwn()
uniqueset()