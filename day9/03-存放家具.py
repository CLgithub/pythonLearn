#coding=utf8

#定义一个房子🏠 类
class Home:
    def __init__(self, area, info, addr):
        self.area=area
        self.leftArea=self.area
        self.info=info
        self.addr=addr
        self.item=[]
    def __str__(self):
        return "房子🏠 的总面积是：%d，可用面积面积是：%d，户型：%s，地址：%s，有家具：%s"%(self.area,self.leftArea,self.info,self.addr,str(self.item))
    def addItem(self, item):
       # self.item.append(item.name)
       # self.leftArea-=item.area
        self.item.append(item.getName())
        self.leftArea-=item.getArea()

#定义一个床类
class Bad:
    def __init__(self, name, area):
        self.name=name
        self.area=area
    def __str__(self):
        return "%s占用的面积是%d"%(self.name,self.area)
    def getName(self):
        return self.name
    def getArea(self):
        return self.area


fangzi=Home(129, "三室一厅", "深圳市罗湖区")

bad1=Bad("标准床",4)
bad2=Bad("小床",3)

fangzi.addItem(bad1)
fangzi.addItem(bad2)

print(fangzi)
