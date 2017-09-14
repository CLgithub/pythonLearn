#对元素为字典的列表进行排序

stus=[{"name":"aa","age":18},{"name":"bb","age":20},{"name":"cc","age":19}]
x=[11,22,33,12,43,32]

print(x)
x.sort(key=lambda xn:xn) #sort(key=func)func为一个函数，每次比较时都会调用这个函数，把x的每个元素当成一个参数传递给这个函数，并且函数有返回
print(x)
#print(stus[0]["name"])
stus.sort(key=lambda s:s["age"])
print(stus)


