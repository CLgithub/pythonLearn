#计算一个数的结成阶乘
i=int(input("请输入一个数："))


def func1(i):
    c=1
    if i<=2&i!=0:
        return i
    elif i==0:
        return 1
    else:
        c=i*func1(i-1)
        # 5*func1(4)---->5*4*func1(3)---->5*4*3*func1(2)---->5*4*3*2
    return c

print(func1(i))
