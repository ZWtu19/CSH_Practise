import random
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
from pyecharts.globals import WarningType
WarningType.ShowWarning = False

def dataManage(filepath,type):
    # 从爬虫获取的data.csv中读取'province','num'字段
    CityInfo = pd.read_csv(filepath, usecols=['city', 'num'])
    all_city = []
    nums = []
    # 定义num字典,其中old字段存储统一的数量累加,new字段存储当前城市的数量
    num = 0

    # 遍历DataFrame的每行,统计城市的num
    for row in CityInfo.iterrows():
        num = row[1]['num']
        all_city.append(row[1]['city'])
        nums.append(num)

    # 将获取到的省份和数量转换为DataFrame
    Infoes = {'Cities': all_city, 'Num': nums}
    Infoes = pd.DataFrame(Infoes)

    # 将Infos写入到表格文件中
    Infoes.to_csv('/Users/authorcai/Documents/Authorcai/CSH/Spider/BaiduMap_Spider/data/'+type+'_data_cities.csv',
                  sep=',', header=True, index=True)
    return Infoes

def CreateMap(data,type):
    # print(data)
    cities = data['Cities'].to_list()
    num_province = data['Num'].to_list()
    length = len(cities)
    list_data = []
    for i in range(0,length):
        data = (cities[i],num_province[i])
        # print(data)
        list_data.append(data)

    print(list_data)
    china_city = (
        Map()
        .add(
            "",
            list_data,
            "china-cities",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=type+'地级市分布图'),
            visualmap_opts=opts.VisualMapOpts(
                min_=0,
                max_=20,
                is_piecewise=True
            ),
        )
            .render(path='./htmls/'+type+'地级市分布图.html')
    )

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
    CreateMap(hm_data, 'hm')
main()