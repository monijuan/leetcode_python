# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 16:20
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 树状数组.py
# @Software: PyCharm
# ===================================
"""
参考：https://mp.weixin.qq.com/s?__biz=MzkyMzI3ODgzNQ==&mid=2247483674&idx=1&sn=263595b26950ac60e5bf789839d70c9e&chksm=c1e6cd86f691449062d780b96d9af6d9590a71872ebfee980d5b045b9963714043261027c16b&token=1500097142&lang=zh_CN#rd
"""
from leetcode_python.utils import *


class tree_树状数组:
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
            self.ntimessum[pos] += k * (x - 1)
            pos += self._lowbit(pos)

    def sum_pos_single(self, pos):
        """ 单点更新：1~pos 区间求和 """
        if not pos: return 0
        ret = 0
        while pos:
            ret += self.sum[pos]
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
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_internal(self, l, r):
        """ 区间更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_internal(r) - self.sum_pos_internal(l - 1)

    def get_sums(self):
        """ 区间更新：计算所有[0,i]的求和"""
        return [self.sum_pos_internal(i) for i in range(1,self.n)]

    def get_scores(self):
        """ 区间更新：计算每一位的值"""
        sums = [self.sum_pos_internal(i) for i in range(1,self.n)]
        return [s-sums[i-1] if i>0 else s for i,s in enumerate(sums)]
    ####### endregion 区间更新



if __name__ == '__main__':
    class Solution_LCP05发LeetCoin:
        def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
            g = [[] for _ in range(n + 1)]
            for l in leadership: g[l[0]].append(l[1])
            # 用begin，end表示领导范围
            begin = [0] * (n + 1)
            end = [0] * (n + 1)
            id = 1

            def dfs(cur):
                nonlocal id
                begin[cur] = id
                for c in g[cur]: dfs(c)
                end[cur] = id
                id += 1

            dfs(1)
            # 树状数组
            tree = BIT(n)
            res = []
            for q in operations:
                if q[0] == 1:
                    tree.add_lr(end[q[1]], end[q[1]], q[2])
                elif q[0] == 2:
                    tree.add_lr(begin[q[1]], end[q[1]], q[2])
                else:
                    r = tree.sum_lr_internal(begin[q[1]], end[q[1]])
                    res.append((r + M) % M)
            return res
