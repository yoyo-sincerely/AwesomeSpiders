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

'''
import requests
from bs4 import BeautifulSoup
 
url = "http://www.v2ex.com/signin"
UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"
 
header = { "User-Agent" : UA,
           "Referer": "http://www.v2ex.com/signin",
           }
 
v2ex_session = requests.Session()
f = v2ex_session.get(url,headers=header)
 
soup = BeautifulSoup(f.content,"html.parser")
once = soup.find('input',{'name':'once'})['value']
print(once)
 
postData = { 'u': 'yoyosincerely',
             'p': 'yoyo331200',
             'once': once,
             'next': '/'
             }
 
v2ex_session.post(url,
                  data = postData,
                  headers = header)
 
f = v2ex_session.get('http://www.v2ex.com/settings',headers=header)
print(f.content)