#coding=utf-8

a=0
nums=[11,22,33]
def test1():
    a=100 #定义一个局部变量 变量名和全局变量相同
    print(a)
def test2():
    global a#引入全局变量 --global:全部的
    a=200 
    print(a)

    nums.append(44)#当有全局变量的列表元组字典时，可以直接使用，不需要加global

test1()
test2()
print(a)
print(nums)
