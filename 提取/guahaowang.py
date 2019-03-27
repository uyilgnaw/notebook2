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

def Page(m):

    url = 'https://bbs.guahao.com/gateway/modulesns/mutualhelp/homepagewaterfall.json'

    data = {
        'firstTime': '{0}'.format(time_stamp()),
        'pageNo': '{0}'.format(m),
        'pageSize': '20',
        'sortMethod': '0',
        'tagGroupId': "",
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
        return
def extract():
    l2 = []

    for m in range(1,4):
        try:
            for i in Page(m)['items']:
                l1 = []
                # print(chuli(1))
                # print("问题id:",i['questionId'])
                # print("问题描述:",i['questionDesc'])
                # print("回答问题人数,",i['answerPesonnel'])
                questionId = i['questionId']
                questionDesc = i['questionDesc']
                answerPesonnel = i['answerPesonnel']
                if answerPesonnel != 1 :
                    l1.append(questionId)
                    l1.append(questionDesc)
                    l1.append(answerPesonnel)
                    l2.append(l1)
            time.sleep(3 + random.random())
            print('第{0}页'.format(m))
        except Exception as e:
            print(e)


    return l2 # 提取问题ID和问题描述


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
    l1 = extract()
    l3 = []
    try:
        for i in l1:
            l2 = []
            l2.append(i[1])
            answer = getUrl(i[0])
            l2.append(answer)
            l3.append(l2)
            time.sleep(3 + random.random())
        # print(l3)
        return l3
    except Exception as e:
        print(e)
        return l3
def data_format():
    l3 = Demo()
    l5 = []
    for i in l3:
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



    return  l5
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
        '0':{'http':'185.32.229.199'},
        '1':{'http':'119.190.196.100'},
        '2':{'http':'112.78.38.165'},
        '3':{'http':'218.38.52.132'},
        '4':{'http':'111.198.154.116'}
    }
    rad = random.randint(0,4)
    print('Ip地址为{0}'.format(proxy[str(rad)]))
    return  proxy[str(rad)]

def excel_save():
    tq = openpyxl.Workbook()
    Sheet1 = tq.active


    print("开始写入")
    l3 = data_format()
    for i in l3:
        Sheet1.append(i)
    print("写入完成")
    tq.save('C:/Users/meridian/Desktop/提取练习/已处理.xlsx')


if __name__ == '__main__':
    excel_save()



