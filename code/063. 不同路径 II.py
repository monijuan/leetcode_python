# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 15:06
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 063. 不同路径 II.py
# @Software: PyCharm
# ===================================
"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

 

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 

提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:return 0
        width = len(obstacleGrid[0])
        height = len(obstacleGrid)
        map = [[0 for _ in range(width)] for _ in range(height)]
        for row_id,row in enumerate(obstacleGrid[::-1]):
            row_id = height-row_id-1
            for col_id,is_stone in enumerate(row[::-1]):
                col_id=width-col_id-1
                if row_id==height-1 and col_id==width-1:
                    map[row_id][col_id] = 1 # 终点为一种情况
                elif is_stone:
                    map[row_id][col_id] = 0 # 如果是障碍则0种情况
                elif row_id<height-1 and col_id<width-1:    # 不靠边 = 下面+右边
                    map[row_id][col_id] = map[row_id + 1][col_id] + map[row_id][col_id + 1]
                elif row_id<height-1:   # 不是最下面一行 （是最右一列）= 下面
                    map[row_id][col_id] = map[row_id + 1][col_id]
                else: # 是最下面一行 =　右边
                    map[row_id][col_id] = map[row_id][col_id + 1]
                # print(f'point:[{row_id}][{col_id}]={is_stone}, map:{map}')
        # print(map)
        return map[0][0]


def test(data_test):
    s = Solution()
    return s.uniquePathsWithObstacles(data_test)


if __name__ == '__main__':
    datas = [
        [[0,0,0],[0,1,0],[0,0,0]],    # 2
        # [[0,0,0],[0,1,0]],
        # [[1,2,3],[4,5,6],[7,8,9]],
        # [[0,0,0],[0,1,0]],
        [[0,1],[0,0]],    # 1
        [[0,0],[0,1]],    # 0
        [[0, 0], [1, 1], [0, 0]],#0
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
