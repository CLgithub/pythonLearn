#coding=utf-8
'''
import 模块名称  #会先搜索当前路径是非有改模块，如果没有在python库中去找，知道找到然后引用进来为止，否则报错，模块名称.__file__可以的到模块所在路径,引入模块时会把模块执行一遍
模块可以通过python的包管理器来安装，pip支持uninstall，pip install pygame

模块被引用后，会在模块所在目录产生一个__pycache__文件夹，换成模块的字节码，改字节码命名规则：模块名称-cpython-python版本.pyc    
cpython 代表使用c写的pythone解释器

'''
import os
import pygame as pg #可以使用as给模块取别名
#import mk    #第一种导入方式 建议使用第一种，比较两个模块直接有相同的方法名时后面导入的模块顶替前面导入的模块
#from mk import run,test2 #第二种导入方式
from mk import *       #第三种导入方式
import mk2 

print(os.__file__)
print(pg.__file__)
#print(mk.__file__)
#mk.run()
run()
test2()
mk2.test2()
