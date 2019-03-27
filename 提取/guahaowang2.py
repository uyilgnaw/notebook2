from urllib import request,parse
import time
import random
import json
from bs4 import BeautifulSoup
import openpyxl


def time_stamp():
    t = time.time()
    t = int(round(t*1000))
    return t    # 返回系统时间戳

def Page(m,n):

    url = 'https://bbs.guahao.com/gateway/modulesns/mutualhelp/homepagewaterfall.json'

    data = {
        'firstTime': '{0}'.format(time_stamp()),
        'pageNo': '{0}'.format(m),
        'pageSize': '20',
        'sortMethod': '0',
        'tagGroupId': "{0}".format(n),
        'type':'0'
}
    data = json.dumps(data)
    data = data.encode()

    headers = {

        'user-agent':'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36',
        'content-length': len(data),
        'weiyi-appid':'p_web_weiyi',
        'content-type':'application/json'


    }
    try:
        req = random_Ip().Request(url=url,data = data,headers = headers)
        rsp = request.urlopen(req)
        json_data = rsp.read().decode()

        json_data = json.loads(json_data)

        # print(json_data)
        return json_data # 返回该页数转化为字典后的数据
    except Exception as e:
        print(e)

def collect_allid():
    url = 'https://bbs.guahao.com/help'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all(class_='J_Tag')
    divs1 = soup.find_all(class_='J_Tag_Inmore')
    d1 = {}
    for i in divs:

        id = i.get('data-id')
        name = i.get_text()
        d1[id]=name
    for j in divs1:

        id_more = j.get('data-id')
        name_more = j.get_text()
        d1[id_more] = name_more


    # print(d1)
    return d1



def extract():
    d1 = collect_allid()
    d2 = {}

    n = d1.keys()
    for k in n:
        l2 = []
        for m in range(1,51):

            try:
                Items = Page(m, k)['items']
                for i in Items:
                    l1 = []
                    # print(chuli(1))
                    # print("问题id:",i['questionId'])
                    # print("问题描述:",i['questionDesc'])
                    # print("回答问题人数,",i['answerPesonnel'])
                    questionId = i['questionId']
                    questionDesc = i['questionDesc']
                    answerPesonnel = i['answerPesonnel']

                    l1.append(questionId)
                    l1.append(questionDesc)
                    # l1.append(answerPesonnel)
                    l2.append(l1)
                time.sleep(3 + random.random())
                print('{1}第{0}页'.format(m,d1[k]))
            except Exception as e:
                print(e)



        d2[d1[k]] = l2
    return d2 # 提取问题ID和问题描述


def getUrl(q_id):
    base_url = 'https://bbs.guahao.com/question/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }

    full_url = base_url + q_id
    print(full_url)
    req = random_Ip().Request(url=full_url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read()

    html = html.decode()
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find(class_='sns-question-reply')


    answer = divs.get_text().replace(' ','')
    # print(answer)
    return answer

def Demo():
    d1 = extract()
    d2 = {}
    l4 = d1.keys()

    for j in l4:
        print(j)
        l3 = []
        for i in d1[j]:
            try:
                l2 = []
                l2.append(i[1])
                answer = getUrl(i[0])

                l2.append(answer)
                l3.append(l2)
                time.sleep(3 + random.random())
            except Exception as e:
                print(e)
        # print(l3)
        d2[j] = l3

    return  d2
def data_format():
    d1 = Demo()
    l6 = d1.keys()
    # l3 = Demo()
    d2 = {}

    for x in l6:
        l5 = []
        for i in d1[x]:
            l4 = []
            l4.append(i[0])
            i = ''.join(i[1].split('\xa0'))
            i = i.split("\n")
            l1 = []

            for m in i:
                if m != '':
                    l1.append(m)
            i = '\n'.join(l1)
            # i = i.split('。')
            # l6 =[]
            # for j in i:
            #     if "赞赏" not in j:
            #         l6.append(j)
            # i = ''.join(l6)
            l4.append(i)
            l5.append(l4)
        d2[x] = l5


    return d2
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
        '0':{'http':'121.61.1.245'},
        '1':{'http':'171.80.1.233'},
        '2':{'http':'112.85.170.183'},
        '3':{'http':'49.86.177.135'},
        '4':{'http':'36.26.225.63'}
    }
    rad = random.randint(0,4)
    # print('Ip地址为{0}'.format(proxy[str(rad)]))
    return  proxy[str(rad)]


def save():
    d1 = data_format()
    tq = openpyxl.Workbook()

    for i in d1.keys():
        Sheet = i
        tq.create_sheet(Sheet)
        print(Sheet)
        Sheet = tq[Sheet]
        for j in d1[i]:
            Sheet.append(j)

    tq.save('C:/Users/meridian/Desktop/提取练习/各科室50页已爬取.xlsx')

if __name__ == '__main__':
    time_start = time.time()
    save()
    time_end = time.time()
    print("totally cost",time_end - time_start)