from urllib import parse,request
from bs4 import BeautifulSoup
import openpyxl
l3 = []
def food(g,p):
    url = 'http://www.boohee.com/food/group/{0}?page={1}'.format(g,p)
    # for i in range(1,{0}).format(g):
        # print(i)



    rsp = request.urlopen(url = url)

    html = rsp.read()

    html = html.decode()

    # print(html)

    soup = BeautifulSoup(html,'lxml')
    divs1 = soup.find_all(class_='widget-food-list pull-right')

    # print(divs1[0].h3.get_text())
    divs = soup.find_all(class_='text-box pull-left')

    return divs,divs1
l2 = []
l4 = []

def w(d,d1):
    url = 'http://www.boohee.com'
    print(d1[0].h3.get_text())
    for j in d:
        l1 = []


        # print(j.a.get('title'))
        # print(j.a.get('href'))
        u1 =j.a.get('href')
        t1 = j.a.get('title')
        fullurl = url + u1

        # print(fullurl)
        rsp = request.urlopen(fullurl)

        html = rsp.read()

        html = html.decode()
        soup = BeautifulSoup(html,'lxml')

        divs = soup.find_all(class_='nutr-tag margin10')

        str_ = divs[0].get_text()
        str_ = str_.replace('\n', '^').replace('\n', '^')
        # print(str_)

        l1 = str_.split('^')
        l2 = [t1]
        for i in l1:
            if i != '':
                l2.append(i)
        l3 = []

        for m in l2:
            if '一' not in m and '详细' not in m:
                l3.append(m)
        # l3.append(j.value)
        # l4.append(dd)
        l4.append(l3)

    # print(l4)




    #
    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已爬取"
    # l5=list()
    # print("开始写入")
    # print(divs)

    #
    # l2.append(l1)
    # l3.append(l2)
    # print(l3)
    # print(len(l3))

    # 行数很少时可以使用
    # Sheet1.append(l4)

    for m in l4:
        Sheet1.append(m)

    tq.save('C:/Users/meridian/Desktop/随机/已爬取.xlsx')




    # for i in range(1,11):






if __name__ == '__main__':
   for i in range(1,3):
       for j in range(1,11):
           print('开始爬取第{0}组,第{1}页'.format(i,j))
           m,n = food(i,j)
           w(m,n)
           # w(food(i,j))

