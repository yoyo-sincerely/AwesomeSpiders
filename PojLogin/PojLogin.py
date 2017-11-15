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
           "Accept-Encoding":"gzip, deflate",
           "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
           "Connection":"keep-alive",
           "Cookie":"JSESSIONID=8D62C31EEA3A0B28E778FCC2EAF05E59; __utmt=1; __utma=79247125.1777514053.1509936862.1510134604.1510710828.7; __utmb=79247125.4.10.1510710828; __utmc=79247125; __utmz=79247125.1510020154.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
           }

# 尝试使用cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookies未能加载")
    # cookies加载不成功，则输入账号密码信息
    datas['form_account'] = "yoyo1995"
    datas['form_password'] = "yoyo331200"
    
login = None
Poj_session = requests.session()

def main():
    f = Poj_session.get(url, headers = headers)
    soup = BeautifulSoup(f.content,"html.parser")
    txt = open(TXT, 'w', encoding = 'utf-8')
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
    login_code = Poj_session.get(url, headers=headers,
                             allow_redirects=False).status_code
    print(login_code)
    if login_code == 200:
        return True
    else:
        return False

def login():
    # datas['u'] = "yoyo1995"
    # datas['p'] = "yoyo331200"
    datas['B1'] = login
    datas['url'] = '/'
    print(datas)
    response = Poj_session.post(url, data=datas, headers=headers)
    login_page = Poj_session.get(url, headers=headers)

    problemlist = open(PROBLEMLIST, 'w', encoding = 'utf-8')
    # print(login_page.content)
    soup = BeautifulSoup(login_page.content,"html.parser")
    problemlist.write(soup.prettify())
    problemlist.close()
    # session.cookies.save()

if __name__ == '__main__':
    main()
    login()
    if isLogin():
        print("Login Successful!")
    else:
        print("Login Failed!")
