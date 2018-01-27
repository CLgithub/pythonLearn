#coding=utf-8
'''
异常处理格式：
try:
    可能跑出异常的代码。。。
    。。。
except 异常类型:
    异常处理代码。。。

java格式：
try{
    可能跑出异常的代码。。。
    。。。
}catch(异常类型Exception e){
    异常处理代码。。。
}finally{
}
'''
try:
    print(a)
except NameError: #except（除非），异常名称:NameError
    print("出现NameError异常，对异常进行处理")
