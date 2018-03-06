# jiandan.net/xxoo crawler

![work with](https://img.shields.io/badge/python-2.X-orange.svg)
![work with](https://img.shields.io/badge/python-3.X-green.svg)

Crawler for jiandan.net/xxoo girl's pics. Friendly and for fun.

python2使用phantomJS；python3使用headless Chrome。

煎蛋妹子图爬虫。友好地单线程和请求延迟。项目只是为了好玩。

喜欢请Star。

Plz star，if U like.

## Usage ##

### Comment setp: ###

rely on **selenium**、**requests**

依赖**selenium**、**requests**。

Install comment dependent modules:

    pip install selenium
	pip install requests

### Difference: ###

If you use py2: just run `XXOO2.py` in `./old/`.

If you use py3, you need to install additional tools:
> Chrome
> 
> [chromedriver.exe](http://chromedriver.storage.googleapis.com/)

[chromedriver mirror in Alibaba](http://npm.taobao.org/mirrors/chromedriver/)

**Waring**:

**chromedriver.exe** need you to add it in `SYSTEM PATH`. If you have installed it successfully, you are able to run it in shell or cmd.

The **py3-script** uses a Headless Chrome method, so type `chrome://version/` in address bar and check Chrome version. Make sure your Chrome browser version:

    Windows >= 60.x
    Linux >= 59.x

## By the way

The jiandan.net/xxooo web server could check **User-Agent** in your request header, but it only checks whether it has the tag or not.

~~Owing to the script automatically can hide bad content, pics you get are not whole.~~

## Change logs

2月5日：更新之后默认爬取所有图片，包括折叠内容。

2/5:crawl all pics, including those folded.

2月20日：将原本依赖的chrome变为phantomJS，添加到项目中，性能有所提升。

2/20：The Web browser had changed from chrome to phantomJS and added it in the project. Improved performance.

3月6日：添加python3代码，python2不再更新；python3使用Headless Chrome;python3代码中调整采集策略;细节修改。

3/6: Added python3 code, python2 code would not upgrade anymore; Used the Headless Chrome replace phantomJS in python3 code; Changed crawling strategy in python3 code; Some details modified.