'''
crawler for jandan.net/ooxx
'''
import re
import sys
import time
import requests
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
url = 'http://jandan.net/ooxx'

driver = webdriver.Chrome()
try:
    driver.get(url)
    time.sleep(2)
    page = driver.page_source
    counts = re.findall('current-comment-page">.*</s', page)[0]
    cou = re.findall('[0-9]{1,4}', counts)
    cou = int(cou[0])
    for i in range(406, cou+1): #start-page to end-page
        url = 'http://jandan.net/ooxx/page-'+str(i)+'#comments'
        driver.get(url)
        page = driver.find_element_by_id('comments').get_attribute("innerHTML")
        pic = re.findall('(p><a href=".*?jpg|p style="position: relative;"><a href=".*?gif|p><a href=".*?png)',page)
        print i
        for j in pic:
            url = 'http:' + j[j.find('/'):]
            #print url
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
finally:
    driver.quit()
