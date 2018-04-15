#coding=utf-8
'''
本学习内容来自 http://cs231n.github.io 
python／Numpy Tutorial
'''
#举例python的快速排序

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) // 2]  #//返回商 相当于对折取中间那个数
    left=[x for x in arr if x< pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,21,-13,1]))
