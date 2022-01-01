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

# a,b = 12,-18
a,b = map(int,input().split())
res1 = max(0,a,b)
res2 = max(0,a+b)
print(res1,res2)
if res1==res2==0:print('-_-')
elif min(a,b)>0:print('^_^')
else :'T_T'
