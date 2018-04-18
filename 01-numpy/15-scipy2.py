#coding=utf-8
#点之间的距离
import numpy as np
from scipy.spatial.distance import pdist,squareform

x = np.array([[0,1],[1,0],[2,0]])
print(x)
d = squareform(pdist(x,'euclidean'))
print(d)
