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

    divs = soup.find_all(class_='text-box pull-left')

    return divs
l2 = []

def w(d):

    for j in d:
        l1 = []
        # print(j.a.get('title'))
        # print(j.p.get_text())
        l1.append(j.a.get('title'))
        l1.append(j.p.get_text())
        l2.append(l1)



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

    for m in l2:
        Sheet1.append(m)

    tq.save('C:/Users/meridian/Desktop/随机/已爬取.xlsx')
    # # return i



    # for i in range(1,11):





if __name__ == '__main__':
   for i in range(1,12):
       for j in range(1,11):
           print('开始爬取第{0}组,第{1}页'.format(i,j))

           w(food(i,j))

