#coding=utf-8
'''
不定长参数
  定义一个函数时，其形式参数前添加个“×”，便可将该参数定义为不定长参数，（一个元组）
  不定长参数只能放在最后一个位置
  注意：使用不定长参数的时候不需要带*
  如果一个元组只有一个元素,(33,)需要多加一个都好
'''
#定义一个带有不定长参数的函数
def func1(a,b,*args):
    print("-"*30)
    print(a)
    print(b)
    print(args)

#func1(11,22,33,44,55,66)
#func1(11,22,33)
#func1(11,22)

#定义一个函数,计算所以输出数值的和
def getSum1(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


s=getSum1(2,3,5,1)
print(s)
