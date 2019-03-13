import requests
from bs4 import BeautifulSoup
from urllib import parse
import bs4
import re
import openpyxl
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return " "
def main():
    depth = 10
    ss = input('请输入查询关键词')
    qs = {
        "query": ss
    }

    qs = parse.urlencode(qs)
    print(qs)
    url = 'http://www.chunyuyisheng.com/pc/search/qalist/?'
    start_url = url + qs
    # start_url = 'http://www.chunyuyisheng.com/pc/search/qalist/?query=%E6%8A%91%E9%83%81 '
    infoList = []
    re_wen = re.compile(r'(?<=<i class="ask-tag">)[\s\S]*?(?=</a>)')
    re_da = re.compile(r'(?<=<div class="qa-item qa-item-answer">)[\s\S]*?(?=</div>)')

    l2 = []
    for i in range(1, depth):
        # l2 = []
        url = start_url + '&page=' + str(i)
        html = getHTMLText(url)
        result_a=re_wen.findall(html)
        result_b=re_da.findall(html)
        for i in range (len(result_a)):
            result_a[i]=result_a[i].replace(" ","").replace(r"</i>",':').replace("\n",'').replace("\t",'')
        for i in range(len(result_b)):
            result_b[i] = result_b[i].replace('<i class="ask-tag answer-tag">', "--").replace("<span class='s-hl'>", '').replace("</span>", "").replace("\t", '').replace(" ","\n")
        l1 = []

        for i in range(len(result_b)):
            print('---------------------------------')
            print(str(i) + ":" + result_a[i] + result_b[i])
            l1.append(result_a[i])
            l1.append(result_b[i])
        l2.append(l1)

    tq = openpyxl.Workbook()
    Sheet1 = tq.active
    Sheet1.title = "已提取"

    for i in l2:
        Sheet1.append(i)

    tq.save('C:/Users/meridian/Desktop/提取练习/已处理.xlsx')
            # print(str(i)+":"+result_a[i]+result_b[i])
main()
