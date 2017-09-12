#coding=utf-8
'''
不定长参数
  定义一个函数时，其形式参数前添加个“*”，便可将该参数定义为不定长参数，（一个元组）
  不定长参数只能放在最后一个位置
  注意：使用不定长参数的时候不需要带*
  如果一个元组只有一个元素,(33,)需要多加一个逗号

  不定长参数分为两种：*args,接收一个元组或列表，**kwargs，接收一个字典
    若定义中只有*args，*args只能放到最后，多余的参数都会封装到里面，或者传递一个列表或元组，并且使用*list 对列表或元组进行拆包
    若定义中只有**kwargs，**kwargs也只能放最后，只能接收带key的参数，或者传递一个字典，并且使用**dict 对字典进行拆包
    若定义中两种都有时：**kwargs放在最后
'''
#定义一个带有不定长参数的函数
def func1(a,b,*args):
    print(a)
    print(b)
    print(args)

#func1(11,22,33,44,55,66)
func1(11,22,33,44)
#func1(11,22,33)
#func1(11,22)

print("-"*30)
#定义一个函数,计算所以输出数值的和
def getSum1(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


s=getSum1(3,5,1)
print(s)

print("-"*30)
def func2(a,b,*kwargs,**args):
    print(a)
    print(b)
    print(args)
    print(kwargs)
func2(11,22,33,44)
