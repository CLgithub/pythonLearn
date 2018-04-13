#coding=utf-8
import os

def t(dirStr,i):
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
                t("%s/%s"%(dirStr,f),i)
            except (Exception) as e:
                print("|___ "*i,end="")
                print(f)
        
def tree():
    t("./",0)
    
if "__main__"==__name__:
    tree()

