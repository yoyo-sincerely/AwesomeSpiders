#!/usr/bin/python3
# -*- coding:utf8 -*-

'''
获取豆瓣电影的网页信息，并保存至data/page.中
'''

import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://movie.douban.com/top250/'
CODE_FILE = 'E:\Python\AwesomeSpiders\data\DouBan.txt'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    # f = open(CODE_FILE, 'w',encoding="utf8")

    soup = BeautifulSoup(html, "html.parser")
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    movie_name_list = []

    # f.write(soup.prettify())
    for movie_li in movie_list_soup.find_all('li'):
        # f.write(str(movie_li))
        detail = movie_li.find('div', attrs={'class': 'hd'})
        # f.write(str(detail))
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()
        # f.write(str(movie_name) + '\n')
        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    # f.close()
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None

def main():
    url = DOWNLOAD_URL

    with codecs.open(CODE_FILE, 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

if __name__ == '__main__':
    main()
