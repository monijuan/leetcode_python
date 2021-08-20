# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 22:15
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 221. 最大正方形.py
# @Software: PyCharm
# ===================================
"""在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List

class Solution:
    def __init__(self):
        """
        思路：
            一行行遍历，记录左边和上边连续多少个1，同时对比左上角确定此刻正方形的边长
        """
        pass

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        每个位置用(x,y,z)表示，其中：
            x表示水平向右方向第x个连续的1，
            y表示竖直向下方向第y个连续的1，
            z表示以这个位置为右下角的最大正方形的边长。
        :param matrix:
        :return:
        """
        max_size = 0
        matrix = [[int(x) for x in line] for line in matrix]
        last_line = [[0,0,0] for _ in matrix[0]]
        for row_id,row in enumerate(matrix):
            this_line = [[0,0,0] for _ in row]
            for col_id,now in enumerate(row):
                if now==0:
                    this_line[col_id] = [0,0,0]
                else:
                    num_1_col = last_line[col_id][1]+1
                    if col_id==0:
                        num_1_row = 1
                        this_size = 1
                    else:
                        num_1_row = this_line[col_id-1][0]+1
                        this_size = min(num_1_row,num_1_col,last_line[col_id-1][2]+1)
                    this_line[col_id] = [num_1_row,num_1_col,this_size]
                    max_size = max(max_size,this_size)
            last_line = this_line
            print(this_line)
        return max_size**2

def print_matrix(matrix):
    for line in matrix:
        print(line)

def test(data_test):
    s = Solution()
    print_matrix(*data_test)
    return s.maximalSquare(*data_test)

if __name__ == '__main__':
    datas = [
        [[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]], # 4
        [[["0", "1"], ["1", "0"]]],   # 1
        [[["0"]]],      # 0
        [[["1"]]],      # 1
        [[["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]],      # 4
        [[["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]],#16
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')