# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 16:41
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 118. 杨辉三角.py
# @Software: PyCharm
# ===================================
"""给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。



 

示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]
 

提示:

1 <= numRows <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        """一行行遍历，每一行 `第col个数` = `前一行第col个数` +` 前一行第col+1个数`"""
        pass

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(numRows):
            res_row = []
            for col in range(row+1):
                if col in [0,row]:
                    res_row.append(1)
                else:
                    res_row.append(sum(res[row-1][col-1:col+1]))
            res.append(res_row)
        return res

def test(data_test):
    s = Solution()
    return s.generate(*data_test)


if __name__ == '__main__':
    datas = [
        [5],
        [1]
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
