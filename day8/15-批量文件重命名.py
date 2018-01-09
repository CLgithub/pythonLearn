#coding=utf-8

import os
os.mkdir("dir1")
i=0
while i<10:
    i+=1
    f=open("./dir1/文件-%d.txt"%i,"w+")
    f.write("文件内容%d"%i)
    f.close()

files=os.listdir("./dir1")
os.mkdir("dir2")
for f in files:
    os.rename("./dir1/%s"%f,"./dir2/a-%s"%f)
