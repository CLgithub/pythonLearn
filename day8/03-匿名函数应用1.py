#匿名函数的应用

#定义一个函数func1,将a与b交给函数func，并把func的返回值+1然后返回
def func1(a,b,func):    #func是一个函数，把这个函数当中一个参数给func1
    return func(a,b)+1

#定义一个函数func2,完成两个数i相加
def func2(a,b):
    return a+b

x=func1(2,3,func2)#把函数func2当中一个参数传递给func1
print(x)

x=func1(2,3,lambda a,b:a-b)#直接定义一个匿名函数当中参数
print(x)

x=func1(2,3,lambda a,b:a*b)
print(x)

x=func1(2,3,lambda a,b:a/b)
print(x)

pStr=input("请输入一个匿名函数：")
p=eval(pStr)#eval可以将字符串转换为python表达式

x=func1(2,3,p)
print(x)
