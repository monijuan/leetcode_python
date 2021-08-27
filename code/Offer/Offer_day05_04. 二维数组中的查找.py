# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 10:58
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : Offer_day05_04. 二维数组中的查找.py
# @Software: PyCharm
# ===================================
"""在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:return False
        elif len(matrix[0])==0:return False
        for row in matrix:print(row)
        # 最下一行，先向左
        # print('to left')
        row = 0
        # for col_id,num in enumerate(matrix[-1][::-1]):
        #     print(col_id,num)
        #     if num>target:
        #         col_id_right=col_id
        #     elif num==target:
        #         return True
        #     else:
        #         break
        for row_id in range(len(matrix)-1,-1,-1):
            print(row_id,matrix[row_id][-1])
            if matrix[row_id][-1]>target:
                row=row_id
            elif matrix[row_id][-1]==target:
                return True
            else:
                break
        print()
        # # 再向下
        # print('to down')
        # row_id_down = 0
        # for row_id,row in enumerate(matrix):
        #     if row[col_id_right]<target:
        #         row_id_down=row_id
        #     elif row[col_id_right]==target:
        #         return True
        #     else:
        #         row_id_down=row_id  # 找到更大的这一行向左
        #         break
        #
        # # 再向左
        print('to left')
        print(matrix[row_id_down][:col_id_right])
        return target in matrix[row_id_down][:col_id_right]


def test(data_test):
    s = Solution()
    return s.findNumberIn2DArray(*data_test)


if __name__ == '__main__':
    datas = [
        [[[1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
         ],5],
        # [[[1,   4,  7, 11, 15],
        #   [2,   5,  8, 12, 19],
        #   [3,   6,  9, 16, 22],
        #   [10, 13, 14, 17, 24],
        #   [18, 21, 23, 26, 30]
        #  ],10],
        # [[[1,   4,  7, 11, 15],
        #   [2,   5,  8, 12, 19],
        #   [3,   6,  9, 16, 22],
        #   [10, 13, 14, 17, 24],
        #   [18, 21, 23, 26, 30]
        #  ],20],
        # [[],0],
        # [[[]],1],
        # [[[-1,3]],3],
        # [[[2,5],[2,8],[7,9],[7,11],[9,11]], 7],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
