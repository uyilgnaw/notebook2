import openpyxl
from multiprocessing import Process





def tiqu():
    e1 = openpyxl.load_workbook("C:/Users/meridian/Desktop/提取练习/提取.xlsx")
    w1 = e1.active
    l1 = []  # l1为所有行的汇总列表
    for i in w1['A']:
        i = i.value
        i = i.split('。')
        l1.append(i)
    l2 = []

    for i in l1:
        l4 = []
        l3 = []

        l4.append(i[0])

        for j in i:
             if "肺" in j or "胸膜" in j:
                if "肉芽肿" in j or "癌" in j or "结节" in j :
                    l3.append(j)

        l4.append('。'.join(l3))
    #     l4.append('。'.join(l5))
        l2.append(l4)

    e2 = openpyxl.Workbook()
    w2 = e2.active
    w2.title = "已提取"
    m = 0
    for i in l2:
        w2.append(i)
        m = m + 1
        print("已经提取了{0}行".format(m))

    print("提取完成!")
    print("保存中...")
    e2.save("C:/Users/meridian/Desktop/提取练习/已提取.xlsx")


if __name__ == '__main__':
    p = Process(target=tiqu)
    p.daemon = True
    p.start()
    p.join()
    print("保存完成")