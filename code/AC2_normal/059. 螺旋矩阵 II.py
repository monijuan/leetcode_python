# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 10:52
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 059. 螺旋矩阵 II.py
# @Software: PyCharm
# ===================================
"""给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np

from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def __next(self,i,j):
        if i <= self.mid and i-1<= j <self.length-i-1:
            res = [i, j + 1]
        elif j>=self.mid and self.length-j-1<=i<j:# 向下
            res = [i + 1, j]
        elif i >= self.mid and self.length - i <= j <= i:#向左
            res = [i, j - 1]
        elif j<self.mid and j<=i<=self.length-j:# 向上
            res = [i - 1, j]
        else:# 结束
            res = [-1,-1]
        return res

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.length = n
        self.mid = n//2
        res = [[0]*n for _ in range(n)]
        i=j=index=0
        while index<n*n:
            index+=1
            res[i][j] = index
            i,j = self.__next(i,j)
            # print(np.array(res))
        return res


def test(data_test):
    s = Solution()
    return s.generateMatrix(*data_test)


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
        [5],
        [4],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
