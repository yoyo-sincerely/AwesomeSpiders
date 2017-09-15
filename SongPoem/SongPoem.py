#!/usr/bin/python3
# -*- coding:utf8 -*-

'''
获取古诗文网http://www.gushiwen.org/gushi/quansong.aspx上的所有诗词并保存在 data/SongPoem中
'''

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://www.gushiwen.org/gushi/quansong.aspx/'
CODE_FILE = 'E:\Python\AwesomeSpiders\data\SongPoem.txt'


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
    Poem_list_soup = soup.find('div', attrs={'class': 'typecont'})
    Poem_href_list = []
    Poem_name_list = []
    # f.write(Poem_list_soup)
    # print(Poem_list_soup.prettify())

    o = urlparse(DOWNLOAD_URL)
    proto = o.scheme
    domain = o.netloc

    for Poem_span in Poem_list_soup.find_all('span'):
        Poem_a = Poem_span.find('a')
        # print(Poem_a)
        Poem_href = Poem_a.attrs['href']
        Poem_name = Poem_a.getText()
        # print(Poem_href, Poem_name)
        Poem_Url = proto + '://' + domain + Poem_href
        # print(Poem_Url)
        Poem_name_list.append(Poem_name)
        Poem_href_list.append(Poem_Url)
    return Poem_href_list

def getPoem(Poem_href_list):
    # for Poem_Url in Poem_href_list:
    #     Poem_html = download_page(Poem_Url)
    Poem_data_list = []

    # Poem_html = download_page(Poem_href_list[0])
    for Poem_URL in Poem_href_list:
        print(Poem_URL)
        Poem_html = download_page(Poem_URL)
        Poem_soup = BeautifulSoup(Poem_html, "html.parser")
        Poem_list = Poem_soup.find('div', attrs = {'class' : 'contson'})
        # f = open(CODE_FILE, 'wb')
        # f.write(Poem_list)
        # f.close()
        for Poem_data in Poem_list.find_all('p'):
            Poem_data_list.append(Poem_data.getText())
            # print(Poem_data.getText())
        # print(Poem_list.encode(gbk))
    return Poem_data_list

def ok():
    url = DOWNLOAD_URL
    html = download_page(url)
    getPoem(parse_html(html))
    with codecs.open(CODE_FILE, 'wb', encoding='utf-8') as fp:
        for Poem in getPoem(parse_html(html)):
            fp.write(u'{Poem}\n'.format(Poem=''.join(Poem)))
    #     while url:
    #         html = download_page(url)
    #         fp.write(html)
    #         parse_html(html)
            # fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

if __name__ == '__main__':
    ok()
