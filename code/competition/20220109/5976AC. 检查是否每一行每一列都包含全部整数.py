# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 10:20
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5976AC. 检查是否每一行每一列都包含全部整数.py
# @Software: PyCharm 
# ===================================
"""对一个大小为 n x n 的矩阵而言，如果其每一行和每一列都包含从 1 到 n 的 全部 整数（含 1 和 n），则认为该矩阵是一个 有效 矩阵。

给你一个大小为 n x n 的整数矩阵 matrix ，请你判断矩阵是否为一个有效矩阵：如果是，返回 true ；否则，返回 false 。

 

示例 1：



输入：matrix = [[1,2,3],[3,1,2],[2,3,1]]
输出：true
解释：在此例中，n = 3 ，每一行和每一列都包含数字 1、2、3 。
因此，返回 true 。
示例 2：



输入：matrix = [[1,1,1],[1,2,3],[1,2,3]]
输出：false
解释：在此例中，n = 3 ，但第一行和第一列不包含数字 2 和 3 。
因此，返回 false 。
 

提示：

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-every-row-and-column-contains-all-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rrr = list(range(1,n+1))
        for r in matrix:
            if sorted(r)!=rrr:return False

        for c in range(n):
            col = []
            for r in range(n):
                col.append(matrix[r][c])
            if sorted(col)!=rrr:return False
        return True


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.checkValid(*data)


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
        [[[1,2,3],[3,1,2],[2,3,1]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')