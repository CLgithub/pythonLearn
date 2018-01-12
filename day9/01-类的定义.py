#conding=utf-8
'''
定义一个类
class 类名:
    属性
    方法
    def 方法名(self):
        方法体
根据类创建对象
类名()

'''

#定义一个类Cat
class Cat:
    name="tom"
    def eat(self):
        print("🐱在吃🐟")
    def drink(self):
        print("🐱在和🍶")
    def introduce(self):
        #print("%s的年龄是%d"%(Cat.name,cat1.age))
        print("%s的年龄是%d,Cat的age=%d"%(Cat.name,cat1.age,Cat.age))

#创建一个对象
cat1=Cat()
cat2=Cat()
cat1.age=19 #给cat1添加属性
cat2.age=20 #给cat2添加属性
Cat.age=21 #给Cat添加属性
Cat.a="a"  #给Cat添加属性
#print("%s的年龄是%d"%(cat1.name,cat1.age))
cat1.eat()
cat1.introduce()
cat2.introduce()
print(cat2.a)

