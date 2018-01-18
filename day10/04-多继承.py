#coding=utf-8
class Base(object): #python3所有类默认都了都继承object类，可以不写
    def test(self):
        print("----Base")

class A(Base):
    def test(self):
        print("----A")
    def test1(self):
        print("----test1")

class B(Base):
    def test(self):
        print("----B")
    def test2(self):
        print("----test2")

class C(B,A): #C同时继承A和B，思考如果A,B,C有相同名字的方法，调用该方法时，用谁的:先看自己有木有，有就使用自己的，没有就使用先继承的,可以用C.__mro__返回的元祖查看
    pass
    #def test(self):
    #    print("C----Base")


c=C()
c.test()
print(C.__mro__) #调用一个方法时搜索的顺序, C3算法决定
