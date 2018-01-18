#coding=utf-8
class Base(object):
    def print_self(self):
        print(self)
    def __str__(self):
        print("Base[]")

class A(Base):
    def print_self(self):
        print("A")
class B(Base):
    def print_self(self):
        print("B")

def introduce(base): #python是若类型的语言，多态体现的不明显，java或c++中传参需要指定类型Base，都是Base的对象，执行同一个方法，却有多种形态
    base.print_self() #执行同一个东西的同一个方法，却有不同形态

a=A()
b=B()
introduce(a)
introduce(b)
