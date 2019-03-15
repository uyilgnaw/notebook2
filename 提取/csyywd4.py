from urllib import request,parse
from bs4 import BeautifulSoup
import time
import random
import openpyxl
from openpyxl.styles import colors
from openpyxl.styles import Font,Color
import sys


def keshi_all1():
    url = 'https://www.chunyuyisheng.com/pc/qalist/?high_quality=1'

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    lis1 = soup.find(class_='first-clinic')

    li1 =lis1.find_all(class_= 'tab-item')

    return li1

def keshi_all2():

    l1 = keshi_all1()
    l2 = []
    for i in l1:
        url = 'http://www.chunyuyisheng.com'
        if i.a.get_text().replace("\n", "").replace("\t", "").replace(" ", "") != '全部科室':
            i = i.a.get('href')
            url = url + i
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

            }
            req = request.Request(url=url, headers=headers)
            rsp = request.urlopen(req)
            html = rsp.read()

            html = html.decode()
            soup = BeautifulSoup(html,"lxml")
            lis2 = soup.find(class_=('sider-wrap dropdown-wrap'))
            li2 = lis2.find_all(class_= 'tab-item ')
            l2.append(li2)
    return l2
def keshi_allurl():
    url = 'https://www.chunyuyisheng.com'
    l1 = []

    l11 = keshi_all1()
    l22 = keshi_all2()
    for i in l11:
        if i.a.get_text().replace("\n","").replace("\t","").replace(" ","") != '全部科室':
            u1 = i.a.get('href')

            fullurl1 = url + u1
            # print(fullurl1)
            l1.append(fullurl1)

    for j in l22:
        for m in j:
            u2 = m.a.get('href')
            fullurl2 = url + u2
            # print(fullurl2)
            l1.append(fullurl2)


    return l1


def jb_allurl():
    u = 'https://www.chunyuyisheng.com'
    l1 = keshi_allurl()
    l2 = []
    for url in l1:
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

        }
        proxy = {'http': '110.52.235.74'}
        # 2.创建ProxyHandler
        proxy_handler = request.ProxyHandler(proxy)
        # 3.创建Opener
        opener = request.build_opener(proxy_handler)
        # 4.安装Opener
        request.install_opener(opener)
        req = request.Request(url=url, headers=headers)
        rsp = request.urlopen(req)

        html = rsp.read()

        html = html.decode()
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.find(class_='tab-type-one disease-list')
        li = lis.find_all(class_='tab-item')
        for l in li:
            ll = l.a.get('href')
            t1 = l.a.get_text()

            qs = {
                'query_str': t1
            }
            t1 = 'query_str=' + t1
            qs = parse.urlencode(qs)
            ll = ll.replace(t1, qs)
            fullurl = u + ll
            l2.append(fullurl)
            print(fullurl,t1)
            time.sleep(0.1+random.random() )

    return l2
    #l2返回的是所有第一页的疾病url
def fenye(i):
    url = i
    url_base = 'http://www.chunyuyisheng.com'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }
    proxy = {'http': '110.52.235.74'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    lis1 = soup.find(class_='pagebar')
    mm = lis1.find_all(class_='next')

    uu = url_base + mm[0].get('href')

    return uu

def keshi(q):
        try:
            url = q
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

            }
            proxy = {'http': '110.52.235.74'}
            # 2.创建ProxyHandler
            proxy_handler = request.ProxyHandler(proxy)
            # 3.创建Opener
            opener = request.build_opener(proxy_handler)
            # 4.安装Opener
            request.install_opener(opener)
            #
            req = request.Request(url=url, headers=headers)
            rsp = request.urlopen(req)
            html = rsp.read()

            html = html.decode()

            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all(class_='qa-item qa-item-ask')
            # print(divs[0].a.get('href'))
            # print(divs[1].a.get('href'))
            return divs
        except Exception as e:
            print(e)


def main():
    url = 'https://www.chunyuyisheng.com'
    l_suoyou = jb_allurl()# 所有的url

    l3 = []
    for q in l_suoyou:
        div_s = keshi(q)  # q是单个第一页url
        count = 0
        fy = q
        while (count <= 30):
            try:
                    for dd in div_s:# div_s是第一页的所有10个问题,dd 为单个问题

                        l1 = []
                        u1 = dd.a.get('href')
                        i = url + u1# i为单个问题的url

                        headers = {
                            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
                        }
                        proxy = {'http': '110.52.235.74'}
                        # 2.创建ProxyHandler
                        proxy_handler = request.ProxyHandler(proxy)
                        # 3.创建Opener
                        opener = request.build_opener(proxy_handler)
                        # 4.安装Opener
                        request.install_opener(opener)
                        #
                        req = request.Request(url=i, headers=headers)
                        rsp = request.urlopen(req)
                        html = rsp.read()
                        html = html.decode()
                        # print(html)
                        soup = BeautifulSoup(html, 'lxml')
                        divs = soup.find_all(class_="content-top")
                        divs2 = soup.find_all(class_='block-right')
                        # print(divs2)
                        d1 = divs[0].h1.get_text()
                        print(d1)
                        l1.append(d1)
                        l2 = []
                        for result_hd in divs2:
                            d2 = result_hd.p.get_text()
                            d3 = result_hd.h6.get_text()
                            d2 = d3 + ":" + d2.replace("\n", '').replace("\t", '').replace(" ", '')
                            l2.append(d2)
                        l1.append("\n".join(l2))
                        l3.append(l1)
                        t = 1 + random.random()
                        time.sleep(t)
                        print("休息{0}秒".format(t))
                    fy = fenye(fy)
                    if fy == None:
                        break
                    else:
                        div_s = keshi(fy)

                        count = count + 1

            except Exception as e:
                print(e)
                count = count+1
    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已爬取"
    Sheet1['A1'] = '标准问题'
    Sheet1['B1'] = '详细问答'
    a1 = Sheet1['A1']
    b1 = Sheet1['B1']
    ft = Font(color=colors.RED, bold=True)
    a1.font = ft
    b1.font = ft

    print("开始写入")

    for i in l3:
        Sheet1.append(i)
    print("写入完成")
    tq.save('C:/Users/meridian/Desktop/提取练习/已处理.xlsx')


#
#










if __name__ == '__main__':
    main()


