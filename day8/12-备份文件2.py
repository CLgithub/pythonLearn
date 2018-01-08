#coding=utf-8

fileName=input("请输入要备份的文件的文件名")

f1=open(fileName,"r")
f2=open(fileName+".bak","a")
#f2.write(f1.read())
c5="null"
while c5!="":
    c5=f1.readline()
    if c5!="":
        f2.write(c5)
f1.close()
f2.close()
