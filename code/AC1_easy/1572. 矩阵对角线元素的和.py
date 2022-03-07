# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 16:41
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1572. 矩阵对角线元素的和.py
# @Software: PyCharm
# ===================================
"""给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

 

示例  1：



输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
示例  2：

输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8
示例 3：

输入：mat = [[5]]
输出：5
 

提示：

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-diagonal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n=len(mat)
        for i,row in enumerate(mat):
            r=n-1-i
            if i==r:res+=row[i]
            else:
                res+=row[i]
                res+=row[r]
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
