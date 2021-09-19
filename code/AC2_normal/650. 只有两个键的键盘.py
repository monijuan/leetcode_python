# -*- coding: utf-8 -*-
# @Time    : 2021/9/19 11:11
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 650. 只有两个键的键盘.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def minSteps(self, n: int) -> int:
        if n==1:return 0
        elif n<6:return n
        for factor in range(2,int(n**0.5)+1):
            if n%factor==0:
                return factor+self.minSteps(n//factor)
        return n


def test(data_test):
    s = Solution()
    return s.minSteps(*data_test)


def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [1],
        [2],
        [3],
        [7],
        [10],
        [100],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')