'''
 Numpy是Python语言的一个扩充程序库。支持高级大量的维度数据与矩阵运算，
 此外也针对数组运算提供大量的数学函数库。Numpy内部解除了Python的PIL（全局解释锁）
 ，运算效率极好，是大量机器学系框架的基础库。


'''

# Numpy简单创建数组

import numpy as np

# 创建一个简单的列表
# a = [1, 2, 3, 4]
# # 将列表转换为数组
# b = np.array(a)
# print(b)
#
# # Numpy查看数组属性
# # 数组元素的个数
# print(b.size)
#
# # 数组的形状,表示该数组有几行几列
#
# print(b.shape)
#
# # 数组的维度
# print(b.ndim)
#
# # 数组的元素类型
# print(b.dtype)
#
# # 快速创建N维数组的api函数
# # 创建10行10列的数值为浮点1的矩阵(默认类型为浮点型)
# array_one=np.ones([10, 10], dtype=int)
# print(array_one)
#
# # 创建10行10列数值为浮点0的矩阵
# array_zero=np.zeros([10,10])
# print(array_zero)

# 从现有的数据创建数组
    # numpy中array和asarray的区别，array和asarray都可以将结构数据转化为ndarray，但是主要区别就是当数据源是ndarray时，array仍然
    # 会copy出一个副本，占用新的内存，但asarray不会。
# 例1
# data1=[[1,1,1],[1,1,1,],[1,1,1]]
# arr2=np.array(data1)
# arr3=np.array(data1)
# data1[1][2]=2
#
# print('data1\n',data1)
# print('arr2\n',arr2)
# print('arr3\n',arr3)
# 以上例子可以看出，array和asarray没有区别，都对原始数据进行了复制

# 例2

# arr1=np.ones((3,3))
# arr2=np.array(arr1)
# arr3=np.asarray(arr1)
# arr1[1]=2
#
# print('arr1:\n',arr1)
# print('arr2:\n',arr2)
# print('arr3:\n',arr3)
# 以上例子可以看出，由array创建的数组，会生成一个新的对象，当原始数据改变时，array生成的对象不会改变，asarray相反

# 深拷贝和浅拷贝的理解
'''
深拷贝：原始数据发生改变时，由原始数据拷贝而来的新数据不会发生改变
浅拷贝：原始数据发生改变时，由原始数据拷贝而来的新数据会发生改变
'''

# Numpy创建随机数组np.random

# 均匀分布
# 创建指定形状（实例为10行10列）的数组（范围在0至1之间）
# print(np.random.rand(10,10))
# # 创建指定范围内的一个数
# print(np.random.uniform(0,100))
# # 创建指定范围内的一个整数
# print(np.random.randint(0,100))

# 正态分布
# 给定均值/标准差/维度的正态分布
# print(np.random.normal(1.75,0.1,(2,3)))
# arr = np.random.normal(1.75,0.1,(4,5))
# print(arr)
# # 表示从第二行的第三列截取到第三行的第四列
# print(arr[1:3,2:4])

# print('reshape函数的使用！')
# one = np.ones([20])
# print(one)
# one_1=one.reshape([4,5])
# print(one_1)
# # 第二个参数是-1时默认将分为整除列
# one_2=one.reshape([4,-1])
# print(one_2)
# # 第一个参数为-1时，原数组将不变
# one_3=one.reshape([-1,-1])
# print(one_3)

# arr=np.array([[80,88],[82,82],[84,75],[86,83],[75,81]])
# # numpy可直接进行判断布尔值
# print(arr>80)
# # 常规数组则不可以直接进行判断
# # arr1=[[80,88],[82,82],[84,75],[86,83],[75,81]]
# # print(arr1>80)
#
# arr1=np.array([[80,88],[82,82],[84,75],[86,83],[75,81]])
# # 用numpy中的where方法,进行三元运算。
# print(np.where(arr1>80,'牛逼','辣鸡'))

# x = np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
#
# print(x)

# list=range(5)
# it=iter(list)
#
# x=np.fromiter(list,dtype=float)
# print(x)

# a = np.logspace(1,10,num=5,base=2)
# print(a)


# a=np.arange(10)
# b=a[1]
# print(b)


