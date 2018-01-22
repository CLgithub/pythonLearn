#coding=utf-8
class CarStore(object):
    def selectCar(self,carType):  #工厂方法模式：先在基类里定义流程，不实现方法，在子类里实现方法
        pass
    def order(self, carType):
        return self.selectCar(carType)

class HondaCarStore(CarStore):
    def selectCar(self,carType):
        return HondaCarFactory.selectCarByType(carType)
class BMWCarStore(CarStore):
    def selectCar(self,carType):
        return BMWCarFactory.selectCarByType(carType)

class HondaCarFactory(object):
    #@classmethod
    @staticmethod
    def selectCarByType(carType):
        if carType=="思域":
            return Civic()
        elif carType=="雅阁":
            return Accord()
class BMWCarFactory(object):
    #@classmethod
    @staticmethod
    def selectCarByType(carType):
        if carType=="330":
            pass
        elif carType=="X6":
            return X6()

class Car(object):
    def move(self):
        print("%s🚗 在移动"%self)
    def musice(self):
        print("%s🚗 在放音乐🎵 "%self)
    def stop(self):
        print("%s🚗 在停止"%self)
class HondaCar(Car):
    def feature(self):
        return "发动机很好"
class BMWCar(Car):
    def feature(self):
        return "操控很好"
class Civic(HondaCar):
    def __str__(self):
        return "%s的思域"%self.feature()
class Accord(HondaCar):
    def __str__(self):
        return "%s雅阁"%self.feature()
class X6(BMWCar):
    def __str__(self):
        return "%sX6"%self.feature()

hcarStore=HondaCarStore()
car=hcarStore.order("思域")
car.move()
car.musice()
car.stop()

bMWcarStore=BMWCarStore()
x6car=bMWcarStore.order("X6")
x6car.move()

