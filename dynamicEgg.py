from splinter import Browser
from bs4 import BeautifulSoup
import os
import urllib.request
import threading
import sys
import time
import random


def setBrowser():
    browser = Browser(driver_name='phantomjs', user_agent=[
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
    ], load_images=False)
    return browser


def startDown(browser, begin, end):
    for page_num in range(begin, end):
        os.mkdir('ooxx')
        os.chdir('ooxx')
        if not os.path.exists(str(page_num)):
            os.mkdir(str(page_num))
        os.chdir(str(page_num))
        browser.visit('http://jandan.net/ooxx/page-' + str(page_num) + '#comments')
        html = browser.html
        Soup = BeautifulSoup(html, 'lxml')
        lists = Soup.find_all('a', {'class': 'view_img_link'})
        for img in lists:
            fileName = img.get('href').split('/')[-1]
            if os.path.exists(fileName):
                continue
            req = urllib.request.Request(img.get('href'))
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
            with open(fileName, 'wb') as f:
                f.write(urllib.request.urlopen(req, timeout=11).read())
            print(threading.Thread.name, ' :Save picture', fileName, 'succeessed')
            time.sleep(random.randint(1, 3))


def start(begin, end):
    browser = setBrowser()
    startDown(browser, begin, end)


if __name__ == 'main':
    start(sys.argv[1], sys.argv[2])
