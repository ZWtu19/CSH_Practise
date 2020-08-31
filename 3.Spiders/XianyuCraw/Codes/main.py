import random
import numpy as np
import pandas as pd
import csv
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# from pyecharts.charts import Map  # 注意这里与老版本pyecharts调用的区别
# from pyecharts.globals import WarningType


# 定义所用的特征信息内容
def DefinationFeatures():
    # 通过Features字典存储特征信息
    Features = {}
    # 列表用于存放商品的其他特征信息
    Features['season'] = ['春', '夏', '秋', '冬', '其他']
    Features['size_1'] = ['s', 'm', 'l', 'xl', 'xxl', '其他']
    Features['size_2'] = ['160', '165', '170', '175', '180', '其他']
    Features['stands'] = ['adidas', '阿迪达斯', '耐克', '贵人鸟', '南极人', '优衣库', 'zara', '其他']
    Features['styles'] = ['学生', '港风', '英伦', '潮牌', '宽松', '修身', 'polo', '其他']
    Features['type'] = ['短袖', '长袖', '上衣', '裤', '裙', '卫衣', '其他']
    Features['material'] = ['纯棉', '涤纶', '']

    # 返回Features
    return Features

# 定义对数据的处理函数
def Assignment(row):
    # 输出原文本内容
    description = row['description']
    # print('原文本内容：%s' %description)
    # 调用函数深度解析数据Analyze
    results = parse(description)
    # 暂存数据
    features = {}
    features['item_id'] = results['item_id']
    features['season'] = results['season']
    features['size_1'] = results['size_1']
    features['size_2'] = results['size_2']
    features['stands'] = results['stands']
    features['styles'] = results['styles']
    features['type'] = results['type']
    features['material'] = results['material']
    # print(features)
    # 返回数据
    return features

# 定义数据读取函数
def readInformation(type):
    all_data = []
    # types = ['men','women','kids','sports']
    # types = ['men']

    data_old = pd.read_csv('/home/authorcai/PycharmProjects/XianyuCraw/Csvs/原始数据/item_'+type+'.csv')
    data = pd.DataFrame()
    data['item_id'] = data_old['卖家Id']
    data['description'] = data_old['商品描述']
    all_data.append(data)
    return all_data


# 定义数据存储函数
def storeData(filePath,features):
    # 数据写入
    l = []
    with  open(filePath, 'a') as csvFile:
        writer = csv.writer(csvFile)
        # writer.writerow(field)
        # 将数据写入
        # 添加数据
        l.append(features['item_id'])
        l.append(features['season'])
        l.append(features['size_1'])
        l.append(features['size_2'])
        l.append(features['stands'])
        l.append(features['styles'])
        l.append(features['type'])
        l.append(features['material'])
        # 数据写入csv文件
        writer.writerow(l)

def parse(description):
    # 将文本内容description的内容解析后存储在content中
    results = {
        'item_id':[],
        'season':[],
        'size_1':[],
        'size_2':[],
        'styles':[],
        'stands':[],
        'type':[],
        'material':[]
    }
    Features = {}
    Features['season'] = ['春','夏','秋','冬']
    Features['size_1'] = ['XXXXXL','5XL','XXXXL','4XL','XXXL','3XL','XXL','2XL','XL','L','M','S']
    Features['size_2'] = ['160','165','170','175','180']
    Features['stands'] = ['adidas','阿迪达斯','阿迪','耐克','Nike','nike','贵人鸟','南极人','优衣库','zara','优衣库','uniqlo','老虎头','富贵鸟','']
#     Features['size_1'] = ['s','m','l','xl','xxl'] 尺码应当忽略大小写,注意xl，2xl，3xl，4xl的写法
#     Features['size_2'] = ['160','165','170','175','180']
#     Features['stands'] = ['adidas','阿迪达斯','耐克','贵人鸟','南极人','优衣库','zara','优衣库','uniqlo'] 牌子应该包括中英文
    Features['styles'] = ['学生','港风','英伦','潮牌','宽松','修身','polo','圆领','v领','V领']
    Features['type'] = ['短袖','长袖','上衣','裤','裙','卫衣','衬衫','家居服','基础款']
    Features['material'] = ['纯棉','涤纶']
    for feature in Features:
        for f in Features[feature]:
            length = len(f)
            # 定位关键字的位置
            pos = description.find(f)
            # 判定该关键字是否存在
            result = description[pos:pos+length]
            if(pos!=-1):
                results[feature].append(f)
            else:
                
    print(results)
    return results


# 定义主函数
if __name__ == '__main__':
    types = ['men', 'women', 'kids', 'sports']
    for type in types:
        contents = DefinationFeatures()
        dataes = readInformation(type)
        for data in dataes:
            for index, row in data.iterrows():
                features = Assignment(row)
                storeData('/home/authorcai/PycharmProjects/XianyuCraw/Csvs/解析后的数据/result_' + type + '.csv', features)