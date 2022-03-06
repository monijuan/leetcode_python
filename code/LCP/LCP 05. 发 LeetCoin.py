# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 10:50
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 05. 发 LeetCoin.py
# @Software: PyCharm
# ===================================
"""力扣决定给一个刷题团队发LeetCoin作为奖励。同时，为了监控给大家发了多少LeetCoin，力扣有时候也会进行查询。

 

该刷题团队的管理模式可以用一棵树表示：

团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）；
不存在循环管理的情况，如A管理B，B管理C，C管理A。
 

力扣想进行的操作有以下三种：

给团队的一个成员（也可以是负责人）发一定数量的LeetCoin；
给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin；
查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和。
 

输入：

N表示团队成员的个数（编号为1～N，负责人为1）；
leadership是大小为(N - 1) * 2的二维数组，其中每个元素[a, b]代表b是a的下属；
operations是一个长度为Q的二维数组，代表以时间排序的操作，格式如下：
operations[i][0] = 1: 代表第一种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量；
operations[i][0] = 2: 代表第二种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量；
operations[i][0] = 3: 代表第三种操作，operations[i][1]代表成员的编号；
输出：

返回一个数组，数组里是每次查询的返回值（发LeetCoin的操作不需要任何返回值）。由于发的LeetCoin很多，请把每次查询的结果模1e9+7 (1000000007)。

 

示例 1：

输入：N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
输出：[650, 665]
解释：团队的管理关系见下图。
第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0;
第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15.


 

限制：

1 <= N <= 50000
1 <= Q <= 50000
operations[i][0] != 3 时，1 <= operations[i][2] <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-bonus
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

M = int(1e9 + 7)

class BIT:
    def __init__(self, n):
        self.n = n + 5
        self.sum = [0 for _ in range(n + 10)]
        self.ntimessum = [0 for _ in range(n + 10)]

    def _lowbit(self, x):
        return x & (-x)

    ### region 单点更新
    def add_pos(self, pos, k):
        """pos 单点更新 k"""
        x = pos
        while pos <= self.n:
            self.sum[pos] += k
            self.sum[pos] %= M
            self.ntimessum[pos] += k * (x - 1)
            self.ntimessum[pos] %= M
            pos += self._lowbit(pos)

    def sum_pos_single(self, pos):
        """ 单点更新：1~pos 区间求和 """
        if not pos: return 0
        ret = 0
        while pos:
            ret += self.sum[pos]
            ret %= M
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_single(self, l, r):
        """ 单点更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_single(r) - self.sum_pos_single(l - 1)

    def get_pos(self, pos):
        """ 单点更新：pos 单点查询 """
        return self.sum_pos_single(pos) - self.sum_pos_single(pos - 1)
    ####### endregion 单点更新

    ### region 区间更新
    def add_lr(self, l, r, k):
        """l~r 区间更新 k"""
        self.add_pos(l, k)
        self.add_pos(r + 1, -k)

    def sum_pos_internal(self, pos):
        """ 区间更新：1~pos 区间求和 """
        if not pos:
            return 0
        ret = 0
        x = pos
        while pos:
            ret += x * self.sum[pos] - self.ntimessum[pos]
            ret %= M
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_internal(self, l, r):
        """ 区间更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_internal(r) - self.sum_pos_internal(l - 1)
    ####### endregion 区间更新

class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n+1)]
        for l in leadership: g[l[0]].append(l[1])
        # 用begin，end表示领导范围
        begin = [0]*(n+1)
        end = [0]*(n+1)
        id=1
        def dfs(cur):
            nonlocal id
            begin[cur]=id
            for c in g[cur]:dfs(c)
            end[cur]=id
            id+=1
        dfs(1)
        # 树状数组
        tree = BIT(n)
        res = []
        for q in operations:
            if q[0]==1:
                tree.add_lr(end[q[1]],end[q[1]],q[2])
            elif q[0]==2:
                tree.add_lr(begin[q[1]],end[q[1]],q[2])
            else:
                r = tree.sum_lr_internal(begin[q[1]],end[q[1]])
                res.append((r+M)%M)
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
