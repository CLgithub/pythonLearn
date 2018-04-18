#coding=utf-8
import numpy as np

v=np.array([1,2,3])
w=np.array([4,5])

print(np.reshape(v,(3,1))*w) #将v平铺，然后按照3行1列组合起来

print('-'*40)
x = np.array([[1,2,3],[4,5,6]])
print(x+v)

print('-'*40)
print((x.T+w).T)

print('-'*40)
print(x+np.reshape(w,(2,1)))

print('-'*40)
print(x*2)
