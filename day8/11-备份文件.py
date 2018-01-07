#coding=utf-8
fileName=input("请输入要备份的文件的文件名")

f1=open(fileName,"r")
f2=open(fileName+".bak","w")
f2.write(f1.read())

f1.close()
f2.close()
