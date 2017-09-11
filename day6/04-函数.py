#coding=utf-8
'''
函数
  函数的定义:
  def funcName():
    funBody

'''
#定义一个无参数无返回值的函数func1()
def func1():
    print("执行...")
    print("函数体...")

#定义一个有参数无返回值的函数faddFunc()
def addFunc(i,j):
    print("%d+%d=%d"%(i,j,i+j))

#定义一个有参数有返回值的函数faddFunc2()
def addFunc2(i,j):
    sum1=i+j
    return sum1

#定义一个有参数有多个返回值的函数fun4()
def func4(i,j):
    sum1=i+j
    #第一种方式：使用列表或元组封装多个参数，一起返回
    a=[i,j,sum1]
    b=(i,j,sum1)
    #return b
    #第二种方式：直接写，其实默认相对应封装成元组返回
    return i,j,sum1

#定义一个带有缺省参数的函数，j=3
def func5(i,j=3):
    sum1=i+j
    return sum1

#调用函数fun1()
#func1()
#addFunc(3,2)

#sum1=addFunc2(2,5)
#print("调用函数addFunc2(2,5)得到返回值=%s"%sum1)

i,j,sum1=func4(2,5)
print("i=%d,j=%d,i+j=%d"%(i,j,i+j))

#调用缺省参数的函数
print(func5(2))
