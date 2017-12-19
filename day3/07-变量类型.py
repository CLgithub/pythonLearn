#coding=utf-8
'''
python 是弱类型

数值：int long float complex
布尔：true false
字符：String
列表：List
元组：Tuple
字典：Dictionary

type(a)可以得到a的数据类型

'''
a = input("请输入数字，判断是否大于20:") #3中的input得到的是字符串 a="13"
x=int(a)  #将a转换为int类型赋值给x
if x>20:
    print("%d大于20"%x)
    print("aaaa")
else:
    print("%d小于20"%x)
    print("%d小于20"%x)
print("aaaa")
