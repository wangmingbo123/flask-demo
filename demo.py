#!/usr/bin/python3
import urllib
import json


def getExpressInfo(num):
    # get请求
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?text=' + num  # get请求通过url传值
    basicInfo = urllib.request.urlopen(url, data=None, timeout=10)  # python3应该可以通过检测data是否携带参数来判断是get请求还是post请求
    data = json.loads(basicInfo.read().decode())  # 解析返回对象获取

    comInfo = data['auto'][0]['comCode']  # 获取快递公司信息

    # 通过公司名称和快递单号请求快速100的API
    url2 = 'http://api.kuaidi100.com/api?id=be2205c7c55b54eb&com=' + comInfo + '&nu=' + num
    result = urllib.request.urlopen(url2, data=None, timeout=10)
    expressInfo = result.read().decode()

    print(expressInfo)
    # 返回快递信息
    return (expressInfo)


num = '280688688407'  # 快递单号

# 调用快递信息方法
getExpressInfo(num)
