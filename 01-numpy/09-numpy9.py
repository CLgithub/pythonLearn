#coding=utf-8

import numpy as np

a = np.array([[1,2],[3,4],[1,1]])
b = np.array([[2],[4]])

print(a)
print('----------')
print(b)
print('----------')
print(a.dot(b))
print('----------')
print(np.dot(a,b))

'''
矩阵乘法    前提 a的列数 = b的行数
结果矩阵的行数=a的行数 列数=b的列数
结果矩阵的m,n的值=a第m行 与 b第n列 分别相乘 然后相加
'''
