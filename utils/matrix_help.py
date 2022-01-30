# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 16:27
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : matrix_help.py
# @Software: PyCharm
# ===================================
from functools import lru_cache
from typing import List

class Solution:
    def __init__(self,matrix):
        self.height,self.width = len(matrix), len(matrix[0])
        pass

    @lru_cache(None)
    def next(self,rowid,colid):
        res = []
        for i, j in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= i < self.height and 0 <= j < self.width:
                res.append([i, j])
        return res


    def dfs(self,r,c):
        self.grid[r][c]=0
        for nextr,nextc in self.next(r,c):
            if self.grid[nextr][nextc]=='1':
                self.dfs(nextr,nextc)

    def cntConnections(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.height,self.width = len(grid),len(grid[0])
        res = 0
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c]=='1':
                    res+=1
                    self.dfs(r,c)
        return res