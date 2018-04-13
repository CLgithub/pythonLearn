#condig=utf-8
'''
模块中的all定义了其他模块通过from x import ＊调用该模块时所能使用的功能
'''
__all__=["test1","Test"]

def test1():
	print("----test1----")
def test2():
	print("----test2----")
def test3():
	print("----test3----")
num=100
class Test(object):
	pass


if "__main__"==__name__:
 	test1()
