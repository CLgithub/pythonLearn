#coding=utf-8

def test(b):
    b=b+b  # 将b指向一个新的值
    #b+=b    # 直接修改b所自相的地址的内容
    print("%s"%b)

#a=100
a=[100]
test(a)
print("a=%s"%a)
