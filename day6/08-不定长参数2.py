'''

'''
def test(a,b,c=33,*args,**kwargs):
    print("-"*30)
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(11,22,33,44,55)
test(11,22,33,key1=44,key2=55)#一旦传递参数时带有key，那带有key的参数就会交给**kwargs
test(11,22,33,44,45,key1=55,key2=66)#不带key的参数就给不定长参数
#test(11,22,key1=33,44,key3=45,key4=55,key5=66)#会出错 SyntaxError: positional argument follows keyword argument
test(11,22,key1=33,key2=44,key3=45,key4=55,key5=66)

A=(44,55,66)
B={"name":"aa","age":18}
test(11,22,33,A,B)
test(11,22,33,*A,**B)#此处的*代表拆包，将A和B分别拆包，分别交给*args和**kwargs

