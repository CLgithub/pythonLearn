#coding=utf-8
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

#数学定义中不能这样运算，也可能是自己目前理解有误
print(v.dot(w))
print(np.dot(v,w))
print('-----------------')

print(v.dot(x))
print(np.dot(v, x)) #np.dot(x,v) 按照数学中的定义是没有意义的，但是这里能算出来，应该会按能算的方式取组合
print('-----------------')

#print(x*y)  #元素相乘
print(x.dot(y))
print(np.dot(y, x))
print('-----------------')

a=np.array([[1],[2]])
b=np.array([1,2])
#print(a*b)
#print(b*a)
print(b.dot(a))
