#coding=utf-8
class Dog(object):
    __dog=None
    def __new__(cls,x):
        if(cls.__dog==None):
            cls.__dog=super().__new__(cls)
            #cls.__dog.x=x
        return cls.__dog

    __c=None
    def __init__(self,x):
        #pass
        if(self.__c==None):
            Dog.__c=x
            self.x=x
            
    def __str__(self):
        return "对象的描述信息%s"%self.x

a=Dog("abc")
print(id(a))
print(a)
b=Dog("xxx")
print(id(b))
print(b)
