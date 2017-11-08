#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'

'''
Poj.org模拟登陆与模拟提交并返回结果

Required
- requests (必须)
- bs4 (必选)

user: yoyo1995
pass: yoyo331200

http://poj.org/loginlog
http://poj.org/problemlist
'''
import sys, codecs, os
import requests
from bs4 import BeautifulSoup
try:
    import cookielib
except:
    import http.cookiejar as cookielib

TXT = '..\\data\\POJ\\PojLoginLog.txt'
PROBLEMLIST = '..\\data\\POJ\\ProblemList.txt'

url = 'http://poj.org'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

datas = {}

headers = {'Host':'poj.org',
           'Referer': 'http://poj.org/',
           'User-Agent': UA,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
           'Accept-Encoding':'gzip, deflate'}

# 尝试使用cookie信息
session = requests.session()
# session.cookies = cookielib.LWPCookieJar(filename='cookies')
# try:
#     session.cookies.load(ignore_discard=True)
# except:
#     print("Cookies未能加载")
#     #cookies加载不成功，则输入账号密码信息
#     datas['form_account'] = "yoyo1995"
#     datas['form_password'] = "yoyo331200"
login = None

def main():
    txt = open(TXT, 'w', encoding = 'utf-8')

    Poj_session = requests.session()
    f = Poj_session.get(url, headers = headers)
    soup = BeautifulSoup(f.content,"html.parser")
    txt.write(soup.prettify())
    
    login_td = soup.find('form', {'action':'login'})
    login = login_td.find('input',{'name':'B1'})['value']
    print(login)

    txt.close()

def isLogin():
    '''
    通过查看用户个人账户信息来判断是否已经登录
    '''
    url = "http://poj.org/loginlog"
    login_code = session.get(url, headers=headers,
                             allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False

def login():
    datas['user_id1'] = "yoyo1995"
    datas['password1'] = "yoyo331200"
    datas['B1'] = login
    login_page = session.post(url, data=datas, headers=headers)
    problemlist = open(PROBLEMLIST, 'w', encoding = 'utf-8')
    print(login_page.content)
    soup = BeautifulSoup(login_page.content,"html.parser")
    problemlist.write(soup.prettify())
    problemlist.close()
    # session.cookies.save()

if __name__ == '__main__':
    main()
    login()