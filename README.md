Download
========

A script to scrape a webpage and download desired file-types.
Includes a parodyBrowser (adds Headers for webpages that forbid scripts)

An interesting observation: HTTPResponses can only be read once.

<h4>External Dependencies</h4>
The program requires the package BeautifulSoup4.

<h4>Quick and Dirty ways of installing BeautifulSoup</h4>
This is copied from the package website to save a little time. <br />
Source: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup <br />

If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

$ apt-get install python-bs4

Beautiful Soup 4 is published through PyPi, so if you can’t install it with the system packager, you can install it with easy_install or pip. The package name is beautifulsoup4, and the same package works on Python 2 and Python 3.

$ easy_install beautifulsoup4

$ pip install beautifulsoup4

<a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup">Read More</a>
<h4>TODO:</h4>
Build my own html-parser or use built-in libraries.
Motivation: I don't want the script to be dependent on external packages (or break more often than it should). 
