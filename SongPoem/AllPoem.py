#!/usr/bin/python3
# -*- coding:utf8 -*-

'''
获取古诗文网http://www.gushiwen.org/gushi/quansong.aspx上的所有诗词并保存在 data/SongPoem中
'''

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://so.gushiwen.org/type.aspx?p='
CODE_FILE = 'E:\Python\AwesomeSpiders\data\AllPoem.txt'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    Poem_data = []
    soup = BeautifulSoup(html, "html.parser")
    Poem_list_soup = soup.find('div', attrs={'class': 'main3'})
    # print(Poem_list_soup)
    for Poem_son in Poem_list_soup.find_all('textarea'):
        # print(Poem_son.getText())
        Poem_data.append(Poem_son.getText())
    #获取下一页URL
    return Poem_data

def main():
    url = DOWNLOAD_URL
    number = 1
    with codecs.open(CODE_FILE, 'wb', encoding='utf-8') as fp:
        while number < 501:
            html = download_page(url + str(number))
            print(url + str(number))
            # print(html)
            number += 1
            Poem = parse_html(html)
            fp.write(u'{Poem}\n'.format(Poem='\n'.join(Poem)))

if __name__ == '__main__':
    main()
