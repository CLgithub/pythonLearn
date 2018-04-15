#ocding=utf-8

import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a, a.shape)
print('-'*50)
b=a[1:, 2:] #可以获取到任意区域

print(b, b.shape)
