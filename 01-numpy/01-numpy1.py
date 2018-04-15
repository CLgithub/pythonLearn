#coding=utf-8

import numpy as np

a = np.array([1,2,3])
print(type(a))
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)  #shape形状 
print(b[0][0], b[0][1], b[1][0]) 
print(b[0,0], b[0,1], b[1,0]) 
print(b[:,1])
