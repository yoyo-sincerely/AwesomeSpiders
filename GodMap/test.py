#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'
'''
利用高德地图api实现地址和经纬度的转换
'''
import requests

# class GodMap:
AddressFrom = ""
AddressTo = '上海市陆家嘴软件园10号楼'
Goal = '121.532609,31.216663'

def geocode(address):
    parameters = {'address': address, 'key': '9711da59fb2de44dfad6f2dd69c590d0'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    if answer['infocode'] != '10000':
        print("消息异常！！！")
        print(response.text)
        return None
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

def getPathTime(addressFrom ):
    gpsFrom = geocode(addressFrom)
    # print(type(gpsFrom)
    print(addressFrom + " 的GPS值为： " + gpsFrom)
    print(AddressTo + " 的GPS值为： " + Goal)
    parameters = {'key': '0ba66e9484832ca9f3545a848cc0f245',
                  'origin': gpsFrom, 'destination': Goal, 'city': '021'}
    base = 'http://restapi.amap.com/v3/direction/transit/integrated'
    response = requests.get(base, parameters)
    # print(response.text)
    answer = response.json()
    # return
    if answer['infocode'] != '10000':
        print("消息异常！！！")
        print(response.text)
        return None
    totalTime = dealTime(answer['route']['transits'][0]['duration'])
    # print(answer['route']['transits'][0]['duration'])
    duration_str = "从 " + addressFrom + " 到 " + AddressTo + " 公交路径规划时间最短为： " + totalTime + '\n'
    # if answer['route']['transits'][0]['cost']
    # print ('answer: ' + str(type(answer['route']['transits'][0]['cost'])))
    # if isinstance(answer['route']['transits'][0]['cost'], list) :
    #     print("list")
    #     print(answer['route']['transits'][0]['cost'][0])
    cost = "总花费" + answer['route']['transits'][0]['cost'] + '\n'
    # print(cost)
    return answer['route']['transits'][0]['duration'], duration_str, cost

def main():
    Goal   = geocode(AddressTo)
    print(AddressTo+ " 的GPS值为： " + Goal)

if __name__=='__main__':
    main()
