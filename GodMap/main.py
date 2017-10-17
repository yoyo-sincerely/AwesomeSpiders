#!/usr/bin/python3
# -*- coding:utf8 -*-
__author__ = 'yoyo_sincerely'

'''
利用高德地图api实现地址和经纬度的转换
'''
import time
import test as G
import Spider as S

if __name__=='__main__':
    # address = input("请输入地址:")
    # S.main()
    f = open(S.CODE_FILE, 'wb')
    address1 = '上海市陆家嘴软件园10号楼'
    address2 = '上海市'
    house_list, nexturl = S.main()
    for house in house_list:
        # print(house.address)
        address = address2 + house.address.replace('\n', '')
        house.duration, house.duration_str, house.cost = G.getPathTime(address1, address)
        print(house.getInfo())
        f.write(house.getInfo().encode('utf-8'))
    # S.pares_html(html)
    # G.getPathTime(address1, address2)
    f.close()
