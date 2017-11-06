#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'

'''
利用高德地图api实现地址和经纬度的转换
'''
import time
import json
import test as G
import Spider as S
import codecs

DATA_JSON = '..\data\LianJia.json'
CODE_FILE = '..\data\LianJiaBest.txt'
CODE_FILE_DATA = '..\data\LianJia.txt'
CODE_FILE_TEMP = '..\data\LianJiaTemp.txt'
ADDRESS = '上海市'

def read_data():
    house_list = []
    f = codecs.open(CODE_FILE_DATA, 'rb', encoding='utf-8')
    i = 0
    house_title = ""
    house_address = ""
    house_price = ""
    house_time = ""
    house_duration = 0
    house_duration_str = ""
    house_cost = ""

    for line in f:
        if i % 9 == 0:
            house_title = line
        elif i % 9 == 1:
            house_address = ADDRESS + line
        elif i % 9 == 2:
            house_price = line.replace('月租:', '')
        elif i % 9 == 3:
            house_time = line
        elif i % 9 == 4:
            house_duration = line
        elif i % 9 == 5:
            house_duration_str = line
        elif i % 9 == 6:
            house_cost = line
        elif i % 9 == 7:
            house_href = line
        else:
            house_temp = S.house(house_title, house_address, house_price, house_time, house_duration, house_duration_str, house_cost, house_href)
            house_list.append(house_temp)
            # print(house_temp.getInfo())
        i += 1
    f.close()
    return house_list

def write_data(house_list):
    print(len(house_list))

    f = codecs.open(CODE_FILE, 'wb+', encoding='utf-8')

    for house in house_list:
        f.write(house.getInfo())

    f.write("总数量： " + str(len(house_list)))
    f.close()

def get_data():
    house_list = S.main()
    print(len(house_list))
    f = codecs.open(CODE_FILE_TEMP, 'wb+', encoding='utf-8')
    for house in house_list:

        address = ADDRESS + house.address.replace('\n', '')
        house.duration, house.duration_str, house.cost = G.getPathTime(address)
        print(house.getInfo())
        f.write(house.getInfo())
    f.close()

def write_json(house_list):
    # list = json.dumps(house_list)
    # print(list)
    f = codecs.open(DATA_JSON, 'wb+', encoding='utf-8')
    for house in house_list:
        # print(house.toJSON())
        f.write(house.toJSON())
    f.close()

def read_json():
    pass

def test_get_data():
    f = codecs.open(CODE_FILE_TEMP, 'wb+', encoding='utf-8')
    address = "上海市丽泽梅傲苑"
    house = S.house()
    house.address = address
    print(house.getInfo())
    f.write(house.getInfo())
    f.close()

def sort_data(house_list):
    # 升序排列
    house_list_sorted = sorted(house_list, reverse=False)
    return house_list_sorted

if __name__=='__main__':
    # address = input("请输入地址:")
    # get_data()
    # test_get_data()
    house_list = read_data()
    # house_list = sort_data(house_list)
    # write_data(house_list)
    write_json(house_list)