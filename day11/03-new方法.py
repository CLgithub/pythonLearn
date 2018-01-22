#coding=utf-8
'''
xtq=Dog("x")
1.先调用Dog类的__new__(cls,x)方法创建对象，cls为Dog类，x为创建对象时的参数，并返回所创建的对象，
    创建对象通过Dog类的父类object的__new__(cls)方法创建对象，并且返所创建的对象
2.将init方法创建的对象self与x传给init方法进行对象初始化工作
3.将初始化好的对象返回给xtq
4.当这个对象没有指数所指向它时，掉用del方法
'''
class Dog(object):
    def __new__(cls,x): #cls是Dog类,该方法在构造对象时会第一个被调用，用于创建对象，并返回所创建的对象
        print("----new----")
        return super().__new__(cls)
        #return object.__new__(cls)
    def __init__(self,x):
        self.x=x
        print("----init----")
    def __del__(self):
        print("----del----")
    def __str__(self):
        print("----str----")
        return "对象的描述信息%s"%self.x

xtq=Dog("abc")
print(xtq)

