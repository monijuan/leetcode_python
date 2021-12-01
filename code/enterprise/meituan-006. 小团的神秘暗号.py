# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 14:54
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-006. 小团的神秘暗号.py
# @Software: PyCharm
# ===================================
"""
"""

def wrong():
    length = int(input())
    mima = list(input())
    try:
        left = mima.index('T',mima.index('M'))
        right = mima[::-1].index('T',mima[::-1].index('M'))
        if left+1<=length-right+1:
            print(''.join(mima[left+1:length-right+1]))
        else:
            print()
    except Exception as e:
        print()


def ac():
    n = int(input())
    s = input()
    l,r = 0,n-1
    while l < n and s[l] != 'M': l += 1
    while l < n and s[l] != 'T': l += 1
    while 0 < r and s[r] != 'T': r -= 1
    while 0 < r and s[r] != 'M': r -= 1
    print(s[l+1:r])

