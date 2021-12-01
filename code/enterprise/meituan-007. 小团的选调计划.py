# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 9:22
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-007. 小团的选调计划.py
# @Software: PyCharm
# ===================================
"""
"""

num = int(input())
res = []
expects = []
flags = [1]+[0]*num
while num:
    expects.append(list(map(int,input().split())))
    num-=1
for expect in expects:
    for e in expect:
        if not flags[e]:
            res.append(e)
            flags[e]=1
            break
for r in res:print(r,end=' ')