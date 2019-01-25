from urllib import request,parse
from bs4 import BeautifulSoup
import openpyxl
url = 'http://test.39.net/test/96-6-110267.html'
l2=[]
for i in ['0','1']:
  for j in ['0','1']:
        for k in ['0','1']:
            for l in ['0','1']:
                for m in ['0','1']:
                    for n in ['0','1']:
                        l1 = i,j,k,l,m,n
                        l1 = list(l1)
                        l2.append(l1)

ll1=[]
for j in l2:
    ll = []
    str_ =','.join(j)
    try:

        headers = {
            'Referer':'http://test.39.net/test/96-5-110265.html',
            "Cookie":"Test_visit0=key:96&name:%25u9888%25u690E%25u75C5%25u81EA%25u6D4B%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520&url:http%3A//test.39.net/test/96.html; Hm_lvt_7f6196c0363432a65486ccaca2b517a6=1548225043; testtop=0; atesttop=0; btesttop=0; ctesttop=0; dtesttop=0; etesttop=0; ftesttop=0; gtesttop=0; fcspersistslider=2; examanswer_sel96={0}; Hm_lpvt_7f6196c0363432a65486ccaca2b517a6=1548233331".format(str_)

        }

        req = request.Request(url=url, headers=headers)

        rsp = request.urlopen(req)

        html = rsp.read()

        html = html.decode()
        soup = BeautifulSoup(html, 'lxml')

        divs = soup.find_all(class_='problem')
        dd = divs[0].get_text()
        dd = dd[:dd.find('。')]
        dd = dd.replace(' ','')

        print(str_, dd)


        ll.append(str_)
        ll.append(dd)
        ll1.append(ll)

        tq = openpyxl.Workbook()
        Sheet1 = tq.active
        Sheet1.title = "已爬取"
        for m in ll1:
            Sheet1.append(m)

        tq.save('C:/Users/meridian/Desktop/随机/已爬取.xlsx')



    except Exception as e:
        print(str_ + '有问题')














