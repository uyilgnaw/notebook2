from urllib import parse,request
import openpyxl
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.boohee.com/food/search?keyword='
    # wd = input("请输入想查询的食物")
    t1 = openpyxl.load_workbook(filename="C:/Users/meridian/Desktop/随机/每日食谱数据营养素表.xlsx")
    e1 = t1.active
    l4 = []
    for j in e1['A']:

        qs = {
            "wd":j.value
        }

        qs = parse.urlencode(qs)

        fullurl = url + qs

        rsp = request.urlopen(fullurl)

        html = rsp.read()
        html = html.decode()
        soup = BeautifulSoup(html,'lxml')

        divs = soup.find_all(class_='text-box pull-left')
        try:


            u1 = divs[0].a.get('href')
            t1 = divs[0].a.get('title')
            url2 ='http://www.boohee.com'
            fullurl2 = url2 + u1
            # print(fullurl2)
            rsp1 = request.urlopen(fullurl2)

            html2 = rsp1.read()
            html2 = html2.decode()

            soup2 = BeautifulSoup(html2,'lxml')

            soup2.select('nutr-tag margin10 span')
            divs2 = soup2.find_all(class_='nutr-tag margin10')
            str_ = divs2[0].get_text()
            # print(type(str_))
            str_ = str_.replace('\n','^').replace('\n','^')
            # print(str_)
            # l1 = str_.splitlines()
            # print(str_)
            # for i in l1:
            #     if i == '' or i == '':
            #         l1.remove(i)
            # print(l1)


            l1 = str_.split('^')
            l2= [j.value]
            for i in l1:
                if i != '' :
                  l2.append(i)
            l3 =[]

            for m in l2:
                if '一' not in m and '详细' not in m:
                    l3.append(m)
            # l3.append(j.value)

            print(l3,t1)
            print('===================================')

            l4.append(l3)
        except Exception as e:
            print(j.value,'手动查')


            # 开始写入

    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已提取"
    # l5=list()
    print("开始写入")

            # 行数很少时可以使用
            # Sheet1.append(l4)



    for i in l4:
        Sheet1.append(i)




    tq.save('C:/Users/meridian/Desktop/随机/已处理.xlsx')



