#coding=utf-8


def func1(n):
    if n>1:
        return n*func1(n-1) # return 4*func1(3)=4*3*func1(2)=4*3*2*func1(1)
    else:
        return 1

n=int(input("请输入一个数字："))
print(func1(n))
