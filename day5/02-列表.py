#incding=utf-8
'''
列表
 定义列表
 可以放多种数据类型
'''
names=["a1","a2",123]
print("names=%s"%names)
'''
列表的增删改查
增：
  list.append("a") 在list最后增加a
  list.insert(2,'a')在list的指定位置插入a
  list1+=list2 list2合并到list1 等同于 list1.extend(list2)
删除：
  list.pop() 从list中删除最后一个元素，并返回该元素
  list.remove("a") 从list中删除遇到的第一个a元素
  del list[1] 从list中删除第1个元素
'''
#增加
print("------添加-----------------")
names.append("append")#添加到列表最后
print(names)
names.insert(1,"insert")#指定位置添加
print(names)
names2=["b1",'b2']
print("names2=%s"%names2)
#names.append(names2)
print("names=%s"%names)
names+=names2#两个列表直接添加
print("names=%s"%names)
names.extend(names2)#第3种添加方式
print("names=%s"%names)
#删除
print("------删除-----------------")
p1=names.pop()#删除最后一个元素,并返回被删除的元素
print("被删除的元素：%s"%p1)
print("names=%s"%names)
print("names.remove('b1')删除第一个b1")
names.remove("b1")#删除第一个b1
print("names=%s"%names)
del names[2]#删除names的第1个元素
print("names=%s"%names)

#修改
print("------修改-----------------")
names[0]="names0"
print("names=%s"%names)

#查
print("------查询-----------------")
if 'names0' in names:
    print("name0在names中")
if 'names1' not in names:
    print("name1不在names中")
