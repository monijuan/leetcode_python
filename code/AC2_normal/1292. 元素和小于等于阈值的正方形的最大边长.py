# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 22:37
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1292. 元素和小于等于阈值的正方形的最大边长.py
# @Software: PyCharm 
# ===================================
"""给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
 

示例 1：



输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
示例 2：

输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


def sum_grid二维前缀和(grid):
    """
    sum = grid[x1..x2][y1..y2]
        = res[x2][y2] - res[x1 - 1][y2] - res[x2][y1 - 1] + res[x1 - 1][y1 - 1]
    """
    h, w = len(grid), len(grid[0])
    res = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + grid[i - 1][j - 1]
    return res


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        h, w = len(mat), len(mat[0])
        P = sum_grid二维前缀和(mat)

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        def check(mid):
            return any(getRect(i, j, i + mid - 1, j + mid - 1) <= threshold for i in range(1, h - mid + 2) for j in range(1, w - mid + 2))

        l, r, ans = 1, min(h, w), 0
        while l <= r:
            mid = (l + r) >> 1
            find = check(mid)
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
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
