#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Yyk_Crawl.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-06-07 10:33   Authorcai      1.0         爬虫练习
'''

# import lib
import requests
import json
import os
import csv

# 定义函数用于获取数据
def CreateUrls():
    urls = {
        'hm': [
            'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=s&c=1&wd=h%26m&da_src=pcmappg.map&on_gel=1&l=5&gr=1&b=(10791381.798845354,3109633.7229259782;14055506.524756543,6852939.549588665)&&pn=0&auth=SV3aQL689PMv9fKZaae0D85TyFLzK5xeuxHTxNNBBNVtDpnSCE%40%40B1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3Guxtdw8E62qvMuTa4AZzUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuxtfvAughxehwzJVzPPDD4BvgjLLwWvrZZWuB&device_ratio=2&tn=B_NORMAL_MAP&nn=0&u_loc=13437544,3654207&ie=utf-8&t=1591773370952'],
        'uniqlo': [
            'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=s&c=1&wd=%E4%BC%98%E8%A1%A3%E5%BA%93&da_src=shareurl&on_gel=1&l=6&gr=1&b=(11578857.408287704,2665277.557463113;13697860.04207616,5103892.227464317)&pn=0&device_ratio=2&auth=%3DUEDYcMwaBTBxU1yPHPXVXZ%3DD99Rx4YeuxHTxETTBzxt1qo6DF%3D%3DC1GgvPUDZYOYIZuVtcvY1SGpuBtGfyMxXwGccZcuVtPWv3GuVtPYIuVtUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuVtegvcguxHTxETTBzxtfiKKv7urZZWuV&tn=B_NORMAL_MAP&nn=0&u_loc=13437490,3654265&ie=utf-8&t=1591499321742'],
        'zara': [
            'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=s&da_src=shareurl&wd=zara&c=1&src=0&pn=0&sug=0&l=5&b=(6822227.219999999,2174811.880000001;12458323.219999999,8638299.88)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2&auth=FY4VxWfHX6KUYU2cBRU3KdVdyF%3D%40W%3DJeuxHTxNNVHEEtDpnSCE%40%40B1GgvPUDZYOYIZuVtcvY1SGpuBtGfyMxXwGccZcuVtPWv3GuVtPYIuVtUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuVtegvcguxHTxNNVHEEthl44yYxrZZWuV&tn=B_NORMAL_MAP&nn=0&u_loc=13437544,3654207&ie=utf-8&t=1591770544636']
    }

    return urls

# 获取网页的json数据
def Crawl(url):
    headers = {"Accept": "*/*",
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
          'Connection': 'keep-alive',
          'Host': 'map.baidu.com',
          'Referer: https': '//map.baidu.com/search/%E4%BC%98%E8%A1%A3%E5%BA%93/@13432005.56,3644785.89,13z?querytype=s&c=224&wd=%E4%BC%98%E8%A1%A3%E5%BA%93&da_src=shareurl&on_gel=1&l=13&gr=1&b=(13401285.56,3629281.89;13462725.56,3660289.89)&pn=0&device_ratio=2',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-origin',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
          }
    r = requests.get(url,headers)
    return r.json()

def getData(urls):
    # urls = ['https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=s&c=1&wd=%E4%BC%98%E8%A1%A3%E5%BA%93&da_src=shareurl&on_gel=1&l=6&gr=1&b=(11578857.408287704,2665277.557463113;13697860.04207616,5103892.227464317)&pn=0&device_ratio=2&auth=%3DUEDYcMwaBTBxU1yPHPXVXZ%3DD99Rx4YeuxHTxETTBzxt1qo6DF%3D%3DC1GgvPUDZYOYIZuVtcvY1SGpuBtGfyMxXwGccZcuVtPWv3GuVtPYIuVtUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuVtegvcguxHTxETTBzxtfiKKv7urZZWuV&tn=B_NORMAL_MAP&nn=0&u_loc=13437490,3654265&ie=utf-8&t=1591499321742']
    for url in urls:
        currentInfo = []
        moreInfo = []
        data = Crawl(url)
        current_province = data['current_city']['up_province_name']
        current_city_info =  data['content']
        other_city_info = data['more_city']
        for city in current_city_info:
            l = []
            city_name = city['view_name'][:-1]
            city_num = city['num']
            # print('%-12s%-10s 所包含门店数量为%4d' % (current_province, city_name, city_num))
            l.append(city_name)
            l.append(city_name)
            l.append(city_num)
            currentInfo.append(l)
        for other_cities in  other_city_info:

            province = other_cities['province'][:-1]
            cities = other_cities['city']
            for city in cities:
                l = []
                other_city_num = city['num']
                other_city_name = city['name'][:-1]
                # print('%-12s%-10s 所包含门店数量为%4d' % (province, other_city_name, other_city_num))
                l.append(province)
                l.append(other_city_name)
                l.append(other_city_num)
                moreInfo.append(l)
        return currentInfo,moreInfo

def storeData(currentInfo, moreInfo,type):
    filepath = '/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/'+type+'_data.csv'
    with open(filepath,'a') as file:
        writer = csv.writer(file)
        rows = currentInfo+moreInfo
        for row in rows:
            print(row)
            writer.writerow(row)

def main():
    # 定义字典用于存储uniqlo,zara,hm等品牌的对应url
    urls = CreateUrls()

    # 获取对应的url
    currentInfo,moreInfo = getData(urls['hm'])
    storeData(currentInfo,moreInfo,'hm')
    currentInfo, moreInfo = getData(urls['uniqlo'])
    storeData(currentInfo, moreInfo, 'uniqlo')
    currentInfo, moreInfo = getData(urls['zara'])
    storeData(currentInfo, moreInfo, 'zara')

main()