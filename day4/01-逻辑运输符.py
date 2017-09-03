#coding=utf-8
var1=True
var2=False
if var1 or var2: 
    print("var1 or var2")
if var1 and var2:
    print("var1 and var2")
if not(var1 and var2):
    print("not(var1 and var2)")

if var1 and var2:
    print("a")
elif True:
    print("b")
