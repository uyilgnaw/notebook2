import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris  # 导入数据集iris

# 载入数据集

iris = load_iris()
# print (iris.data)  # 输出数据集
# # 一共150条纪录，分别代表三种鸢尾花各50个（0，1，2）
# print (iris.target)  # 输出真实标签
# 获取花卉两列数据集
DD = iris.data

# 提取鸢尾花数据中的第一列，一共150个元素
X = [x[0] for x in DD]
print(X)
# 提取鸢尾花数据中的第二列，一共150个元素
Y = [x[1] for x in DD]
print(Y)
'''
绘制散点图，其中X和Y是相同长度的数组序列
    - s:默认20
    - c：色彩或者颜色序列，可选
        - 
    - maker：MakerStyle，可选，默认为"o"
    - cmap：Colormap可选，默认：None
    - norm：Normalize可选，默认：None
    - vmin，vmax：标量，可选，默认：None
    - alpha:标量，可选，默认：None
    - linewidths：标量或数组，默认：None

    此处将iris.target的序列当作颜色传入，前50个元素为0，中间为1，最后为2，进行颜色划分，但形状都是相同的
    也可分别进行绘制

'''
plt.scatter(X, Y, c=iris.target, marker='x')
# plt.scatter(X[:50], Y[:50], color='red', marker='o', label='setosa')  # 前50个样本
# plt.scatter(X[50:100], Y[50:100], color='blue', marker='x', label='versicolor')  # 中间50个
# plt.scatter(X[100:], Y[100:], color='green', marker='+', label='Virginica')  # 后50个样本
plt.legend(loc=2)  # 左上角
plt.show()
