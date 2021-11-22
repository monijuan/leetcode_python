# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 9:09
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1557. 可以到达所有点的最少点数目.py
# @Software: PyCharm
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        超时case：https://leetcode-cn.com/submissions/detail/240988246/testcase/
        """
        pass

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(range(n))
        for start,end in edges:
            if end in res: res.remove(end)
        return list(res)

    def findSmallestSetOfVertices_超时(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [x for x in range(n)]
        for start,end in edges:
            if end in res: res.remove(end)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.findSmallestSetOfVertices(*data)


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
        [6,[[0,1],[0,2],[2,5],[3,4],[4,2]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
