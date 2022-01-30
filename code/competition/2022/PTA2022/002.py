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

inputlist = list(map(int,input().split()))
y,n=inputlist.count(1),inputlist.count(0)
if y>n:print('Yes')
elif y<n:print('No')
else:print('Tie')
print(f'{y}:{n}')


