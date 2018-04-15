#coding=utf-8

import numpy as np

a = np.zeros((2,2))
print(a)

a = np.ones((2,2))
print(a)

a = np.ones((2,2))
print(a)

a = np.full((2,2),7)
print(a)

a = np.eye(2) #创建特征矩阵为2的矩阵
print(a)

a = np.random.random((5,2)) #创建特征矩阵为2的矩阵
print(a[:,0])
print(a)
