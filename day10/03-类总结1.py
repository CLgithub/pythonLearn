#coding=utf-8
'''
1.类的定义
    class 类名:
        def 方法名(self,参数1,参数2,...): 
            pass
    其中self表示调用该方法的对象，类似java的this

2.私有
    类似java的private，只能在类内部访问（调用），若按javabean规范，属性应该都是私有的，getset方法应该都是公有的。语法：在方法名前加__，调用时也要添加__

3.类的几个魔法方法
    语法：__方法名__(self):
            pass
    init方法:创建该类或该类的子孙类时会自动调用，可以完成初始化的工作，类似java的构造方法
    str方法:类似java的toString()方法，在print对象时，调用该方法，放回一个字符串给print
    del方法:在类创建的对象内存空间没有对象名指向,即引用计数=0时，会自动调用该方法
        sys.getrefcount(对象) 返回改对象的引用计数 对象名一个，该方法调用一个
    ？思考：魔法方法算私有方法吗？？？

4.继承
    class 子类名(父类名):
        pass

5.私有在继承中的表现
    私有方法和私有属性不能被子类继承，也不能在类外边被访问和调用
'''

class A:
    def __init__(self, attr1, attr2):
        self.attr1=attr1
        self.__attr2=attr2
        print("%s对象被创建"%(self))
    def __str__(self):
        return "A = [attr1:%s, __attr2:%s]"%(self.attr1, self.__attr2)
    def __del__(self):
        print("%s被回收♻️ "%self)

    def meath1(self):
        print("---------meath1-----------")
    def __meath2(self):
        print("---------__meath2-----------")

    def getAttr2(self):
        return self.__attr2
    def setAttr2(self,attr2):
       self.__attr2=attr2
class B(A):
    def meath3(self):
        print("---------meath3-----------")
#####################################

a1=A("attr1","attr2")
print(a1)
print(a1.attr1)
#print(A1.__attr2) #类外部不能直接方法私有属性
#a1.__meath2() #类外部不能直接调用私有方法
a1.setAttr2(123)
print(a1.getAttr2())
print("----------------------------")
#####################################
b1=B("battr1","") #会使用父类的构造方法

#print(b1)

