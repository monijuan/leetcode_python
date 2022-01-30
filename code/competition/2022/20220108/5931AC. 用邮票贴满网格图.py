# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 22:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5931AC. 用邮票贴满网格图.py
# @Software: PyCharm 
# ===================================
"""
User Accepted:71
User Tried:236
Total Accepted:74
Total Submissions:450
Difficulty:Hard
给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

覆盖所有 空 格子。
不覆盖任何 被占据 的格子。
我们可以放入任意数目的邮票。
邮票可以相互有 重叠 部分。
邮票不允许 旋转 。
邮票必须完全在矩阵 内 。
如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。



示例 1：



输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
输出：true
解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
示例 2：



输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2
输出：false
解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。


提示：

m == grid.length
n == grid[r].length
1 <= m, n <= 105
1 <= m * n <= 2 * 105
grid[r][c] 要么是 0 ，要么是 1 。
1 <= stampHeight, stampWidth <= 105
"""
from leetcode_python.utils import *

class Solution_大佬:
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