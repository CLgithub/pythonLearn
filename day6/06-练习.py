#coding=utf-8

i=input("请输入一个阿拉伯数字:")
d=("零","一","二","三","四","五","六","七","八","九")

for temp in i:
    #print(d[temp],end="")
    print(d[int(temp)],end="")
else:
    print()
