#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize

#pi～=3.14 sin(pi)=sin(180')=0
x=np.arange(0,3*np.pi,0.1)
#print(x)
y_sin=np.sin(x)
y_cos=np.cos(x)

plt.subplot(2,2,1)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('sine and cosine1')
plt.legend(['Sine','Cosine'])

plt.subplot(2,2,2)
plt.scatter(x,y_sin,c=x)
plt.scatter(x,y_cos,c=x)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('sine and cosine2')
#plt.legend(['Sine','Cosine'])

plt.subplot(2,2,3)
img1=imread('/Users/l/Pictures/a.jpg')
plt.imshow(img1)

plt.subplot(2,2,4)
img2=img1*[1,0.5,0.5]
plt.imshow(np.uint8(img2))
plt.show()
