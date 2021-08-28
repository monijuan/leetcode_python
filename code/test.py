# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 16:01
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : test.py
# @Software: PyCharm
# ===================================

def test():
    for x in range(50000,50200):
        print(f'[{x}],',end='')
    print()
    for x in range(50000,50200):
        print(f',"addNum"',end='')
    return


if __name__ == '__main__':
    test()
