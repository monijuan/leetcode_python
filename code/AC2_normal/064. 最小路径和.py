# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 10:22
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 064. 最小路径和.py
# @Software: PyCharm
# ===================================
"""给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """动态规划逐行往下遍历，每行逐个往右遍历，自己+min(左边,右边)"""
        pass

    def minPathSum(self, grid: List[List[int]]) -> int:
        for rowid,row in enumerate(grid):
            line_now = []
            for colid,num in enumerate(row):
                if 0==rowid==colid:
                    line_now.append(num)
                elif 0==rowid:
                    line_now.append(num+line_now[-1])
                elif 0==colid:
                    line_now.append(num+line_last[colid])
                else:
                    line_now.append(num+min(line_now[-1],line_last[colid]))
            line_last = line_now
        return line_now[-1]


def test(data_test):
    s = Solution()
    return s.minPathSum(*data_test)


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
