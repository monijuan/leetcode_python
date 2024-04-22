# -*- coding: utf-8 -*-
# @Time    : 2024/4/22 9:33
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 216. 组合总和 III.py
# @Software: PyCharm
# ===================================
"""找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。



示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。
示例 3:

输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。


提示:

2 <= k <= 9
1 <= n <= 60
"""
from leetcode_python.utils import *


class Solution:
    def dfs(self, nowlist, sumnow, need, numnow):
        if need == 0:
            if len(nowlist) == self.k and nowlist not in self.res:
                self.res.append(nowlist)
        elif numnow <= need and numnow <= 9 and len(nowlist) < self.k:
            # 插入当前数
            self.dfs(nowlist + [numnow], sumnow + numnow, need - numnow, numnow + 1)
            # 跳过当前数
            self.dfs(nowlist, sumnow, need, numnow + 1)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.k = k
        self.dfs([], 0, n, 1)
        return self.res

class Solution_2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations
        return list(t for t in combinations(range(1, 10), k) if sum(t) == n)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.combinationSum3(*data)


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
        [3, 7],
        [3, 9],
        [4, 1],
        [8, 55],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
