import openpyxl
from bs4 import BeautifulSoup
from urllib import request
import time
import random
from openpyxl.styles import colors
from openpyxl.styles import Font,Color


def keshi(m):
    url = 'https://www.chunyuyisheng.com/pc/qalist/?high_quality=1&page={0}'.format(m)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()

    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all(class_='qa-item qa-item-ask')
    # print(divs[0].a.get('href'))
    # print(divs[1].a.get('href'))
    return divs

def chuli():
    url = 'https://www.chunyuyisheng.com'
    l3 = []
    for m in range(1,31):

        try:
            d = keshi(m)
            for i in d:
                l1 = []
                u1 = i.a.get('href')
                fullurl = url + u1
                # print(fullurl)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

                }
                req = request.Request(url=fullurl, headers=headers)
                rsp = request.urlopen(req)


                html = rsp.read()

                html = html.decode()
                # print(html)
                soup = BeautifulSoup(html, 'lxml')

                divs = soup.find_all(class_="content-top")
                divs2 = soup.find_all(class_='block-right')
                # print(divs2)
                d1 = divs[0].h1.get_text()
                # print(d1)
                l1.append(d1)
                l2 = []
                for result_hd in divs2:
                    d2 = result_hd.p.get_text()
                    d3 = result_hd.h6.get_text()
                    d2 = d3 + ":" + d2.replace("\n",'').replace("\t",'').replace(" ",'')
                    # print(d2)
                    # print("----------------------")

                    l2.append(d2)
                    # l2.append(d3)
                l1.append("\n".join(l2))
                l3.append(l1)
                t = 1 + random.random()
                time.sleep(t)
                print("休息{0}秒".format(t))


        except Exception as e:
            print(e)
    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已爬取"
    Sheet1['A1'] = '标准问题'
    Sheet1['B1'] = '详细问答'
    a1 = Sheet1['A1']
    b1 = Sheet1['B1']
    ft = Font(color = colors.RED,bold = True)
    a1.font = ft
    b1.font = ft

    print("开始写入")

    for i in l3:
        Sheet1.append(i)
    print("写入完成")
    tq.save('C:/Users/meridian/Desktop/提取练习/全部科室.xlsx')

if __name__ == '__main__':
    chuli()








