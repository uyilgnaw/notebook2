# -!- coding: utf-8 -!-
import sys
import requests

import importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf8')
from urllib import parse,request
import openpyxl
from bs4 import BeautifulSoup
import time
import random
import json
def Analysis_Web(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Cookie": "Hm_lvt_b1ccef85a3456b5f14347f4d25b82c86=1563328190,1563328356,1563347172,1563354684; Hm_lpvt_b1ccef85a3456b5f14347f4d25b82c86=1563357327"
        }

        req = request.Request(url=url, headers=headers)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        return html
    except Exception as e:
        print("{0}出现了异常".format(url))
        return 0


def get_id(drugs_name):

    data = {
                'tag':drugs_name
        }
    data = parse.urlencode(data)
    url = 'http://39.105.161.146:9999/api/searchByTag?{0}&type=medical&pageSize=5000'.format(data)
    # print(url)

    # print(html)
    html = Analysis_Web(url)
    html_dict = json.loads(html)
    XinNao = {}
    for i in html_dict['list']:
        XinNao[i['id']] = i['name']
    return XinNao
def fanyi(drugs):
    url = "https://fanyi.baidu.com/sug"
    # 定义请求的参数
    data = {'kw': drugs}
    # 创建请求， 发送请求， 爬取信息
    res = requests.post(url, data=data)
    # 解析结果
    str_json = res.content.decode("utf-8")
    # print(type(str_json))
    myjson = json.loads(str_json)
    # print(type(myjson))
    # print(myjson)
    value = myjson['data'][0]['v']
    print(value[3:value.find(';')])
    return value[3:value.find(';')]

def Translate(key):
    kk = []
    for i in key:

        i = fanyi(i)
        time.sleep(2 + random.randint(0,1))
        kk.append(i)
    return kk


def get_drugs(drugs_name):
    drugs_id = get_id(drugs_name)
    hh = []
    url = 'http://39.105.161.146:9999/api/medical/'
    for i in drugs_id.keys():
        time.sleep(2 + random.randint(0,1))
        # global html_dict
        html = Analysis_Web(url + str(i) )
        if html == 0:
            print("继续下一个")
            continue
        html_dict = json.loads(html)
        # global keys
        # keys = html_dict['medical'].keys()
        # keys = Translate(keys)
        if '查询资源不存在' in html :
            # print(html)
            print("查询资源不存在")

            time.sleep(3+ random.randint(0,1))

        else:

            # values = html_dict['medical'].values()
            print("爬取了{0}".format(html_dict['medical']['id']))
            # global keys
            # keys = html_dict['medical'].keys()
            # keys = Translate(list(keys))
            values = html_dict['medical'].values()
            # hh.append(list(keys))
            hh.append(list(values))
    # keys = html_dict['medical'].keys()
    return hh
def save(drugs_name):
    hh= get_drugs(drugs_name)
    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已提取"
    # Sheet1.append(list(keys))
    for m in hh:
        try:
            Sheet1.append(m)
        except Exception as e:
            print('写入异常')
            continue
    tq.save('C:/Users/meridian/Desktop/已爬取/{0}.xlsx'.format(drugs_name))
    print("{0}已保存".format(drugs_name))
if __name__ == '__main__':
    ll = ['血液系统用药','抗肿瘤药','消化系统用药','呼吸系统用药',
          '心脑血管用药','皮肤科用药','镇痛、解热、抗炎、抗风湿、抗痛风药','抗微生物药',
          '抗寄生虫病药','抗过敏药（抗变态反应药）','眼科用药','耳鼻喉科用药']
    for i in ll:

        save(i)
        time.sleep(2 + random.randint(0,1))



