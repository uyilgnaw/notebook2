'''
销量与广告的线性回归模型
'''

import csv

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    path = 'C:/Users/meridian/Desktop/8.Regression/8.Advertising.csv'

# pandas数据读入
data = pd.read_csv(path)
# 将数据中的特征项输入
# x = data[['TV', 'Radio', 'Newspaper']]
# print(data)
x = data[['TV','Radio']]

y = data['Sales']
# 将文件特征内容输出，并打印文件行数和列数
# print(x)
# # # 将文件结果内容输出，并打印文件行数和数据类型
# print(y)

# 绘制第一种图形

# plt.plot(data['TV'], y, 'ro', label='TV')
#
# plt.plot(data['Radio'], y, 'g^', label='Radio')
#
# plt.plot(data['Newspaper'], y, 'mv', label='Newspaper')
# # 在图中显示各个特征的具体表现形式
# plt.legend(loc='lower right')
# # 在图中显示网格线
# plt.grid()
# # 展示效果图
# plt.show()

# 绘制第二种图形

# plt.figure(figsize=(9,12))
# # 返回一条给定网格位置的轴
# plt.subplot(311)
#
# plt.plot(data['TV'], y, 'ro')
#
# plt.title('TV')
#
# plt.grid()
#
# plt.subplot(312)
#
# plt.plot(data['Radio'], y, 'g^')
#
# plt.title('Radio')
#
# plt.grid()
#
# plt.subplot(313)
#
# plt.plot(data['Newspaper'], y, 'b*')
#
# plt.title('Newspaper')
#
# plt.grid()
# # 调整子图之间的间隔来减少堆叠
# plt.tight_layout()
#
# plt.show()

'''
这里将对所给的数据分为训练数据和测试数据，给定随机初始值为1。
可以添加train_size参数划分用于训练和预测的数据的比例。
x_tarin表示用于训练的特征元素(原始特征值),y_train表示用于训练的y元素（对应的Sales值）
x_test表示用于测试的特征元素（原始特征值），y_test表示用于测试的y元素（原始值，用于与测试输出后的y值进行比较）

'''
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
# print('训练数据：')
# print(x_train)
# print('训练结果')
# print(y_train)
# print('测试数据')
# print(x_test)
# print(len(x_test))
# print('测试结果')
# print(y_test)

# 此处引入线性回归模型
linreg = LinearRegression()

# fit进行计算，x_train，y_train以矩阵的方式传入，其中有sample_weight参数则是每条测试数据的权重，同样以array格式传入
model = linreg.fit(x_train, y_train)

# print(model)
# # 回归系数
# print(linreg.coef_)
# # 截距
# print(linreg.intercept_)
# 预测结果
y_hat = linreg.predict(np.array(x_test))
# print(y_hat)
# print(y_test)
# 均方误差（越小越好）
mse = np.average((y_hat - np.array(y_test))**2)
# 均方根误差（越小越好）
rmse = np.sqrt(mse)

# print(mse, rmse)

# 将用于预测的数据个数形成一个列表，作图用作横坐标
print(y_hat)
t = np.arange(len(x_test))

plt.plot(t, y_test, 'r-',linewidth=2, label ='Test')

plt.plot(t, y_hat, 'g-',linewidth=2, label ='Predict')
# 显示图形详情并分配位置
plt.legend(loc='upper right')

plt.grid()

plt.show()

'''
上面的试验中，当输入的特征指标中不包含newspaper时 ，生成的均方误差和均方根误差比包含newspaper小
也就是说更加精确
需要注意的是，首先要分析原始数据，去除不必要的特征值。才能使模型更加精确，预测的更加精准
并不是说特征越多，预测的结果越好
'''