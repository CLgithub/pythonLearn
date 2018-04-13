#coding=utf-8
'''
给程序传参数，不用等程序运行时再传參，可以才程序运行前就传參，例如 python3 setup.py install
实现方式：
	1.导入sys模块
'''
import sys
#arg="abc"
#print(sys.argv)
print("程序%s共收到%d个参数，分别是："%(sys.argv[0],len(sys.argv)-1),end="")
for agr in sys.argv[1:]:
    print("%s,"%agr,end="")
print("")
