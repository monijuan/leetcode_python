# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 10:18
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6081. 到达角落需要移除障碍物的最小数目.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的二维整数数组 grid ，数组大小为 m x n 。每个单元格都是两个值之一：

0 表示一个 空 单元格，
1 表示一个可以移除的 障碍物 。
你可以向上、下、左、右移动，从一个空单元格移动到另一个空单元格。

现在你需要从左上角 (0, 0) 移动到右下角 (m - 1, n - 1) ，返回需要移除的障碍物的 最小 数目。



示例 1：



输入：grid = [[0,1,1],[1,1,0],[1,1,0]]
输出：2
解释：可以移除位于 (0, 1) 和 (0, 2) 的障碍物来创建从 (0, 0) 到 (2, 2) 的路径。
可以证明我们至少需要移除两个障碍物，所以返回 2 。
注意，可能存在其他方式来移除 2 个障碍物，创建出可行的路径。
示例 2：



输入：grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
输出：0
解释：不移除任何障碍物就能从 (0, 0) 到 (2, 4) ，所以返回 0 。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] 为 0 或 1
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from leetcode_python.utils import *

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        flights = []
        for i in range(m):
            for j in range(n):
                if i:
                    flights.append([i * n + j, (i - 1) * n + j, grid[i - 1][j]])
                if i < m - 1:
                    flights.append([i * n + j, (i + 1) * n + j, grid[i + 1][j]])
                if j:
                    flights.append([i * n + j, (i) * n + j - 1, grid[i][j - 1]])
                if j < n - 1:
                    flights.append([i * n + j, (i) * n + j + 1, grid[i][j + 1]])

        def findCheapestPrice(flights: List[List[int]], src: int, dst: int, k: int) -> int:
            g = defaultdict(list)
            for u, v, w in flights:
                g[u].append((v, w))
            res = defaultdict(lambda: float('inf'))
            res[(0, 0)] = 0
            q = [(0, 0, src)]
            while q:
                time, step, nownode = heapq.heappop(q)
                if step > k + 1 or time > res[(step, nownode)]:
                    continue
                if nownode == dst:
                    return time
                for v, w in g[nownode]:
                    newtime = w + time
                    if newtime < res[v]:
                        heapq.heappush(q, (newtime, step + 1, v))
                        res[v] = newtime
                # print(res)
            return -1

        return findCheapestPrice(flights, 0, m * n - 1, m + n + 100000)

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.minimumObstacles(*data)


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
        # [[[0,1,1],[1,1,0],[1,1,0]]],
        # [[[0,0,1,1,1,1,0,0,0,1],[0,1,1,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,0],[0,0,1,1,1,1,0,0,1,1],[1,0,1,0,0,0,1,1,1,0]]],
        [[[0,0,1,1,1,1,0,0,0,1],[0,1,1,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,0],[0,0,1,1,1,1,0,0,1,1],[1,0,1,0,0,0,1,1,1,0]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
