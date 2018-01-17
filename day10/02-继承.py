#coding=utf-8
'''
继承：
    class 子类名(父类名):
重写：
   直接在子类里定义 

'''
#定义一个父类 Animal
class Animal:
    def __init__(self):
        self.a=100
        self.__b=200
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def sleep(self):
        print("----睡----")
    def run(self):
        print("----跑----")
        self.__runCool() #在类内部，私有方法是可以被访问的
    def __runCool(self):
        print("----跑酷----")

#定义一个子类继承父类
class Dog(Animal):
    def bark(self):
        print("----🐶 汪汪汪----")
#定义一个子类继承父类
class Cat(Animal):
    def catch(self):
        print("----🐱 抓🐭 ----")

class Xiaotq(Dog):
    def fly(self):
        print("----飞----")
    #方法重写 重写bark方法
    def bark(self):
        print("----啸天🐶 汪汪汪----")
        #调用父类的bark方法
        #Dog.bark(self) 方法一
        super().bark() #方法二
#-----------------------------------#

#a=Animal()
#a.run()

dog1=Dog()
dog1.eat()
dog1.bark()
print("-"*40)
tom=Cat()
tom.run()
tom.catch()
print("-"*40)
xtq=Xiaotq()
xtq.run()
xtq.bark()
xtq.fly()
print("-"*40)
print(xtq.a)
#print(xtq.__b) 
#xtq.__runCool() 子类不能继承父类的私有属性和私有方法

