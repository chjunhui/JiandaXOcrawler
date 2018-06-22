# jiandan.net/xxoo crawler #

![work with](https://img.shields.io/badge/py2-NoBrowser-green.svg)
![work with](https://img.shields.io/badge/py3-Browser&Selenium-blue.svg)
![work with](https://img.shields.io/badge/py2-Browser&Selenium-red.svg)

Crawler for jiandan.net/xxoo girl's pics. Friendly and for fun.

python2使用phantomJS；python3使用headless Chrome。

煎蛋妹子图爬虫。友好地单线程和请求延迟。项目只是为了好玩。

推荐使用无浏览器版本（NoBrowser script），保持对煎蛋robots.txt的尊重，间隔时间会要求在大于等于5秒的范围内。

~~多线程需要根据网络质量慎重选择并发量，否则可能下载出错。调整改进了策略，采用先采集后下载的策略。考虑图片越来越少，没有再加进度保存的功能，但可以通过手动修改`start-page`指定开始位置。~~

**好用请Star。**

## ToDo

暂时没有

## 伸手党

可以直接用请求器（本仓库不含）读取`NoDependence`下的`allurls.txt`文件，注意去掉每行最后的`'\n'`。

不保证是最新的内容，因为不会每天都爬，记录的是测试时的访问。

## NoBrowser script Usage ##

不依赖浏览器版的煎蛋妹子图爬虫，实现了同解密的JS一样的算法，目前可用。单线程，保持5秒一次的友好请求。通过日志来跳过已经下载的图片。

before using:

    pip install requests

（Test env: Windows, py2）

Change CMD to `NoDependence`, then type `python xxoonodep.py` or `python xxoonodep.py start-page end-page`. Caution: make sure start-page always end-page

切换到`NoDependence`目录下，`python xxoonodep.py`默认从头开始爬取所有的内容，`python xxoonodep.py start-page end-page`选择性地爬取内容。注意输入。如果输入的结束位置大于现实值，可能导致为止的问题，暂时无测试和应对。

Warning:

CDN Cache(I guess) may make the script get a non-existent JS file and make it break. If so, wait for some time and retry it.

## The script wokring with browser Usage ##

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

## BTW ##

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

3月24日：因为现在煎蛋妹子图没有那么多了，干脆暴力一点，在微博取图的阶段使用了`multiprocessing`。

3/24: Use `multiprocessing` to make script more powerful.

5月16日：逆向解密的JS并完成了这个JS解密的python脚本。

5/16: Analyze the crypto algorithm in JS and use python achieve so.

5月21日：应对改版重写了脚本。（Knick your ass.）

5/21: Rewrite the code owing to HTML changed.

5月25日：粗略计算总页数并优化了间隔时间。

5/25: Roughly, calculate a total number of pages. Delay time is optimised.

6月22日：不依赖浏览器的版本从python2升级到了python3。基于文件二进制内容的哈希值计算值的去重。间接地避免基于图片名称去重时，被和谐的图片再次采集时会覆盖同名文件。

6/22:  The no-browser script has changed from python2 to python3.
