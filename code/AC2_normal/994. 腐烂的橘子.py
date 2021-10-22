# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 13:56
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 994. 腐烂的橘子.py
# @Software: PyCharm
# ===================================
"""在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

 

示例 1：



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def next(self,rowid,colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res


    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.height,self.width = len(grid),len(grid[0])
        queue = []  # row,col,time

        # 烂橘子作为bfs的起点
        for row_id,line in enumerate(grid):
            for col_id,num in enumerate(line):
                if 2==num:
                    queue.append([row_id,col_id,0])

        # bfs
        times = 0
        while queue:
            row_id, col_id, times = queue.pop(0)
            for row_id, col_id in self.next(row_id, col_id):
                if grid[row_id][col_id]==1:
                    grid[row_id][col_id] = 2
                    queue.append((row_id, col_id,times+1))

        for row_id,line in enumerate(grid):
            for col_id,num in enumerate(line):
                if 1==num:
                    return -1
        return times


def test(data_test):
    s = Solution()
    return s.orangesRotting(*data_test)


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
