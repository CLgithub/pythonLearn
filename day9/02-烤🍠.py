#inding=utf-8

class Hongs:
    def __init__(self):
        self.s="生"
        self.k=0
        self.t=[]

    def __str__(self):
        return "🍠 当前状态%s,%s"%(self.s,str(self.t))
         

    def kao(self,k):
        self.k+=k
        if self.k<3:
            self.s="生"
        elif self.k>=3 and self.k<5:
            self.s="熟了" 
        elif self.k>=5:
            self.s="糊了"
    def addt(self,t):
        self.t.append(t)


h=Hongs()
h.addt("胡椒")
h.addt("盐")
h.kao(1)
print(h)
