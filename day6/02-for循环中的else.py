#coding=utf-8
names = [11,22,33,44,55]
print(names)
i=int(input("请数据值:"))
for name in names:
    if i==name:
        print("%d在列表names中"%i)
        break #当跳出后，就跳出for循环，else也不执行
else: #当for循环♻️执行完成后执行eles     
    print("%d不在列表names中"%i)
'''
for else 结合break使用是个不错的设计
java中没有，在判断一个集合中是非有某变量时，不需要定义一个booble,在找到后设置booble=true来帮助判断
而是直接找到后就执行找到后的业务，然后break 跳出，跳出后else就不执行，否则说明没有找到，就执行else没有找到的业务

'''
