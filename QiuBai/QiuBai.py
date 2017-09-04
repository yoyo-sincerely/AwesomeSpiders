#!/usr/bin/python3
# -*- coding:utf8 -*-

'''
获取糗事百科成人版的图片
'''

import requests
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'http://www.qiubaichengren.com/'
IMG_FILE = 'E:\\Python\\AwesomeSpiders\\data\\IMG_QiuBaiChengRen\\'


def load_page_html(url):
    ''' 得到页面的HTML文本 '''
    log('Get a html page : ' + url)
    return urllib.urlopen(url).read()

def download_qiushichengren(fro = 1, pageCount = 10, save_dir):
    for x in xrange(fro, pageCount):
        log('Page : ' + `x`)
        download_Img(x, save_dir)

def main():
    download_qiushichengren(fro, pageCount, save_dir = IMG_FILE)

if __name__ == '__main__':
    main()
