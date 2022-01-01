# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 23:49
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 001.py
# @Software: PyCharm 
# ===================================
"""
"""
A=input()
B=input()
A = [int(x)for x in A[::-1]]
B = [int(x)for x in B[::-1]]
res = 0
for i,(a,b) in enumerate(zip(A,B)):
    if a>=b:continue
    elif a==-1:
        A[i+1]-=1
    else:
        res+=1
        A[i+1]-=1
print(res)


