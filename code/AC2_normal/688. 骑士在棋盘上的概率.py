# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 21:40
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 688. 骑士在棋盘上的概率.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        lastdp = [[1]*n for _ in range(n)]
        while k:
            k-=1
            dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            dp[i][j] += lastdp[ni][nj] / 8
            lastdp = dp
        return lastdp[row][column]


        return dp[k][row][column]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.knightProbability(*data)


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
        [3,2,0,0],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

