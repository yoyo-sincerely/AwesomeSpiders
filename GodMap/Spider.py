#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'
'''
爬取链家网站获取房租与地址
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import codecs

DOWNLOAD_URL = 'http://sh.lianjia.com/zufang/pudong/' # d1z1
CODE_FILE = '..\data\LianJia.txt'

class house(object):
    def __init__(self, title, address, price, time):
        self.title   = title
        self.address = address
        self.price   = price
        self.time    = time
        self.duration = 0
        self.duration_str = ""
        self.cost    = ""

    def getInfo(self):
        info = ""
        info += self.title
        info += self.address
        info += "月租:" + self.price
        info += self.time
        info += str(self.duration) + '\n'
        info += self.cost + '\n'+ '\n'
        return info

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    # f = open(CODE_FILE, 'wb')
    # f.write(html)
    soup = BeautifulSoup(html, "html.parser")
    list_wrap = soup.find('div', attrs={'class': 'list-wrap'})
    # f.write(list_wrap.prettify().encode('utf-8'))
    # print(list_wrap.prettify())
    house_list = []
    for house_li in list_wrap.find_all('li'):
        # f.write(house_li.encode('utf-8'))
        # print(house_li)

        house_info = house_li.find('div', attrs={'class': 'info-panel'})

        house_title = house_info.find('h2').getText()
        house_title = clean_data(house_title)
        # f.write(house_title.encode('utf-8'))

        house_where = house_info.find('div', attrs={'class': 'where'})\
            .find('a', attrs={'class': 'laisuzhou'}).getText()
        house_where = clean_data(house_where)
        # f.write(house_where.encode('utf-8'))

        house_price = house_li.find('div', attrs={'class': 'col-3'})\
            .find('span', attrs={'class': 'num'}).getText()
        # house_price += '\n'
        house_price = clean_data(house_price)
        # f.write(house_price.encode('utf-8'))

        house_time =  house_li.find('div', attrs={'class': 'col-3'})\
            .find('div', attrs={'class': 'price-pre'}).getText()
        # house_time += '\n'
        house_time = clean_data(house_time)
        # f.write(house_time.encode('utf-8'))

        temphouse = house(house_title, house_where, house_price, house_time)
        house_list.append(temphouse)

    nexturl = soup.find('div', attrs={'class': 'page-box house-lst-page-box'})\
        .find('a',attrs={'gahref': 'results_next_page'}).get('href')

    o = urlparse(DOWNLOAD_URL)
    proto = o.scheme
    domain = o.netloc

    nexturl = proto + '://' + domain + nexturl
    # f.write(nexturl.encode('utf-8'))
    # f.close()

    return house_list, nexturl

def clean_data(data):
    cleaned_data = data
    # 清理回车与tab
    cleaned_data = cleaned_data.replace('\n', '')
    cleaned_data = cleaned_data.replace('\t', '')

    cleaned_data = cleaned_data + '\n'
    return cleaned_data

def main():
    url = DOWNLOAD_URL + 'd1z1'
    html = download_page(url)

    house_list, nexturl = parse_html(html)
    return house_list, nexturl
    # with codecs.open(CODE_FILE, 'wb', encoding='utf-8') as fp:
    #     while url:
    #         html = download_page(url)
    #         fp.write(parse_html(html))

if __name__=='__main__':
    main()