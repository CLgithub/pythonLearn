#coding=utf-8

import numpy as np

a = np.array([[1,2,3],[0,'b',6]])
print(a, a.dtype)
a = np.array([[1,2,3],[0,3,6]],dtype=np.float64)
print(a, a.dtype)
