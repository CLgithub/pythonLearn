#coding=utf-8
from scipy.misc import imread, imsave, imresize
import numpy as np
img=imread('/Users/l/Pictures/a.jpg')
print(img.shape)
#print(img)

x=np.full((6,6,3),251)
x2=np.array([0.7,1,0.5])
img_tinted=np.dot(img,x2)
#img_tinted=x2*img
y=np.array(img_tinted).T
#print(y)

#print(img_tinted)
#img_tinted = imresize(img_tinted, (4, 4))
imsave('/Users/l/Pictures/y.jpg',y.T)#转置相当于中心对称

