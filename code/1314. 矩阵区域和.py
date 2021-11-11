# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 17:19
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1314. 矩阵区域和.py
# @Software: PyCharm
# ===================================
"""给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - k <= r <= i + k,
j - k <= c <= j + k 且
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-block-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np

from leetcode_python.utils import *
from scipy import signal

class Solution:
    def __init__(self):
        pass

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        data = np.array(mat)
        print(data)
        nurcle = np.ones((1+k*2,1+k*2))
        print(nurcle)
        res = signal.convolve2d(data, nurcle).astype(np.uint8)
        # res = signal.convolve2d(data, nurcle, 'same').astype(np.uint8)
        print(res)
        return res.tolist()


def test(data_test):
    s = Solution()
    return s.matrixBlockSum(*data_test)


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
        # [[[1,2,3],[4,5,6],[7,8,9]],2],
        [[[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]],3],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
