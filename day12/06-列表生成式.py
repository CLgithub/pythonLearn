#coding=utf-8
#需求：创建一个列表，里面包含10～27
#方法一
a=[]
i=10
while i<=27:
	a.append(i)
	i+=1
print(a)
print("-"*40)
'''
range 注意下面表达式在2和3中不同表现
在python2中range存在风险，比如range(1,9999999999)
在python3中避免了这个风险,在使用时才真正开辟内存
'''
print("range(10)=%s"%range(10))
print("range(10,15)=%s"%range(10,15))
print("range(10,15,2)=%s"%range(10,15,2))
print("range(-10,-15,-2)=%s"%range(-10,-15,-2))
print("range(15,10,-2)=%s"%range(15,10,-2))
a=range(1,9999999999)
print(a[2])
#方法二 考研使用列表生存式 range
print("-"*40)
a=[]
for i in range(10,28):  #range 系列，种类
	a.append(i)
print(a)
# 简单写法
a=[]
a=[i for i in range(10,28)] #构建好列表生成式去遍历出每一个i，赋值给i
print(a)

#变换
print("-"*40)
a=[]
a=[i for i in range(10,28,2)]
print(a)

print("-----------------变换----------------")
#变换
print("-"*40)
a=[]
a=[i for i in range(10,28) if True]  #执行前要判断后面是非是true
print(a)

#变换
print("-"*40)
a=[]
a=[i for i in range(10,28) if i%2==0]
print(a)

#变换
print("-"*40)
a=[]
a=[i for i in range(10,28) if []] #只要满足后面的条件，就执行生成
print(a)

#变换
print("-"*40)
a=[]
a=[i for i in range(10,28) for j in range(2)] #每生成前，就要先判断后面是非true
print(a)

#变换
print("-"*40)
a=[]
a=[(i,j) for i in range(10,28) for j in range(2)] 
print(a)

#变换
print("-"*40)
a=[]
a=[(i,j,k) for i in range(5) for j in range(5) for k in range(5)] #其实是for循环♻️ 的嵌套
print(a)


