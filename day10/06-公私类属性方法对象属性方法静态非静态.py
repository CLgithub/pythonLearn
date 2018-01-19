#coding=utf-8
'''
静态的只能是方法，也只能是类的
'''
class A(object):
    def print__AM(self,name):
        print(A.__privateClassAttr)
        print(eval(name))
    def __str__(self):
        return "A []"
    # 公共的 类的 属性 
    publicClassAttr="publicClassAttr"
    # 公共的 对象的 属性 
    def __init__(self):
        self.publicObjectAttr="publicObjectAttr"
    # 私有的 类的 属性 
    __privateClassAttr="__privateClassAttr"
    # 私有的 对象的 属性 

    # 公共的 类的 方法
    # 公共的 对象的 方法 
    # 私有的 类的 方法 
    # 私有的 对象的 方法

    # 公共的 类的 静态的 方法 
    # 私有的 类的 静态的 方法 

print("------公共的 类的 属性---------")
print(A.publicClassAttr)
a=A()
print(a.publicClassAttr)
print("------公共的 对象的 属性---------")
print(a.publicObjectAttr)
print("------私有的 类的 属性---------")
a.print__AM("A.__privateClassAttr")

