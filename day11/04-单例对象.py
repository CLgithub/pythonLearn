#coding=utf-8
class Dog(object):
    __dog=None
    def __new__(cls,x): #cls是Dog类,该方法在构造对象时会第一个被调用，用于创建对象，并返回所创建的对象
        if(cls.__dog==None):
            cls.__dog=super().__new__(cls)
        return cls.__dog

    def __init__(self,x):
        self.x=x
    def __str__(self):
        return "对象的描述信息%s"%self.x

a=Dog("abc")
print(id(a))
b=Dog("xxx")
print(id(b))
print(b)
