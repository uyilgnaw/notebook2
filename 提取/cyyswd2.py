import openpyxl
from bs4 import BeautifulSoup
from urllib import request,parse
import time
import random
def question_start(m):

    url = 'https://www.chunyuyisheng.com/pc/qalist/?high_quality=1&page={0}'.format(m)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }
    req = request.Request(url = url,headers = headers)
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
    l2 = []

    for m in range(1,31):
        try:
            d = question_start(m)
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
                print(divs[0].h1.get_text())
                print(divs2[0].p.get_text())

                t = 2 + random.random()
                print("休息{0}秒钟".format(t))
                time.sleep(t)
                l1.append(divs[0].h1.get_text())
                l1.append(divs2[0].p.get_text())
                l2.append(l1)
        except Exception as e:
            print(e)

    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已提取"

    print("开始写入")

    for i in l2:

        Sheet1.append(i)
    print("写入完成")
    tq.save('C:/Users/meridian/Desktop/提取练习/已处理.xlsx')

# def main():
#     chuli(question_start())



if __name__ == '__main__':
    chuli()