# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 17:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 119. 杨辉三角 II.py
# @Software: PyCharm
# ===================================
"""给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。



 

示例 1:

输入: rowIndex = 3
输出: [1,3,3,1]
示例 2:

输入: rowIndex = 0
输出: [1]
示例 3:

输入: rowIndex = 1
输出: [1,1]
 

提示:

0 <= rowIndex <= 33

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for row in range(rowIndex+1):
            res_row = []
            for col in range(row+1):
                if col in [0,row]:
                    res_row.append(1)
                else:
                    res_row.append(sum(res[row-1][col-1:col+1]))
            res.append(res_row)
        return res[-1]


def test(data_test):
    s = Solution()
    return s.getRow(*data_test)


if __name__ == '__main__':
    datas = [
        [3],
        [0],
        [1],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
