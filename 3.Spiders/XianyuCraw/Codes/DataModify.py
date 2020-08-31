#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DataModify.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-06-12 15:32   Authorcai      1.0         爬虫练习
'''

# import lib
import random
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts.globals import WarningType
WarningType.ShowWarning = False

def dataGet(file_path):
    # 定义item_old用于存放初始商品描述
    item_old = {'商品描述':''}
    # 定义item_new 和 其他列表用于存放商品的其他特征信息
    season = ['春','夏','秋','冬','其他']
    size_1 = ['s','m','l','xl','xxl','其他']
    size_2 = ['160','165','170','175','180','其他']
    stand = ['adidas','阿迪达斯','耐克','贵人鸟','南极人','优衣库','zara','其他']
    style = ['学生','港风','英伦','潮牌','宽松','修身','polo','其他']
    type = ['短袖','长袖','上衣','裤','裙','卫衣','其他']
    material = ['纯棉','涤纶','']
    item_new = {'季节':'',
                '尺码':'',
                '品牌':'',
                '风格':'',
                '种类':''}
    items = []

    itemInfo = pd.read_csv(file_path, usecols=['商品描述'])

    # 定义item字典,其用于存储原始商品的'商品描述信息'
    num = 0

    # 遍历DataFrame的每行,统计城市的num
    for row in itemInfo.iterrows():
        item = row[1]['商品描述']
        items.append(item)

    # 将获取到的省份和数量转换为DataFrame
    Infoes = {'Cities': all_city, 'Num': nums}
    Infoes = pd.DataFrame(Infoes)

    # 将Infos写入到表格文件中
    Infoes.to_csv('/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/' + type + '_data_cities.csv',
                  sep=',', header=True, index=True)
    return Infoes
    return
