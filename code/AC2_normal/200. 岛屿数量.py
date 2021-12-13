# -*- coding: utf-8 -*-
# @Time    : 2021/12/13 9:46
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 200. 岛屿数量.py
# @Software: PyCharm
# ===================================
"""给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    @lru_cache(None)
    def next(self,rowid,colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res

    def dfs(self,r,c):
        self.grid[r][c]=0
        for nextr,nextc in self.next(r,c):
            if self.grid[nextr][nextc]=='1':
                self.dfs(nextr,nextc)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.height,self.width = len(grid),len(grid[0])
        res = 0
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c]=='1':
                    res+=1
                    self.dfs(r,c)
        # print(self.grid)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.numIslands(*data)


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
        [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
