#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'
'''
爬取链家网站获取房租与地址
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
import codecs

DOWNLOAD_URL = 'http://sh.lianjia.com/zufang/pudong/' # d1z1
HOUSE_LIST = []

o = urlparse(DOWNLOAD_URL)
proto = o.scheme
domain = o.netloc

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    # f = open(CODE_FILE, 'wb')
    soup = BeautifulSoup(html, "html.parser")
    list_wrap = soup.find('div', attrs={'class': 'list-wrap'})
    for house_li in list_wrap.find_all('li'):
        nexturl = None
        house_info = house_li.find('div', attrs={'class': 'info-panel'})

        house_title = house_info.find('h2').getText()
        # house_title = clean_data(house_title)
        # f.write(house_title.encode('utf-8'))

        house_where = house_info.find('div', attrs={'class': 'where'})\
            .find('a', attrs={'class': 'laisuzhou'}).getText()
        # house_where = clean_data(house_where)
        # f.write(house_where.encode('utf-8'))

        house_price = house_li.find('div', attrs={'class': 'col-3'})\
            .find('span', attrs={'class': 'num'}).getText()
        # house_price += '\n'
        # house_price = clean_data(house_price)
        # f.write(house_price.encode('utf-8'))

        house_time =  house_li.find('div', attrs={'class': 'col-3'})\
            .find('div', attrs={'class': 'price-pre'}).getText()
        # house_time += '\n'
        # house_time = clean_data(house_time)
        # f.write(house_time.encode('utf-8'))

        temphouse = house(house_title, house_where, house_price, house_time)

        house_href = house_li.find('div', attrs={'class': 'pic-panel'})\
            .find('a', attrs={'class': 'rent js_triggerGray'}).get('href')
        temphouse.href = proto + '://' + domain + house_href
        # house_time = clean_data(house_time)
        HOUSE_LIST.append(temphouse)
    if soup.find('div', attrs={'class': 'page-box house-lst-page-box'}) \
            .find('a', attrs={'gahref': 'results_next_page'}) != None:
        nexturl = soup.find('div', attrs={'class': 'page-box house-lst-page-box'})\
            .find('a',attrs={'gahref': 'results_next_page'}).get('href')

    if nexturl != None:
        nexturl = proto + '://' + domain + nexturl

    return nexturl


def main():
    url = DOWNLOAD_URL + 'd1z1'

    while url:
        print(url)
        html = download_page(url)
        url = parse_html(html)

    return HOUSE_LIST

if __name__=='__main__':
    main()


class house(object):
    def __init__(self, title = "", address = "", price = "", time = "", duration = "0", duration_str = "", cost = "", href = ""):
        self.title          = title
        self.address        = address
        self.price          = price
        self.time           = time
        self.duration       = duration
        self.duration_str   = duration_str
        self.cost           = cost
        self.href           = href

    def getInfo(self):
        info = ""
        info += self.clean_data(self.title)
        info += self.clean_data(self.address)
        info += self.clean_data(self.price)
        info += self.clean_data(self.time)
        info += self.clean_data(self.duration)
        info += self.clean_data(self.duration_str)
        info += self.clean_data(self.cost)
        info += self.clean_data(self.href)
        info += '\n'
        return info

    def __lt__(self, other):
        return self.duration < other.duration

    def clean_data(self, data):
        if data == "" or None:
            return "信息缺失\n"
        cleaned_data = data
        # 清理回车与tab
        cleaned_data = cleaned_data.replace('\n', '')
        cleaned_data = cleaned_data.replace('\t', '')

        cleaned_data = cleaned_data + '\n'
        return cleaned_data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)