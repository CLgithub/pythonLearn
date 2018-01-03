#coding=utf-8
'''
常用字符串操作
    1
'''
str1="a12345 789abcdef abc a"
print("str=%s"%str1)
print("-"*30)
# 查找
#1 str.find("a")  找到第一个a出现的位置并返回，没有找到就返回-1
#2 str.index("a") 没有找到就会抛异常
#3 str.rfind("a") 从后往前找 返回所在位置
#4 str.rindex("a") 从后往前找,没有找到就会抛异常
print("str1.find(a)=%s"%str1.find("a"))
print("str1.index(c)=%s"%str1.index("c"))
print("str1.rfind(a)=%s"%str1.rfind("a"))
print("str1.rindex(c)=%s"%str1.rindex("c"))

# 统计
#5 str.count("a") 统计str中有多少个a
print("-"*30)
print("str1.count(a)=%s"%str1.count("a"))
print("str1.count(x)=%s"%str1.count("x"))

# 替换
# str.replace("a","b",i) 将str中的a替换成b，替换i次，若不写i，默认全部替换，并返回替换后的字符串
print("-"*30)
print("str1.replace(a,x)=%s"%str1.replace("a","x"))
print("str1.replace(a,x,1)=%s"%str1.replace("a","x",2))

# 切割
# str.split(a) 按a切割str
print("-"*30)
print("str1.split(a)=%s"%str1.split("a"))
#print("str1.partition(a)=%s"%str1.partition(""))

# 首字母大写
print("-"*30)
print("str1.capitalize()=%s"%str1.capitalize())
# 所有单词首字母大写
print("str1.title()=%s"%str1.title())

# 判断是非以某字符串开头或结尾
print("-"*30)
print("str1.startswith(a)=%s"%str1.startswith("a"))
print("str1.endswith(a)=%s"%str1.endswith("a"))

# 将字符串全部切换成大写或小写
print("-"*30)
print("str1.upper()=%s"%str1.upper())
print("str1.upper().lower()=%s"%str1.upper().lower())

# 左右对齐
print("-"*30)
print("str1.ljust(30)|=%s%s"%(str1.ljust(30),"|"))
print("str1.ljust(3)|=%s%s"%(str1.ljust(3),"|"))
print("str1.rjust(30)=%s"%(str1.rjust(30)))
print("str1.rjust(3)=%s"%(str1.rjust(3)))
print("|str1.center(30)|=|%s|"%(str1.center(30)))
str2="ab"
print("|str2.center(3)|=|%s|"%(str2.center(3)))

# 去掉空格
print("-"*30)
print("|str1.center(40).lstrip()|=|%s|"%(str1.center(40).lstrip()))
print("|str1.center(40).rstrip()|=|%s|"%(str1.center(40).rstrip()))
print("|str1.center(40).strip()|=|%s|"%(str1.center(40).strip()))











