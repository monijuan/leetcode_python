# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 16:50
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 2373. 矩阵中的局部最大值.py
# @Software: PyCharm
# ===================================
"""给你一个大小为 n x n 的整数矩阵 grid 。

生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：

maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。

返回生成的矩阵。

 

示例 1：



输入：grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
输出：[[9,9],[8,6]]
解释：原矩阵和生成的矩阵如上图所示。
注意，生成的矩阵中，每个值都对应 grid 中一个相接的 3 x 3 矩阵的最大值。
示例 2：



输入：grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
输出：[[2,2,2],[2,2,2],[2,2,2]]
解释：注意，2 包含在 grid 中每个 3 x 3 的矩阵中。
 

提示：

n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/largest-local-values-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        print([(x,y) for x in range(3) for y in range(3)])
        h,w = len(grid),len(grid[0])
        res = [[0 for _ in range(w-2)] for _ in range(h-2)]
        for r in range(h-2):
            for c in range(w-2):
                res[r][c] = max(max(grid[_r][c:c+3]) for _r in range(r,r+3))
                # print(f"res[{r}][{c}] = r[{r}:{r+3}], c[{c}:{c+3}]")
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.largestLocal(*data)


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
        # [[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]],
        # [[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2],[6,2,2,2],[6,2,2,9]]],
        [[[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
