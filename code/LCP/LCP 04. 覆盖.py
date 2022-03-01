# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 9:16
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 04. 覆盖.py
# @Software: PyCharm
# ===================================
"""你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。

 

输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。

输出：一个整数，代表最多能在棋盘上放的骨牌数。

 

示例 1：

输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
输出：2
解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）


 

示例 2：

输入：n = 3, m = 3, broken = []
输出：4
解释：下图是其中一种可行的摆放方式


 

限制：

1 <= n <= 8
1 <= m <= 8
0 <= b <= n * m

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/broken-board-dominoes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    @lru_cache(None)
    def next(self, rowid, colid):
        res = []
        for i, j in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= i < self.height and 0 <= j < self.width:
                res.append([i, j])
        return res

    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        self.height, self.width = n, m
        match = [[None] * m for _ in range(n)]
        for i, j in broken: match[i][j] = '#'

        def dfs(i, j, visited):
            visited.add((i, j))
            for ni, nj in self.next(i, j):
                nxt = match[ni][nj]
                if nxt in visited: continue
                if not nxt or dfs(*nxt, visited):
                    match[i][j] = (ni, nj)
                    match[ni][nj] = (i, j)
                    return True
            return False

        # 考虑奇数结点为起点
        return sum(dfs(i, j, {'#'}) for i in range(n) for j in range(m) if match[i][j] != '#' and (i + j) % 2)


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
