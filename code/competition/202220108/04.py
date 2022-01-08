# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 22:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 04.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        N = len(grid)
        M = len(grid[0])
        dp = [[0] * M for _ in range(N)]
        for i, r in enumerate(grid):
            for j in range(M - 1, -1, -1):
                if r[j]:
                    dp[i][j] = 0
                else:
                    if j == M - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j + 1] + 1
        for i in range(N - 1, -1, -1):
            for j in range(M):
                if dp[i][j] >= stampWidth:
                    if i == N - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j] + 1
                else:
                    dp[i][j] = 0
        for i in range(N):
            j_limit = -1
            for j in range(M):
                if dp[i][j] >= stampHeight:
                    j_limit = j + stampWidth
                dp[i][j] = (j < j_limit)
        for j in range(M):
            i_limit = -1
            for i in range(N):
                if dp[i][j]:
                    i_limit = i + stampHeight
                dp[i][j] = (i < i_limit)
        for i in range(N):
            for j in range(M):
                if not grid[i][j] and not dp[i][j]:
                    return False
        return True

class Solution:
    def checkwidth(self,heights)->bool:
        # line = ['1' if x>0 else ' ' for x in heights]
        # return not all([0<len(w)<self.stampWidth for w in ''.join(line).split(' ')])

        line = ['1' if x>0 else ' ' for x in heights]
        s = ''.join(line)
        for w in s.split(' '):
            if 0<len(w)<self.stampWidth:return False
        return True

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        for g in grid:print(g)
        self.m,self.n = len(grid),len(grid[0])
        if stampHeight==1 and stampWidth==1:return True
        self.stampWidth = stampWidth
        heights = [0]*self.n
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]==0: heights[j]+=1
                else: 
                    if 0<heights[j]<stampHeight:return False
                    heights[j]=0
            if not self.checkwidth(heights):return False
        for h in heights:
            if 0<h<stampHeight:return False
        return True


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.possibleToStamp(*data)


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
        # [[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],4,3],#True
        # [[[1,1,1,1,1,0],[1,0,0,1,0,0],[1,1,0,1,1,0],[1,0,0,1,0,0],[1,0,1,0,1,0],[1,1,1,0,1,1],[0,0,1,0,0,0],[0,0,1,1,0,0]],5,1],
        # [[[1],[1],[0],[0]],3,1],
        # [[[1],[1],[0],[0]],1,3],
        # [[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]],9,4],
        # [[[1]],1,4],
        # [[[0,0],[0,1]],1,1],
        [[[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,1,1]],2,2],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')