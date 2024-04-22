# -*- coding: utf-8 -*-
# @Time    : 2024/4/22 13:48
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1631. 最小体力消耗路径.py
# @Software: PyCharm
# ===================================
"""你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。



示例 1：



输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
示例 2：



输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
示例 3：


输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。


提示：

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""
from leetcode_python.utils import *


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h, w = len(heights), len(heights[0])
        # rows,columns  = len(heights)
        dp = [[float('-inf') for _ in range(w)] for _ in range(h)]
        # dp[0][0] = 0
        for rid in range(h):
            for cid in range(w):
                if rid == 0 and cid == 0:
                    dp[rid][cid] = 0
                elif rid == 0:
                    ## 第一行，向左max
                    dp[rid][cid] = max(
                        dp[rid][cid - 1],
                        abs(heights[rid][cid] - heights[rid][cid - 1]),
                    )
                elif cid == 0:
                    ## 第一列，向上max
                    dp[rid][cid] = max(
                        dp[rid - 1][cid],
                        abs(heights[rid][cid] - heights[rid - 1][cid]),
                    )
                else:
                    max_left = max(
                        dp[rid][cid - 1],
                        abs(heights[rid][cid] - heights[rid][cid - 1]),
                    )
                    max_up = max(
                        dp[rid - 1][cid],
                        abs(heights[rid][cid] - heights[rid - 1][cid]),
                    )
                    dp[rid][cid] = min(max_up, max_left)
        return dp[-1][-1]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.minimumEffortPath(*data)


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
        [[[1, 2, 2], [3, 8, 2], [5, 3, 5]]],
        [[[1, 2, 3], [3, 8, 4], [5, 3, 5]]],
        [[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
