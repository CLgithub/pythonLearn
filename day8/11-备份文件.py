#coding=utf-8

fileName=input("请输入要备份的文件的文件名")

f1=open(fileName,"r")
f2=open(fileName+".bak","a")
#f2.write(f1.read())
#content5="null"
#while content5!="":
#    content5=f1.read(5)
#    if content5!="":
#        #print(content5)
#        f2.write(content5)

while True:
    c5=f1.read(5)
    if c5=="":
        break
    f2.write(c5)
f1.close()
f2.close()
