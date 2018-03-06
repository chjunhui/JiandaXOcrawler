'''
crawler for jandan.net/ooxx
'''
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
driver = webdriver.Chrome(chrome_options = chrome_options)


def crawlurl():
    driver.get(url = 'http://jandan.net/ooxx')
    time.sleep(2)
    pics = []
    order = 1
    try:    
        page = driver.page_source
        counts = re.findall('current-comment-page">.*</s', page)[0]
        cou = re.findall('[0-9]{1,4}', counts)
        cou = int(cou[0])
        for i in range(38, cou+1): #start-page to end-page
            order = i
            print(order,len(pics))
            url = 'http://jandan.net/ooxx/page-' + str(i) + '#comments'
            driver.get(url)
            page = driver.find_element_by_id('comments').get_attribute("innerHTML")
            pics.extend(re.findall('(src=".*?jpg|src=".*?gif|src=".*?png)', page))
        return pics
    finally:
        print('[-]',order)
        driver.quit()


def getpic(pics):
    for j in pics:
        url = re.sub('cn/.*?/', 'cn/large/', j[5:])
        if 'jandan.net' in url:
            continue
        if url.find('http://') != 0:
            print('[-]',url)
            continue
        print(url)
        r = requests.get(url)
        name1 = re.findall('([a-zA-Z0-9]*?.jpg|[a-zA-Z0-9]*?.gif|[a-zA-Z0-9]*?.png)', j[-36:])
        with open('./pics/'+name1[0], "wb") as code:
            try:
                code.write(r.content)
            except:
                pass
        code.close()
        time.sleep(0.5)


getpic(crawlurl())