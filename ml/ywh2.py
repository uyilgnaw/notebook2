import matplotlib.pyplot as plt

import numpy as np

from sklearn.datasets import load_iris

from sklearn.linear_model import LogisticRegression


# 载入数据集
iris = load_iris()
X = iris.data[:, :2]  # 获取花卉两列数据集
Y = iris.target
# print(X)
#
# print(Y)

'''
一共有14个参数
    - penalty：惩罚项，str类型，可选参数为l1和l2，默认为l2
    - dual：对偶或原始方法，bool类型，默认为false
    - tol：停止求解的标准，float类型，默认为1e-4.就是求解到多少的时候，停止，认为已经求出最优解
    - C：正则化系数lama的倒数，float类型，默认为1.0.必须是正浮点型数

'''
lr = LogisticRegression(C=1e5)
# 逻辑回归模型
lr.fit(X, Y)

# meshgrid函数生成两个网格矩阵
h = .02
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# pcolormesh函数将xx,yy两个网格矩阵和对应的预测结果Z绘制在图片上
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(8, 6))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# 绘制散点图
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.scatter(X[100:, 0], X[100:, 1], color='green', marker='s', label='Virginica')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.legend(loc=2)
plt.show()


