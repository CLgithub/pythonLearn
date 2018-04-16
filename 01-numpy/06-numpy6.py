#coding=utf-8
#布尔数组索引,可以选择数组中的任意元素

import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)
print("-"*40)

bool_idx = (a>2)
print(bool_idx)
print("-"*40)

print(a[bool_idx])
print("-"*40)

print(a[a>2])

