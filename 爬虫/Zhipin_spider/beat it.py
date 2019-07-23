import openpyxl
from bs4 import BeautifulSoup
from urllib import request
import time
import random
from multiprocessing import Process
import os




def get():
    url = 'http://www.vfast.com.cn/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }

    req = random_Ip().Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()

    print("访问了1次")

def random_Ip():
    proxy = Ip_pool()
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    return request
def Ip_pool():
    proxy = {
        '0': {'http': '60.217.154.243'},
        '1': {'http': '112.14.47.6'},
        '2': {'http': '103.207.167.12'},
        '3': {'http': '27.188.64.70'},
        '4': {'http': '120.210.219.104'}
    }
    rad = random.randint(0, 4)
    # print('Ip地址为{0}'.format(proxy[str(rad)]))
    return proxy[str(rad)]

if __name__ == '__main__':


    pass
    # while 1:
    #     try:
    #
    #     except Exception as e:
    #         print("再来一次")
