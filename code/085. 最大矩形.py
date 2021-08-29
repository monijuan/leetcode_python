# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 16:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 085. 最大矩形.py
# @Software: PyCharm
# ===================================
"""给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0
 

提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        每个位置用(num_1_row, num_1_col, now_width, now_height)表示，其中：
            num_1_row 表示水平向右方向第x个连续的1，
            num_1_col 表示竖直向下方向第y个连续的1，
            now_width  表示以这个位置为右下角的最大矩形的宽，
            now_height 表示以这个位置为右下角的最大矩形的高。
        """
        if len(matrix)==0:return 0
        max_size = 0
        matrix = [[int(x) for x in line] for line in matrix]
        last_line = [[0,0,0,0] for _ in matrix[0]]
        for row_id,row in enumerate(matrix):
            this_line = [[0,0,0,0] for _ in row]
            for col_id,now in enumerate(row):
                if now==0:
                    this_line[col_id] = [0,0,0,0]
                else:
                    num_1_col = last_line[col_id][1]+1
                    if col_id==0:
                        num_1_row = 1
                        now_width = 1
                        now_height = num_1_col
                    else:
                        num_1_row = this_line[col_id-1][0]+1
                        now_width  = min(num_1_row,last_line[col_id-1][2]+1)
                        now_height = min(num_1_col,last_line[col_id-1][3]+1)
                    this_line[col_id] = [num_1_row,num_1_col,now_width,now_height]
                    max_size = max(max_size,now_width*now_height)
            last_line = this_line
            print(this_line)
        return max_size


def test(data_test):
    s = Solution()
    return s.maximalRectangle(*data_test)


if __name__ == '__main__':
    datas = [
        # [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]],    #6
        # [[]],       # 0
        # [[["0"]]],  # 0
        # [[["1"]]],  # 1
        # [[["0","0"]]],  # 0
        [[["1","1"]]],  # 2
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
