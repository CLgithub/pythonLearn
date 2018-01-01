#coding=utf-8

print("--------------列表----------------")
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
print("--------------字典----------------")
infor={"1":"aa",2:"bb",3:"cc","4":"dd"}
print("infor=%s"%infor)#直接打印
print("len(infor)=%s"%len(infor))#len可以得到字典键值对的个数
for key in infor:# 直接in可以得到key
    print("%s=%s "%(key,infor[key]),end="") 
print("")
print("infor.keys()=%s"%infor.keys())
print("infor.values()=%s"%infor.values())
print("infor.items()=%s"%infor.items())
for kv in infor.items(): #使用迭代器遍历
    print("key=%s,value=%s "%(kv[0],kv[1]),end="")
print("")

for kv in infor.items():#由于迭代出来的keyvalue 是元组，所以可以利用拆包来来遍历
    key,value=kv
    print("key=%s,value=%s "%(key,value),end="")
print("")
for key,value in infor.items():#由于迭代出来的keyvalue 是元组，所以可以利用拆包来来遍历
    print("key=%s,value=%s "%(key,value),end="")
print("")
