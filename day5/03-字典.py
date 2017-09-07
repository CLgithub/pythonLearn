#coding=utf-8
'''
字典
  相当于java里的map 里面存储的一个元素是一个键值对,而且是无序的map
'''
#定义一个字典
infor={"name":"aa","age":18,"gender":"男"}
print(infor)
print("name=%s age=%d gender=%s"%(infor["name"],infor["age"],infor["gender"]))

'''
字典的增删改查
'''
#增加
infor["address"]="深圳"
print(infor)
#删除
del infor["address"]
print(infor)
#修改
infor["name"]="bb"
print(infor)
#查
gender=infor["gender"]
print(gender)
age=infor.get("age")
print(age)
name=infor.get("name")
print(name)
#思考如何遍历字典,貌似不存在这个问题，因为直接print出来就行，不像java打印出来是个对象
