#coding=utf-8
'''
匿名函数
  定义
  lambda 参数:函数体
'''
#定义一个匿名函数
lam1=lambda x,y:x+y #匿名函数函数体不需要写return
#调用匿名函数
a=lam1(3,4)
print(a)

lam2=lambda x:print(x)#python2中不能写print，只能写表达式
b=lam2(4)
