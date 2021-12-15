# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 8:49
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 851. 喧闹和富有.py
# @Software: PyCharm
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        richer_dict = defaultdict(set)
        for a,b in richer:
            richer_dict[b].add(a)
        for i,j in product(range(length),repeat=2):
            if j in richer_dict[i]: richer_dict[i] |= richer_dict[j]
        # print(richer_dict)
        res = []
        for p in range(length):
            minid,minq = p,quiet[p]
            for r in richer_dict[p]:
                if quiet[r]<minq:
                    minid = r
                    minq=quiet[r]
            res.append(minid)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.loudAndRich(*data)


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
        [[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
