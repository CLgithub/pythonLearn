#coding=utf-8
'''
异常处理格式：
try:
    可能跑出异常的代码。。。
    。。。
except (异常类型1,异常类型2) as e:
    异常处理代码。。。
else:
    没有异常才会执行
finally:
    不管有没有异常都会执行

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
    1/0
    #print(a)
    #open("a.txt")
    print("-----1-----")
except (FileNotFoundError,NameError) as e: #except（除非），异常类型:NameError
    print("出现NameError异常，对异常进行处理",end="")
    print("或出现FileNotFoundError异常，对异常进行处理")
    print(e)
except (Exception) as e:
    print("全部的异常都可以用这个来捕获%s"%e)
else:
    print("没有异常才会执行")
finally:
    print("不管有没有异常都执行")
print("-----2-----")
