#想设计一个会根据反馈结果改变自己的程序，还没想清楚

x=7
y=0

def test1(a,func):
    x=func(a)
    return x

while x!=y:
    if y>x:
        y=test1(y,lambda a:a-1)
    elif y<x:
        y=test1(y,lambda a:a+1)
print(y)

