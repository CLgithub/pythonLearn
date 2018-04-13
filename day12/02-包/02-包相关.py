#coding=utf-8
'''
定义包：
	建立一个文件夹，文件夹下放入模块，并建立一个文件“__init__.py”，在2中必须要有这个文件才能看成是包，在3中没有这样文件也相当于包
	__init__.py在导入该包时会被调用



当导入该包时，init文件会被执行
'''

import TestMsg
#from TestMsg import *

TestMsg.sendmsg.send("abc")
