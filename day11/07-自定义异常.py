#coding=utf-8
'''
'''

class MyE(Exception): #自定义异常
    def __init__(self,a,b):
        self.a=a
        self.b=b

def func1():
    try:
        print("a")
        raise Exception("故意抛出一个异常")  #raise 抛出异常，相当于java的throw
#        raise
    except (Exception) as e:
        try:
            print("异常：%s"%e)
            raise MyE(1,2) #同样抛出异常，不过改异常是自定义的
        except (MyE) as e2:
            print("异常：%s"%e2)
            raise    #将异常再次抛出给调用者，在java中是在定义方法是声明可能会爬出什么异常，而python是直接这样抛出

func1()
