#coding=utf-8
class HondaCarStore(object):
    def order(self, carType):
        return HondaCar.selectCarByType(carType)

class HondaCar(object):
    def move(self):
        print("%s🚗 在移动"%self)
    def musice(self):
        print("%s🚗 在放音乐🎵 "%self)
    def stop(self):
        print("%s🚗 在停止"%self)
    #@classmethod
    @staticmethod
    def selectCarByType(carType):
        if carType=="思域":
            return Civic()
        elif carType=="雅阁":
            return Accord()
class Civic(HondaCar):
    def __str__(self):
        return "思域"
class Accord(HondaCar):
    def __str__(self):
        return "雅阁"

carStore=HondaCarStore()
car=carStore.order("思域")
car.move()
car.musice()
car.stop()
