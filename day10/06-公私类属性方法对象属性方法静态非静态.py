#coding=utf-8
'''
静态的只能是方法，也只能是类的
'''
class A(object):
    @classmethod
    def print__privateClassAttr(cls):
        print(cls.__privateClassAttr)
    def print__privateObjectAttr(self):
        print(self.__privateObjectAttr)
    @classmethod
    def print__privateClassMethod(cls):
        cls.__privateClassMethod()
    def print__privateObjectMethod(self):
        self.__privateObjectMethod()
    @classmethod
    def print__privateClassStaticMethod(cls):
        cls.__privateClassStaticMethod()
    def __str__(self):
        return "A []"
#############################################
    # 公共的 类的 属性 
    publicClassAttr="publicClassAttr"
    # 公共的 对象的 属性 
    # 私有的 对象的 属性 
    def __init__(self):
        self.publicObjectAttr="publicObjectAttr"
        self.__privateObjectAttr="__privateObjectAttr"
    # 私有的 类的 属性 
    __privateClassAttr="__privateClassAttr"

    # 公共的 类的 方法
    @classmethod
    def publicClassMethod(cls):
        print("publicClassMethod")
    # 公共的 对象的 方法 
    def publicObjectMethod(self):
        print("publicObjectMethod")
    # 私有的 类的 方法 
    @classmethod
    def __privateClassMethod(cls):
        print("__privateClassMethod")
    # 私有的 对象的 方法
    def __privateObjectMethod(self):
        print("__privateObjectMethod")

    # 公共的 类的 静态的 方法 
    @staticmethod
    def publicClassStaticMethod():
        print("publicClassStaticMethod")
    # 私有的 类的 静态的 方法 
    @staticmethod
    def __privateClassStaticMethod():
        print("__privateClassStaticMethod")
    def method():
        print("method")

a=A()
print("------公共的 类的 属性---------")
print(A.publicClassAttr)
print(a.publicClassAttr)
print("------公共的 对象的 属性---------")
print(a.publicObjectAttr)
print("------私有的 类的 属性---------")
A.print__privateClassAttr()
print("------私有的 对象的 属性---------")
a.print__privateObjectAttr()
print("------公共的 类的 方法---------")
A.publicClassMethod()
a.publicClassMethod()
print("------公共的 对象的 方法---------")
a.publicObjectMethod()
print("------私有的 类的 方法---------")
A.print__privateClassMethod()
print("------私有的 对象的 方法---------")
a.print__privateObjectMethod()
print("------公共的 类的 静态的 方法---------")
A.publicClassStaticMethod()
a.publicClassStaticMethod()
print("------私有的 类的 静态的 方法---------")
A.print__privateClassStaticMethod()
print("--------")
A.method()
#a.method()
