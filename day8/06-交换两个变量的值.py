#
a=4
b=5

# 方法1
a=a^b
print(a) #异或是二进制的运算
b=a^b# a^b^b
a=a^b# a^b^a
print(a)
print(b)

# 方法2
a,b=b,a
print(a)
print(b)


'''
print("-"*30)
c="c"
d="d"
c=c^d
d=c^d
c=c^d
print(c)
print(d)
'''
