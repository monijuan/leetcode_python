# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 9:22
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 2132. 用邮票贴满网格图.py
# @Software: PyCharm
# ===================================
"""给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

覆盖所有 空 格子。
不覆盖任何 被占据 的格子。
我们可以放入任意数目的邮票。
邮票可以相互有 重叠 部分。
邮票不允许 旋转 。
邮票必须完全在矩阵 内 。
如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。

 

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
grid[r][c] 要么是 0 ，要么是 1 。
1 <= stampHeight, stampWidth <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stamping-the-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class pre_前缀和:
    def __init__(self, A):
        """ 前缀和 pre[r][c] == sum(A[:r, :c]) """
        height,width = len(A), len(A[0])
        pre = [[0]*(width+1) for _ in range(height+1)]
        for r in range(height):
            for c in range(width):
                pre[r+1][c+1] = A[r][c] + pre[r][c+1] + pre[r+1][c] - pre[r][c]
        self.pre = pre

    def sum_rcrc(self, r0, c0, r1, c1):
        """ 区域求和 sum(A[r0:r1+1, c0:c1+1]) """
        # assert 0<=r0<=r1<m, 0<=c0<=c1<n
        return self.pre[r1+1][c1+1] - self.pre[r1+1][c0] - self.pre[r0][c1+1] + self.pre[r0][c0]

class Solution:
    def possibleToStamp(self, A: List[List[int]], sh: int, sw: int) -> bool:
        m,n=len(A),len(A[0])
        preA = pre_前缀和(A)
        B = [[0]*n for _ in range(m)]
        for r in range(m-sh+1):
            for c in range(n-sw+1):
                if preA.sum_rcrc(r,c,r+sh-1,c+sw-1) == 0:
                    B[r][c] = 1
        preB = pre_前缀和(B)
        for r in range(m):
            for c in range(n):
                if A[r][c] == 0 and preB.sum_rcrc(max(0,r-sh+1),max(0, c-sw+1),r,c)==0:
                    return False
        return True

class Solution_前缀和加二维差分:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        height, width = len(grid), len(grid[0])
        sum = [[0] * (width + 1) for _ in range(height + 1)]
        diff = [[0] * (width + 1) for _ in range(height + 1)]

        # 二维前缀和
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                sum[i + 1][j + 1] = sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + v

        # 更新二维差分
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    x, y = i + stampHeight, j + stampWidth  # 注意这是矩形右下角横纵坐标都 +1 后的位置
                    if x <= height and y <= width and sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j] == 0:
                        diff[i][j] += 1
                        diff[i][y] -= 1
                        diff[x][j] -= 1
                        diff[x][y] += 1

        # 用滚动数组还原二维差分矩阵对应的计数矩阵
        cnt, pre = [0] * (width + 1), [0] * (width + 1)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                cnt[j + 1] = cnt[j] + pre[j + 1] - pre[j] + diff[i][j]
                if cnt[j + 1] == 0 and v == 0:
                    return False
            cnt, pre = pre, cnt
        return True

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
