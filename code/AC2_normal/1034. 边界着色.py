# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 8:57
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1034. 边界着色.py
# @Software: PyCharm
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        self.height,self.width = len(grid), len(grid[0])
        self.grid = grid
        flag = [[False]*self.width for _ in range(self.height)]
        res = [line.copy() for line in grid]
        old_color = grid[row][col]
        queue = [(row,col)]
        flag[row][col]=True
        while queue:
            row,col = queue.pop(0)
            if grid[row][col] == old_color:
                for r,c in self.next(row,col):
                    if not flag[r][c]:
                        flag[r][c]=True
                        queue.append((r,c))

                if self.isBorder(row,col):
                    res[row][col]=color
        # print('isBorder(1,2)',self.isBorder(1,2))
        return res

    @lru_cache(None)
    def isBorder(self,row,col):
        if row in [0,self.height-1] or col in [0,self.width-1]:return True
        else:
            color = self.grid[row][col]
            # print(row,col,color,[self.grid[r][c] for r,c in self.next(row,col)])
            return any([self.grid[r][c]!=color for r,c in self.next(row,col)])

    @lru_cache(None)
    def next(self,rowid,colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.colorBorder(*data)


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
        # [[[1,2,1],[1,2,2],[2,2,1]],1,1,2],
        [[[1,2,2,2,1],[1,2,2,2,1],[1,2,2,2,1],[1,2,2,2,1],[1,2,1,2,1],[1,2,2,2,1],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[1,2,2,2,1],[1,2,1,2,1]],0,1,3],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
