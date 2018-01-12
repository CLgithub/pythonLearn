#conding=utf-8
'''
定义一个类
class 类名:
    属性
    方法
    def 方法名(self):     self相当于java中的this
        方法体
根据类创建对象
类名()

'''

#定义一个类Cat
class Cat:
    name="tom"
    def eat(self):
        print("%s🐱在吃🐟"%self.name)
    def drink(self):
        print("%s🐱在和🍶"%self.name)

    def introduce2(self):
        print("------------%s-----------"%self)
        #print("%s的年龄是%d"%(Cat.name,cat1.age))
        print("a=%d"%(cat1.a)) #访问cat1的a
        print("a=%d"%(self.a)) # 访问每个对象自己的a，没有就访问类的，类也没有a就报错
#创建一个对象
cat1=Cat()
cat2=Cat()
cat3=Cat()

cat1.a=19 #给cat1添加属性
cat2.a=20 #给cat2添加属性
Cat.a=21 #给Cat添加属性

#print("%s的年龄是%d"%(cat1.name,cat1.age))
cat1.eat()
cat1.introduce2() #相当于 cat1.intraduce2(cat1)
cat2.introduce2()
cat3.introduce2()

