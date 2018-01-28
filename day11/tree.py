#coding=utf-8
import os

def treeDir(dirStr,i):
    i+=1
    thisdirlist=os.listdir(dirStr)
    for f in thisdirlist:
        if(f.startswith(".")):
            pass
        else:
            try:
                #print("%s/%s"%(dirStr,f))
                list2=os.listdir("%s/%s"%(dirStr,f))
                #print("%s/%s"%(dirStr,f))
                print("|___ "*i,end="")
                print(f)
                treeDir("%s/%s"%(dirStr,f),i)
            except (Exception) as e:
                print("|___ "*i,end="")
                print(f)
        
if "__main__"==__name__:
    dirStr=input("请输入要遍历的目录：")
    treeDir(dirStr,0)


