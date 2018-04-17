#coding=utf-8

import numpy as np

x = np.array([[1,2],[3,4]])

print(x)
print(np.sum(x))    #所有元素求和
print(np.sum(x, axis=0))    #各列元素求和得到数组
print(np.sum(x, axis=1))    #各行元素求和
