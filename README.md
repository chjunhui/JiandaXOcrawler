# jiandan.net/xxooo crawler

Crawler for jiandan.net/xxoo girl's pics. Friendly and for fun.

煎蛋妹子图爬虫。友好地单线程和请求延迟。项目只是为了好玩。

依赖selenium。

2月5日更新之后默认爬取所有图片，包括折叠内容。

## Usage

Work with: **python 2**

Type this command in shell to install **selenium**:

    pip install selenium

Otherwise, you need to install basic tools:
> Chrome
> 
> chromedriver.exe

**chromedriver.exe** need you to add it in system **PATH**. If you have installed it successfully, you are able to run it in shell.

## By the way

The jiandan.net/xxooo web server could check **User-Agent** in your request header, but it only checks whether it has the tag or not.

Owing to the script automatically can hide bad content, pics you get are not whole.