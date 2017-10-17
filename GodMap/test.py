#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'
'''
利用高德地图api实现地址和经纬度的转换
'''
import requests

# class GodMap:
AddressFrom = ""
AddressTo = ""
def geocode(address):
    parameters = {'address': address, 'key': '9711da59fb2de44dfad6f2dd69c590d0'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    return answer['geocodes'][0]['location']

def dealTime(time):
    totalTime = ""
    time = int(time)
    if time >= 86400 :
        print("大于一天！")
        totalTime += str(time//86400) + "天"
    if time >= 3600 :
        totalTime += str(time//3600) + "时"
    time = time % 3600
    if time >= 60 :
        totalTime += str(time//60) + "分"
    time = time % 60
    if time > 0 :
        totalTime += str(time) + "秒"
    return totalTime

def getPathTime(addressFrom, addressTo):
    gpsFrom = geocode(addressFrom)
    gpsTo   = geocode(addressTo)
    print(addressFrom + " 的GPS值为： " + gpsFrom)
    print(addressTo+ " 的GPS值为： " + gpsTo)
    parameters = {'key': '9711da59fb2de44dfad6f2dd69c590d0',
                  'origin': gpsFrom, 'destination': gpsTo, 'city': '021'}
    base = 'http://restapi.amap.com/v3/direction/transit/integrated'
    response = requests.get(base, parameters)
    answer = response.json()
    # return
    totalTime = dealTime(answer['route']['transits'][0]['duration'])
    # print(answer['route']['transits'][0]['duration'])
    duration_str = "从 " + addressFrom + " 到 " + addressTo + " 公交路径规划时间最短为： " + totalTime
    cost = "总花费" + answer['route']['transits'][0]['cost']
    return answer['route']['transits'][0]['duration'], duration_str, cost