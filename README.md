# jiandan.net/xxoo crawler

Crawler for jiandan.net/xxoo girl's pics. Friendly and for fun.

煎蛋妹子图爬虫。友好地单线程和请求延迟。项目只是为了好玩。

下载后，安装依赖模块，运行即可。

随缘Watch、Star。

## Usage

Work with: **python 2**

python2代码

rely on **selenium**、**requests**

依赖**selenium**、**requests**。

Install dependent modules:

    pip install selenium
	pip install requests

Then just run this script.

~~Otherwise, you need to install basic tools:~~
> ~~Chrome~~
> 
> ~~chromedriver.exe~~

~~**chromedriver.exe** need you to add it in system **PATH**. If you have installed it successfully, you are able to run it in shell.~~

## By the way

The jiandan.net/xxooo web server could check **User-Agent** in your request header, but it only checks whether it has the tag or not.

Owing to the script automatically can hide bad content, pics you get are not whole.

## Change logs

2月5日：更新之后默认爬取所有图片，包括折叠内容。

2/5:crawl all pics, including those folded.

2月20日：讲原本依赖的chrome变为phantomJS，添加到项目中，性能有所提升。

2/20：The Web browser has changed from chrome to phantomJS and added it in the project. Improved performance.