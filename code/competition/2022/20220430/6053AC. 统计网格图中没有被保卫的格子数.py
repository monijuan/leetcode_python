# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 21:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6053AC. 统计网格图中没有被保卫的格子数.py
# @Software: PyCharm 
# ===================================
"""给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，其中 guards[i] = [rowi, coli] 且 walls[j] = [rowj, colj] ，分别表示第 i 个警卫和第 j 座墙所在的位置。

一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。

请你返回空格子中，有多少个格子是 没被保卫 的。



示例 1：



输入：m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
输出：7
解释：上图中，被保卫和没有被保卫的格子分别用红色和绿色表示。
总共有 7 个没有被保卫的格子，所以我们返回 7 。
示例 2：



输入：m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
输出：4
解释：上图中，没有被保卫的格子用绿色表示。
总共有 4 个没有被保卫的格子，所以我们返回 4 。


提示：

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
guards 和 walls 中所有位置 互不相同 。
"""
from leetcode_python.utils import *


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(m)]
        stop = [[1] * n for _ in range(m)]
        for x, y in guards + walls:
            grid[x][y] = 0
            stop[x][y] = 0

        for x, y in guards:
            x_ = x
            y_ = y + 1
            while y_ < n and stop[x_][y_]:
                grid[x_][y_] = 0
                y_ += 1
            y_ = y - 1
            while y_ >= 0 and stop[x_][y_]:
                grid[x_][y_] = 0
                y_ -= 1

            y_ = y
            x_ = x + 1
            while x_ < m and stop[x_][y_]:
                grid[x_][y_] = 0
                x_ += 1
            x_ = x - 1
            while x_ >= 0 and stop[x_][y_]:
                grid[x_][y_] = 0
                x_ -= 1
        # for l in stop:
        #     print(l)
        #
        # print()
        # for l in grid:
        #     print(l)
        return sum(sum(line) for line in grid)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countUnguarded(*data)


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
        [4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
