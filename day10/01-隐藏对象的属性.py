#coding=utf-8

'''
隐藏对象的属性，应该类似java的private修饰

定义私有方法：在方法名前加__ 相当于java里的private

__del__方法：当对象内存空间没有对象名指向,即引用计数=0时，会自动调用该方法

'''
import sys
class Dog:
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age

    #公有方法
    def test1(self):
        print("---------1---------")
        #在公有方法里调用私有方法
        self.__test2()
    #私有方法
    def __test2(self):
        print("---------2---------")
    #del方法 当对象被删除时会自动调用该方法
    def __del__(self):
        print("%s被删除"%self)
    def __str__(self):
        return "Dog[%s]"%self.name
dog=Dog()
dog.age=3
dog.name="小白"
#dog.setAge(3)
print(dog.getAge())

dog.test1()
#dog.__test2()  #test2方法是私有的，不能调用
print("-"*40)
print("引用计数：%d"%sys.getrefcount(dog)) #dog一个指针，掉该方法时另一个指针
dog2=dog
print("引用计数：%d"%sys.getrefcount(dog))
dog=""
#dog2=""
#del dog
print("引用计数：%d"%sys.getrefcount(dog2))
#del dog2
print("="*30)



