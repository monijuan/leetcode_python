# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 17:08
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 329. 矩阵中的最长递增路径.py
# @Software: PyCharm
# ===================================
"""给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

 

示例 1：


输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：


输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：

输入：matrix = [[1]]
输出：1
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np

from leetcode_python.utils import *


class Solution:
    @lru_cache(None)
    def next(self,rowid,colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res

    @lru_cache(None)
    def dfs_find_bigger(self,rowid,colid):
        if self.res[rowid][colid]==-1:
            now = self.matrix[rowid][colid]
            biggers = [(r,c) for r,c in self.next(rowid,colid) if self.matrix[r][c]>now]
            self.res[rowid][colid] = max([0]+[self.dfs_find_bigger(r,c) for r,c in biggers]) + int(len(biggers)>0)
        return self.res[rowid][colid]


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.height,self.width = len(matrix), len(matrix[0])
        self.res = [[-1]*self.width for _ in range(self.height)]
        for rowid in range(self.height):
            for colid in range(self.width):
                self.dfs_find_bigger(rowid,colid)
        print(self.res)
        return int(np.max(np.array(self.res)))+1


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.longestIncreasingPath(*data)


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
        [[[9,9,4],[6,6,8],[2,1,1]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
