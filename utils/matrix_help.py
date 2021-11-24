# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 16:27
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : matrix_help.py
# @Software: PyCharm
# ===================================
from functools import lru_cache

class Solution:
    def __init__(self,matrix):
        self.height,self.width = len(matrix), len(matrix[0])

    @lru_cache(None)
    def next(self,rowid,colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res