# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MapSet.py
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-06-08 11:24   Authorcai      1.0         爬虫练习
'''

# 导入第三方库
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts
from pyecharts.globals import WarningType
WarningType.ShowWarning = False
import random
# 定义dataManage()用于处理初始数据
def dataManage(filepath,type):
    # 从爬虫获取的data.csv中读取'province','num'字段
    ProvinceInfo = pd.read_csv(filepath,usecols=['province','num'])
    # 定义直辖市字典
    city_direct = ['上海','北京','重庆','天津']
    # 初始化省份list,对应的数量list
    provinces = []
    nums = []
    # 定义num字典,其中old字段存储统一的数量累加,new字段存储当前城市的数量
    num = {'old':0,
           'new':0}

    # 遍历DataFrame的每行,对同一省份作累加
    for row in ProvinceInfo.iterrows():
        num['new'] = row[1]['num']
        if row[1]['province'] in provinces:
            num['old'] = num ['old']+ num['new']
        elif row[1]['province'] not in provinces:
            if row[1]['province'] == '上海':
                provinces.append(row[1]['province'])
                num['old'] = num['new']
            else:
                provinces.append(row[1]['province'])
                nums.append(num['old'])
                num['old'] = num['new']
    nums.append(num['old'])

    # 将获取到的省份和数量转换为DataFrame
    Infoes = { 'Province':provinces,'Num':nums}
    Infoes = pd.DataFrame(Infoes)

    # 将Infos写入到优衣库表格文件中
    #Infoes.to_csv('/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data_province.csv',
    #             sep=',',header=True,index=True)
    # 将Infos写入到zara表格文件中
    Infoes.to_csv('/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/'+type+'_data_province.csv',
                  sep=',', header=True, index=True)
    return Infoes

# 定义CreateMap()用于绘制地图
def CreateMap(data,type):
    # print(data)
    province = data['Province'].to_list()
    num_province = data['Num'].to_list()
    length = len(province)
    list_data = []
    for i in range(0,length):
        data = (province[i],num_province[i])
        # print(data)
        list_data.append(data)

    print(list_data)
    china_province = (
        Map()
            .add('', list_data, 'china')
            .set_global_opts(
            title_opts=opts.TitleOpts(title=type+'省级分布图'),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=70,
                is_piecewise=True)
        )
            .render(path='./htmls/'+type+'省级分布图.html')
    )

# 定义主函数main()
def main():
    # 分别定义路径
    # Uniqlo_filepath 为uniqlo_data存储路径,对应uniqlo的全国省,市数量信息
    uniqlo_filepath = '/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/uniqlo_data.csv'
    # Zara_filepath 为zara_data存储路径,对应uniqlo的全国省,市数量信息
    zara_filepath = '/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/zara_data.csv'
    # HM_filepath 为zara_data存储路径,对应uniqlo的全国省,市数量信息
    hm_filepath = '/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/hm_data.csv'

    # 依次调用dataManage(),获取数据
    # Uniqlo_data = dataManage(uniqlo_filepath,'uniqlo')
    # Zara_data = dataManage(zara_filepath,'zara')
    hm_data = dataManage(hm_filepath,'hm')
    # CreateMap(Uniqlo_data,'Uniqlo')
    # CreateMap(Zara_data,'Zara')
    CreateMap(hm_data,'hm')

main()
