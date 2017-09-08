#coding=utf-8
names=["aa",'bb',123,"dd"]
print("names=%s"%names)

#------------------------while
i=0
while i<len(names):
    print("names[%d]=%s "%(i,names[i]),end="")
    i+=1
print("")
#-----------------------for
for name in names:
    print("%s "%name,end="")
print("")
print("------------------------------")
infor={"1":"aa",2:"bb",3:"cc","4":"dd"}
print("infor=%s"%infor)
