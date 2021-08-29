# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 16:17
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 062. 不同路径.py
# @Software: PyCharm
# ===================================
"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109

"""
import time
from typing import List


class Solution:
    def __init__(self):
        """
        因为只能往下和往右，不能往回走，所以便从end往回遍历：
        - 路线数量 = 右边一格的路线数量 + 下边一格的路线数量
        - 当然，如果是最下面一行和最右边一列，就不存在下边一格和右边一格，要区分一下

        因为python的机制，一行行分析比较方便，如果是c++或java，从最右一列往左也是可以的，总之要么是“先从下往上再从右往左”，要么是“先从右往左再从下往上”，本质没有区别。
        """
        pass

    def uniquePaths(self, m: int, n: int) -> int:
        height = m
        width = n
        map = [[0 for _ in range(width)] for _ in range(height)]
        for row_id in range(height):
            row_id = height - row_id - 1
            for col_id in range(width):
                col_id = width - col_id - 1
                if row_id==height-1 and col_id==width-1:
                    map[row_id][col_id] = 1 # 终点为一种情况
                elif row_id<height-1 and col_id<width-1:    # 不靠边 = 下面+右边
                    map[row_id][col_id] = map[row_id + 1][col_id] + map[row_id][col_id + 1]
                elif row_id<height-1:   # 不是最下面一行 （是最右一列）= 下面
                    map[row_id][col_id] = map[row_id + 1][col_id]
                else: # 是最下面一行 =　右边
                    map[row_id][col_id] = map[row_id][col_id + 1]
        return map[0][0]


def test(data_test):
    s = Solution()
    return s.uniquePaths(*data_test)


if __name__ == '__main__':
    datas = [
        [3,7],      # 28
        [3,2],      # 3
        [7,3],      # 28
        [3,3],      # 6
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
