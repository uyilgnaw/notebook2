#!/usr/bin/python
# -*- coding:utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn import preprocessing
# import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


'''
python2.7和python3的区别
在字符串前面加u：
    - 作用：后面的字符串以Unicode格式进行编码，一般用在中文字符串前面，防止因为源码格式存储问题，导致再次使用时出现乱码
在字符串前面加r：
    - 作用：声明后面的字符串是普通字符，而不是特殊字符。即不必转义
在字符串前面加b：
    - 作用：b''表示的是一个bytes对象，表示后面的字符串是bytes类型
    
'''



if __name__ == "__main__":
    path = 'C:/Users/meridian/Desktop/8.Regression/8.iris.data'  # 数据文件路径

    # # # 手写读取数据
    # f = file(path)
    # x = []
    # y = []
    # for d in f:
    #     d = d.strip()
    #     if d:
    #         d = d.split(',')
    #         y.append(d[-1])
    #         x.append(map(float, d[:-1]))
    # # # print '原始数据X：\n', x
    # # print '原始数据Y：\n', y
    # x = np.array(x)
    # # print 'Numpy格式X：\n', x
    # y = np.array(y)
    # # print 'Numpy格式Y - 1:\n', y
    # # y[y == 'Iris-setosa'] = 0
    # # y[y == 'Iris-versicolor'] = 1
    # # y[y == 'Iris-virginica'] = 2
    # # print 'Numpy格式Y - 2:\n', y
    # # y = y.astype(dtype=np.int)
    # # print 'Numpy格式Y - 3:\n', y
    #
    # 使用sklearn的数据预处理
    # df = pd.read_csv(path, header=0)
    # x = df.values[:, :-1]
    # y = df.values[:, -1]
    # print ('x = \n', x)
    # print ('y = \n', y)
    # le = preprocessing.LabelEncoder()
    # le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    # # print (le.classes_)
    # y = le.transform(y)
    # print ('Last Version, y = \n', y)

    '''
    np.loadtxt():
        - fname: 要读取的文件，文件名或生成器
        - dtype: 数据类型，默认为float。还可以控制每一列的数据类型和精度等信息
        - comments: 注释
        - delimiter：分隔符，默认是空格
        - skiprows：跳过前几行读取，默认是0，必须是int整型
        - usecols：要读取哪些列，0是第一列。默认读取所有列
        - unpack：如果为True，将分列读取
    
    '''


    def iris_type(s):
        it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
        return it[s]

        # return it[s]


    # 路径，浮点型数据，逗号分隔，第4列使用函数iris_type单独处理
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4:iris_type})
    # print (data)
    # 将数据的0到3列组成x，第4列得到y
    # 把data数据集中的所有数据按第四、五列之间分割为x集，y集
    x, y = np.split(data, (4,), axis=1)

    # 为了可视化，仅使用前两列特征
    x = x[:, :2]

    # print (x)
    #
    # print (y)

    # x = StandardScaler().fit_transform(x)
    # lr = LogisticRegression()   # Logistic回归模型
    # #     lr.fit(x, y.ravel())        # 根据数据[x,y]，计算回归参数
    # #
    # 等价形式

    '''
    peieline构造器接受(name,transform)tuple的列表作为参数。按顺序执行列表中的transform，完成数据预处理
    
    
    '''
    lr = Pipeline([('sc', StandardScaler()),
                ('clf', LogisticRegression()) ])
    lr.fit(x, y.ravel())

    # 画图
    N, M = 1000, 1000    # 横纵各采样多少个值
    # 取第一列最小值和最大值
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()   # 第0列的范围
    # 取第二列最小值和最大值
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()   # 第1列的范围

    # 在默认情况下，linspace函数可以生成元素为50的等间隔数列。而前两个参数分别是数列的开头与结尾
    # 如果写入第三个参数，可以指定数列的元素个数。
    # 以最最小值和最大值生成500个等间隔数列
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)

    '''
    meshgrid的作用是根据传入的两个一维数组参数生成两个数组元素的列表
    如果第一个参数是xarray，维度xdimesion，第二个参数是yarray，维度是
    ydimesion。那么生成的第一个二维数组是以xarray为行，ydimesion行的向量
    而第二个二维数组是以yarray的转置为列，xdimesion列的向量
    '''
    x1, x2 = np.meshgrid(t1, t2)                    # 生成网格采样点
    print(x1)
    print(x2)

    x_test = np.stack((x1.flat, x2.flat), axis=1)   # 测试点

    # 无意义，只是为了凑另外两个维度
    # x3 = np.ones(x1.size) * np.average(x[:, 2])
    # x4 = np.ones(x1.size) * np.average(x[:, 3])
    # x_test = np.stack((x1.flat, x2.flat, x3, x4), axis=1)  # 测试点

    cm_light = mpl.colors.ListedColormap(['#77E0A0', '#FF8080', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    y_hat = lr.predict(x_test)                  # 预测值
    y_hat = y_hat.reshape(x1.shape)                 # 使之与输入的形状相同
    plt.pcolormesh(x1, x2, y_hat, cmap=cm_light)     # 预测值的显示
    plt.scatter(x[:, 0], x[:, 1], c=y.ravel(), edgecolors='k', s=50, cmap=cm_dark)    # 样本的显示
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid()
    # plt.savefig('2.png')
    plt.show()

    # 训练集上的预测结果
    y_hat = lr.predict(x)
    y = y.reshape(-1)
    result = y_hat == y
    print (y_hat)
    print (result)
    acc = np.mean(result)
    print ('准确度: %.2f%%' % (100 * acc))



