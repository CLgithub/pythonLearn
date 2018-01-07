#coding=utf-8
'''
给定一个字符串aStr，返回使用空格或者‘\t’分割后的倒数第二个子串
'''
aStr="haha nihao a \t heihei \t  woshi nide \t hao \npengyou"
print("aStr=%s"%aStr)

print("aStr.split()=%s"%aStr.split())
print("".join(aStr.split()))

