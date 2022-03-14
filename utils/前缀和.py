# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 9:51
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 前缀和.py
# @Software: PyCharm
# ===================================
from leetcode_python.utils import *

class pre_二维前缀和:
    def __init__(self, grid):
        """ 前缀和 pre[r][c] == sum(grid[:r, :c]) """
        height,width = len(grid), len(grid[0])
        pre = [[0]*(width+1) for _ in range(height+1)]
        for r in range(height):
            for c in range(width):
                pre[r+1][c+1] = grid[r][c] + pre[r][c+1] + pre[r+1][c] - pre[r][c]
        self.pre = pre

    def sum_rcrc(self, r0, c0, r1, c1):
        """ 区域求和 sum(A[r0:r1+1, c0:c1+1]) """
        # assert 0<=r0<=r1<m, 0<=c0<=c1<n
        return self.pre[r1+1][c1+1] - self.pre[r1+1][c0] - self.pre[r0][c1+1] + self.pre[r0][c0]

class Solution:
    def possibleToStamp(self, A: List[List[int]], sh: int, sw: int) -> bool:
        m,n=len(A),len(A[0])
        preA = pre_二维前缀和(A)
        B = [[0]*n for _ in range(m)]
        for r in range(m-sh+1):
            for c in range(n-sw+1):
                if preA.sum_rcrc(r,c,r+sh-1,c+sw-1) == 0:
                    B[r][c] = 1
        preB = pre_二维前缀和(B)
        for r in range(m):
            for c in range(n):
                if A[r][c] == 0 and preB.sum_rcrc(max(0,r-sh+1),max(0, c-sw+1),r,c)==0:
                    return False
        return True