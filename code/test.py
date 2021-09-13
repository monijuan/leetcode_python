# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 16:01
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : test.py
# @Software: PyCharm
# ===================================
from leetcode_python.utils import *

def test():
    print(2**10)

def test4():
    chars = '()*'

    length = 100
    times = 10
    while times:
        times-=1
        str = ''
        for x in range(length):
            str+=chars[random.randint(0, 2)]
        print(f'"{str}"')


def test3():
    n=10

    for i in range(n):
        print('-'*50)
        print(f'i={i}')
        times = 0
        for w in range(1,n,2):
            time = min(i+1,n-i,w,(n-1)//2)
            times+=time
            print(f'i:{i}, w:{w}, time:{time}')
        print(f'[res]n:{n}, i:{i}, times:{times}')

def test2():
    res = 11 & 1
    res = 12 & 1
    print(res)

def test1():
    for x in range(50000,50200):
        print(f'[{x}],',end='')
    print()
    for x in range(50000,50200):
        print(f',"addNum"',end='')
    return


if __name__ == '__main__':
    test()
