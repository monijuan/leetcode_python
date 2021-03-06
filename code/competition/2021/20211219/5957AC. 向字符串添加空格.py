# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5957AC. 向字符串添加空格.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces.insert(0,0)
        spaces.append(len(s))
        for spid in range(1,len(spaces)):
            res.append(s[spaces[spid-1]:spaces[spid]])
        return ' '.join(res)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')