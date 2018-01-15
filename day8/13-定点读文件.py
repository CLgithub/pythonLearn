#coding=utf-8
'''
f.tell() 返回当前都到什么位置
f.seek(offset,from) 
offset 偏移量
from 0:文件开头，1:当前位置，2:文件末尾
'''
f=open("file1","r")

i=f.tell()
print("当前读取到的位置:%d"%i)

f.seek(0,2)
i=f.tell()
print("当前读取到的位置:%d"%i)

f.seek(1,0)
i=f.tell()
print("当前读取到的位置:%d"%i)
