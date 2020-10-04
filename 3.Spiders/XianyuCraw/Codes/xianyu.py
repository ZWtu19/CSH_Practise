# 爬虫标配第三方库
from __future__ import print_function
import requests
import urllib.parse
import json
import csv
import os
import codecs

# 在99api文档中复制的头文件信息
headers = {
"Accept-Encoding": "gzip",
"Connection": "close"
}


# 生成urls
# 定义函数生成url，并存储在列表urlsapi，函数将返回列表
def CreateUrls(item_id_path):
    # 初始url前缀
    urlApi = 'https://api03.6bqb.com/xianyu/detail?apikey=***********************' #修改路径

    # 调用urlComplete()
    urlsApi, itemNum = urlComplete(urlApi, item_id_path)

    # 返回完整的url列表和列表长度
    return urlsApi, itemNum


# 定义urlComplete函数
def urlComplete(urlApi, item_id_path):
    # 初始化urlapi存储完整url，初始化itemIds存储itemId，初始化itemNum存储url数量
    urlsApi = []
    itemIds = []
    itemNum = 0

    # 读取Ids_Path对应的csv文件，并添加至itemIds列表中
    idFiles = open(item_id_path)
    csv_reader_lines = csv.reader(idFiles)

    for one_line in csv_reader_lines:
        itemIds.append(one_line)  # 将读取的csv分行数据按行存入列表itemIds中
        itemNum = itemNum + 1  # 统计行数

    # 将urlApi和itemIds列表中的itemId遍历拼接，并添加至urlsApi中
    i = 1
    while i < itemNum:
        urlApi_new = urlApi + str(itemIds[i][1])
        urlsApi.append(urlApi_new)
        i = i + 1
    # print(urlsapi)

    # 返回完整的url列表和列表长度
    return urlsApi, itemNum

# 爬虫测试：获取数据->爬卖家信息和商品信息数据
# 定义数据获取函数
def crawl(url,headers):
    # 获取请求的data数据
    r = requests.get(url, headers=headers)
    result = r.json()
    #print(result)
    # 存储获取的卖家信息
    seller = result['data']['seller']
    print(seller)
    # 存储获取的商品信息
    item =  result['data']['item']
    print(item)
    # quantity = result['data']['quantity']
    # desc = result['data']['desc']
    return seller,item


# 爬虫测试：解析数据
# 定义数据解析函数
def GetData(url, savePath):
    # 获取原始信息：seller_old,item_old
    seller_old, item_old = crawl(url, headers)
    seller_new = {}
    item_new = {}
    # 定义解析后的信息：seller_new,item_new
    # 完善seller_new信息
    # 解析卖家自我介绍
    seller_new['Id'] = seller_old['sellerId']
    slSummary = seller_old['xianyuSummary']
    slSum = slSummary.split('。')
    seller_new['slTime'] = slSum[0].split(',')[0]
    seller_new['slSolds'] = slSum[0].split(',')[1]
    seller_new['slJob'] = slSummary.split('生。')[-1].split('。')[0]
    # 解析卖家其他信息
    seller_new['lastVisitTime'] = seller_old['lastVisitTime']
    seller_new['zhimaLevelInfo'] = {}
    seller_new['zhimaLevelInfo']['levelCode'] = seller_old['zhimaLevelInfo']['levelCode']
    seller_new['zhimaLevelInfo']['levelName'] = seller_old['zhimaLevelInfo']['levelName']
    seller_new['city'] = seller_old['city']
    # print(seller_new)

    # 对item商品信息进行解析和处理
    item_new['title'] = item_old['title']
    item_new['itemStatus'] = item_old['itemStatus']
    if item_new['itemStatus'] == '0':
        item_new['itemStatus'] = '在售'
    elif item_new['itemStatus'] == '1':
        item_new['itemStatus'] = '已售出'
    else:
        item_new['itemStatus'] = '未知'
    item_new['originalPrice'] = item_old['originalPrice']
    item_new['soldPrice'] = item_old['soldPrice']
    item_new['quantity'] = item_old['quantity']
    item_new['transportFee'] = item_old['transportFee']
    item_new['browseCnt'] = item_old['browseCnt']
    item_new['wantCnt'] = item_old['wantCnt']
    item_new['favorCnt'] = item_old['favorCnt']
    if 'tabData' not in item_old:
        item_new['tabData'] = '无同款商品信息'
    else:
        item_new['tabData'] = item_old['tabData']
    item_new['desc'] = item_old['desc']
    # print(item_new)

    # 存储完善后的信息
    storeData(seller_new, item_new, savePath)


# 爬虫测试：存储数据
# 定义数据存储函数
def storeData(seller, item, filePath):
    # 定义字典作为存储字段
    field = ['卖家Id', '卖家入驻闲鱼时长', '卖家卖出商品数量', '卖家职业', '卖家访问闲鱼频率', '卖家芝麻评级', '卖家芝麻信用', '卖家发货地址',
             '商品标题', '商品状态', '商品划线价格', '商品售价', '商品数量', '商品邮费', '商品浏览数', '商品想要人数', '商品点赞数', '商品同款信息', '商品描述']

    # 将传送的参数赋值
    # 卖家信息
    slId = seller['Id']
    slTime = seller['slTime']
    slSolds = seller['slSolds']
    slJob = seller['slJob']
    slFrq = seller['lastVisitTime']
    slZmLv = seller['zhimaLevelInfo']['levelCode']
    slZmName = seller['zhimaLevelInfo']['levelName']
    slAdr = seller['city']

    # 商品信息
    itmTit = item['title']
    itmStatus = item['itemStatus']
    itmOriPrice = item['originalPrice']
    itmPrice = item['soldPrice']
    itmNum = item['quantity']
    itmTrFee = item['transportFee']
    itmBrowse = item['browseCnt']
    itmWant = item['wantCnt']
    itmFavor = item['favorCnt']
    itmSimilar = item['tabData']
    itmDesc = item['desc']

    # 数据写入
    l = []
    with  open(filePath, 'a') as csvFile:
        writer = csv.writer(csvFile)
        # writer.writerow(field)
        # 将数据写入
        # 添加卖家数据
        l.append(slId)
        l.append(slTime)
        l.append(slSolds)
        l.append(slJob)
        l.append(slFrq)
        l.append(slZmLv)
        l.append(slZmName)
        l.append(slAdr)

        # 添加商品数据
        l.append(itmTit)
        l.append(itmStatus)
        l.append(itmOriPrice)
        l.append(itmPrice)
        l.append(itmNum)
        l.append(itmTrFee)
        l.append(itmBrowse)
        l.append(itmWant)
        l.append(itmFavor)
        l.append(itmSimilar)
        l.append(itmDesc)

        # 数据写入csv文件
        writer.writerow(l)
    print('id为%s的商品信息存储完成' %slId)


def main():
    # 定义type列表用于确定获取数据类型
    # item_type = ['men', 'women', 'kids', 'sports','sold']
    item_type = ['sold']
    # 定义idPath字典用于确定不同数据类型的存储位置
    item_id_path = {
        'men': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/itemIds/itemId_men.csv',
        'women': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/itemIds/itemId_women.csv',
        'kids': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/itemIds/itemId_kids.csv',
        'sports': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/itemIds/itemId_sports.csv',
        'sold': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/itemIds/itemId_sold.csv'
    }
    # 定义itemPath字典用于确定不同数据类型的存储位置
    item_data_path = {
        'men': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/ClothData/item_men.csv',
        'women': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/ClothData/item_women.csv',
        'kids': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/ClothData/item_kids.csv',
        'sports': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/ClothData/item_sports.csv',
        'sold': '/Users/authorcai/Documents/Authorcai/CSH/Spider/Csvs/ClothData/item_sold.csv'
    }

    # 遍历爬取item_type中不同type（类型）的数据
    for type in item_type:
        # 通过CreateUrls()，得到urls，包含完整的url列表
        urls, urlsNum = CreateUrls(item_id_path[type])
        # 对urls进行遍历，对每个url执行getData()
        i = 1
        while i < urlsNum:
            # print(urls[i-1])
            try:
                GetData(urls[i-1],item_data_path[type])
                i = i + 1
            except:
                i = i + 1
                continue

# 调用主函数
main()

