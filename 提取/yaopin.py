from urllib import parse,request
import openpyxl
from bs4 import BeautifulSoup
import time
import random
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
        '0':{'http':'183.146.213.198'},
        '1':{'http':'212.64.51.13'},
        '2':{'http':'39.137.69.10'},
        '3':{'http':'39.137.69.7'},
        '4':{'http':'118.26.170.209'}
    }
    rad = random.randint(0,4)
    # print('Ip地址为{0}'.format(proxy[str(rad)]))
    return  proxy[str(rad)]
def Analysis_Web(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        # "Cookie":"__auc=3ff488b116b02d00faf8115ed70; DXY_USER_GROUP=36; _da_sid=C1A1BA939779D3227A9B7B5E511D4C581559120318238; __utma=1.1302554949.1559120319.1559120319.1559120319.1; __utmz=1.1559120319.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1559120319; _ga=GA1.2.1302554949.1559120319; _gid=GA1.2.595304980.1563327621; route=39787fe2b5295772f852a2edb6841363; _da_uid=baa13d1955b6716835c88ccc329e649b0ea55a33f3bcf0099b66969eddf29ed4af68366ae3a9a997; JUTE_BBS_DATA=72fe69071c98842538792254ed88495c398d5ea29c1b518e68ff0796dac3d27e8bebd2dac33be0bff6b4c72358134af2244bfce02f5afa46bfe48f193f1d53d80a0dcaaff7259c0166c2b6fb009ae59a5a2e95fa3a53ea2e7fed53f41f7141a215aba6e181fa7c2d3494180c0e4b3c58; DRUGSSESSIONID=A3796C3C5F3DCDFE132F19D7BC1D5357-n2; __asc=a8cb633516bfdbe8a23f754cdfe; _da_pid=02e00004acb17a491b8f72b8a3cb00962e30bb741e475d551413500429dccdc8695ee1168cb4eaa58fcc70c306187ccb6d4f0247ba8b8a80b11ec27770b38caa1b83066e8183cdc90222602ce7f5b4f632a7017062b9081833a89af2d830353e9e2563dd4399ccba"
    }
    req = request.Request(url=url,headers = headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    return soup

def Drugs_classification():
    url = 'http://drugs.dxy.cn/'
    soup  = Analysis_Web(url)
    lis1 = soup.find_all('h3')

    fenlei = []
    for i in lis1:
        print(i.a.get('href'))
        fenlei.append(i.a.get('href'))
    return fenlei

def Secondary_classification():
    url = 'http:'
    drugs_classlist = Drugs_classification()
    # print(drugs_classlist)
    Secondary_fenlei = []
    for i in drugs_classlist:
        soup = Analysis_Web(url + i)
        lis1 = soup.find(class_='list')
        lis2 = lis1.find_all('h3')

        for j in lis2:
            # print(j.a.get('href'))
            # print('-----------')
            Secondary_fenlei.append(j.a.get('href'))
    # print(len(Secondary_fenlei))
    return Secondary_fenlei

# def Third_classification():
#     drugs_name = []
#     url = 'http:'
#     Second_classlist = Secondary_classification()
#     for i in Second_classlist:
#         soup = Analysis_Web(url + i)
#         lis1 = soup.find_all('section')
#         # print('爬取了{0}'.format(i))
#         # time.sleep(random.random() * 1)
#         for j in lis1:
#             print(j.a.get('href'))
#             drugs_name.append(j.a.get('href'))
#
#     return drugs_name

def drugs_details():
    drugs_type = []
    url = 'http:'
    drugs_list = Secondary_classification()
    print(drugs_list)
    for i in drugs_list:
        # drugs_type = []
        print("爬取了{0}".format(i))
        time.sleep(2)
        soup = Analysis_Web(url + i)
        print(soup)
        lis1 = soup.find(class_='m49 detail detail1')
        print(lis1)
        lis2 = lis1.find_all('dd')
        drugs = []
        for i in lis2:
            # print(i)

            ii = i.get_text()

            ii = ii.replace('\t', "").replace(' ', "")
            if '请登录' not in ii:
                drugs.append(ii)
        drugs_type.append(drugs)
        # drugs_all.append(drugs_type)

    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已提取"
    for m in drugs_type:

        Sheet1.append(m)
    # for j in drugs:
    #     Sheet1.append(j)

    tq.save('C:/Users/meridian/Desktop/已爬取/已爬取.xlsx')


if __name__ == '__main__':
    drugs_details()
    # Drugs_classification()
    # Secondary_classification()