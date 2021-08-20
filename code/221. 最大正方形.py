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
            一行行遍历，如果是0则是0，如果是则是左边数+1，
            第二行开始，不仅考虑上一步的结果，还不能超过上面那个数字
        """
        pass

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(x) for x in line] for line in matrix]
        res = 0
        for row_id,row in enumerate(matrix):
            for col_id,now in enumerate(row):
                if now!=0 and col_id!=0:
                    if row_id==0:
                        matrix[row_id][col_id]=row[col_id-1]+1
                    else:
                        new = min(row[col_id-1]+1,matrix[row_id-1][col_id])
                        res = max(res,new)
                        matrix[row_id][col_id] = new
                
        print('\n'.join([str(x) for x in matrix]))
        return res


def test(data_test):
    s = Solution()
    return s.maximalSquare(*data_test)

if __name__ == '__main__':
    datas = [
        [[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]], # 4
        [[["0", "1"], ["1", "0"]]],   # 1
        [[["0"]]],    # 0
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')