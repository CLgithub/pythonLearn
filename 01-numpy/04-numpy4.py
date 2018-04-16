#coding=utf-8
import numpy as np

a=np.array([[1,2],[3,4],[5,6]])

b=a[ [0,1,2],[0,1,0] ]  #用array[0,1,2]
c=np.array([a[0,0], a[1,1], a[2,0]])
print(a)
print(b)
print(c)
