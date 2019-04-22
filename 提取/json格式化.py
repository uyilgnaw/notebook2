# -*- coding:utf-8 -*-
import json
import random
import openpyxl
import os
def load_data():
    l1 = []
    rootdir = "C:/Users/meridian/Desktop/json报告"
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        l1.append(path)
    return  l1

def handle_data():
    k = 1
    all_data = load_data()
    for i in all_data:

        f = open(i,encoding='utf-8')
        print("读取",i)
        setting = json.load(f)
        chuli(setting,k)
        k = k+1
        # print(type(setting))

def chuli(s,k):
    setting = s

    ss = setting["Items"]
    l4 = []
    for j in ss:
        l3 = []
        # print(j["Category"] + "_" + j["Name"])
        keys = j["Category"] + "_" + j["Name"]
        values = j["Result"]
        # print(j["Result"])
        l3.append(keys)
        l3.append(values)
        l4.append(l3)

    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已提取"

    for i in l4:
        Sheet1.append(i)

    tq.save('C:/Users/meridian/Desktop/提取练习/已处理{0}.xlsx'.format(k))




if __name__ == '__main__':
    handle_data()