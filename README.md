# jiandan.net/xxoo crawler #

![work with](https://img.shields.io/badge/python-2.X-red.svg)
![work with](https://img.shields.io/badge/python-3.X-green.svg)

Crawler for jiandan.net/xxoo girl's pics. Friendly and for fun.

python2使用phantomJS；python3使用headless Chrome。

煎蛋妹子图爬虫。~~友好地单线程和请求延迟~~。项目只是为了好玩。

已经改为暴力的多线程。改进了策略，采用先采集后下载的策略。考虑图片越来越少，没有再加进度保存的功能，但可以通过手动修改`start-page`指定开始位置。

喜欢请Star。

## Usage ##

### Comment setp: ###

rely on **selenium**、**requests**

依赖**selenium**、**requests**。

Install comment dependent modules:

    pip install -r requirements.txt

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

    Chrome(Windows) >= 60.x
    Chrome(Linux) >= 59.x

## By the way ##

图片去重的demo在我的[另一个仓库](https://github.com/B1u3Buf4/de-duplication)里。

挖一个坑：准备挖一下微博相册上的老司机，在[这个仓库](https://github.com/B1u3Buf4/WeiboDriver)中。

The jiandan.net/xxooo web server could check **User-Agent** in your request header, but it only checks whether it has the tag or not.

~~Owing to the script automatically can hide bad content, pics you get are not whole.~~

## Change logs ##

2月5日：更新之后默认爬取所有图片，包括折叠内容。

2/5:crawl all pics, including those folded.

2月20日：将原本依赖的chrome变为phantomJS，添加到项目中，性能有所提升。

2/20：The Web browser had changed from chrome to phantomJS and added it in the project. Improved performance.

3月6日：添加python3代码，python2不再更新；python3使用Headless Chrome替代phantomJS；python3代码中调整采集策略；细节修改。

3/6: Added python3 code, python2 code would not upgrade anymore; Used the Headless Chrome replace phantomJS in python3 code; Changed crawling strategy in python3 code; Some details modified.

3月24日：因为现在煎蛋妹子图没有那么多了，干脆暴力一点，使用了`multiprocessing`。

3/24: Use `multiprocessing` to make script more powerful.
