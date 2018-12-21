'''
岭回归和Lasso回归主要是为了解决线性回归出现的过拟合以及在通过正规方程方法求解θ的过程中
出现的x转置乘以x不可逆这两类问题，这两种回归均通过在损失函数中引入正则化项来达到目的。

岭回归与lasso回归最大的区别就是岭回归引入的是L2范数惩罚项，Lasso回归引入的是L1范数惩罚项
计算量Lasso回归远远小于岭回归

Lasso回归可以产生稀疏权值矩阵，即产生一个系数模型，可以用于特征选择
    - 稀疏矩阵是指很多元素为0，只有少数元素是非零的矩阵。
    - 在特征很多的时候，带入这些特征得到的模型就是一个稀疏模型，表示只有少数特征对这个模型有贡献（他们前面的系数不为零或者很小的值）
    - 这就是Lasso回归中的稀疏模型和特征选择的关系
岭回归可以防止模型过拟合；一定程度上，Lasso回归也可以防止过拟合
    - 拟合过程中都倾向于让权值尽可能小，最后构造一个所有参数都比较小的模型。
    - 参数值小的模型相对简单，能适应不同的数据集，避免了过拟合现象
    - 其中λ称为正则化参数，如果λ选取过大，会把所有参数θ均最小化，造成欠拟合，如果λ选取过小，会导致对过拟合问题解决不当，因此λ的选取是一个技术活。
损失函数是用来估量模型的预测值与真实值的不一致程度，它是一个非负的实值函数，损失函数越小，模型的鲁棒性（健壮性）就越好


'''


import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import Lasso,Ridge

from sklearn.model_selection import GridSearchCV


if __name__ == '__main__':
    # pandas 读入数据
    path = 'C:/Users/meridian/Desktop/8.Regression/8.Advertising.csv'

    data = pd.read_csv(path)

    x = data[['TV','Radio','Newspaper']]

    y = data['Sales']

    # print(x)
    # print(y)
    # 未指定trainsize时，默认值为0.25
    x_train,x_test, y_train,y_test = train_test_split(x,y,random_state=1)
    # print('训练数据：')
    # print(x_train)
    # print('训练结果')
    # print(y_train)
    # print('测试数据')
    # print(x_test)
    # print(len(x_test))
    # print('测试结果')
    # print(y_test)

    # L1正则化的Lasso回归，会形成一个稀疏矩阵，选择有意义的特征
    model = Lasso()
    # L2正则化的岭回归，其中的参数λ的确定会影响模型是否过拟合或欠拟合的关键因素
    # model = Ridge()

    # 创建一个开始点为10的-3次方，结束点为10的平方，元素个数为10的等比数列,作为最后参数lamada的值
    # 每个alpha_can都会进行一次预测，选择最小的值
    # 所说的正则项，就为alpha_can
    alpha_can = np.logspace(-3,2,10)
    #print(alpha_can)

    '''
    GridSearchCv,它存在的意义就是自动调参，只要把参数输入进去，就能给出最优化的结果和参数
    但是这个方法适合小数据集，一旦数据量变大，很难得出结果。
    参数为
        - estimator:所使用的分类器，就是用哪个算法模型
        - param_grid:值为字典或者列表，即需要最优化的参数的取值。
        - scoring：准确度评价标准，默认None，这是需要使用score函数。如果时None，则使用estimator的误差估计函数
        - cv:交叉验证参数，默认None，使用三折交叉验证。指定fold数量，默认为3。
        - refit：默认为true，程序将会以交叉验证训练集得到的最佳参数。即在搜索参数结束后，用最佳参数结果再fit一遍全部的数据集
        - iid：默认true，为true时，默认为各个样本fold概率分布一致，误差估计为所有样本之和，而非各个fold的平均
        - verbose：日志冗长度，int：冗长度，0：不输出训练过程，1：偶尔输出，>1：对每个子模型都输出
        - pre_dispatch：指定总共分发的并行任务数。
        
    
    
    '''
    # 5折交叉验证
    lasso_model = GridSearchCV(model,param_grid={'alpha':alpha_can},cv=5)
    # 用所有的原始数据进行计算
    lasso_model.fit(x,y)
    #
    # print('验证参数为',lasso_model.best_params_)
    # print('最好成绩为',lasso_model.best_score_)
    # #print(lasso_model)

    y_hat = lasso_model.predict(np.array(x_test))
    # 同样计算均方误差和均方根误差
    mse = np.average((y_hat - np.array(y_test)) ** 2)
    rmse = np.sqrt(mse)

    # print(mse)
    # print(rmse)

    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

    '''
    通过对比发现岭回归的mse和rmse值略好于lasso回归和线性回归
    但不是绝对
    
    '''