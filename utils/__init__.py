# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 21:33
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : __init__.py
# @Software: PyCharm 
# ===================================
from typing import List, Callable, Optional
from functools import lru_cache, reduce
from itertools import product
import queue
import heapq
import numpy as np
import sys
import time
import math
import random
from collections import Counter, defaultdict, deque
from sortedcontainers import SortedList, SortedKeyList, SortedListWithKey, SortedDict, SortedKeysView, \
    SortedItemsView, SortedValuesView, SortedSet

from .rand_help import randListInt, randListListInt, randListListIntShow
from .all_node import ListNode, TreeNode
from .load_node import List2Tree, List2BST, List2Node, BST2List, Tree2List, Node2List
from .树状数组 import tree_树状数组
from .最短路径 import map_单源最短路径
from .并查集 import union_并查集
from .前缀和 import pre_二维前缀和
from .字符串哈希 import hash_字符串哈希
from .线段树 import tree_线段树


@lru_cache(None)
########################### test
## region 二维前缀和
def sum_grid二维前缀和(grid):
    """
        res[i][j][0]:水平和
        res[i][j][1]:垂直和
    """
    h, w = len(grid), len(grid[0])
    res = [[[0, 0] for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            res[i][j][0] = grid[i][j] + (0 if j == 0 else res[i][j - 1][0])
    for j in range(w):
        for i in range(h):
            res[i][j][1] = grid[i][j] + (0 if i == 0 else res[i - 1][j][1])
    return res
# endregion

# region 子数组
def lengthOfLIS_最长递增子数组(nums: List[int]) -> int:
    """最长非递减子数组"""
    dp = []
    for num in nums:
        j = bisect.bisect_left(dp, num + 1)
        if j == len(dp):
            dp.append(num)
        else:
            dp[j] = num
    return len(dp)


def lengthOfLIS_最长严格递增子数组(nums: List[int]) -> int:
    """最长递增子数组"""
    dp = []
    for num in nums:
        j = bisect.bisect_left(dp, num)
        if j == len(dp):
            dp.append(num)
        else:
            dp[j] = num
    return len(dp)


# endregion

# region dfs
def __demo_bfs():
    end = '0001'
    start, step = '0000', 0
    queue = [(start, step)]
    while queue:
        word, step_ = queue.pop(0)
        if word == end:
            return step
        for id in range(len(word)):
            new = word
            if True:
                queue.append((new, step + 1))
    return -1


# endregion

# region dfs
class Solution:
    """ 047. 全排列 II"""

    def dfs(self, now):
        if self.length >= len(now):
            if now not in self.res:
                self.res.append(now)
        else:
            for nextid in range(self.length):
                if not self.vis[nextid]:
                    self.vis[nextid] = True
                    self.dfs(now + [self.nums[nextid]])
                    self.vis[nextid] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length = len(nums)
        self.vis = [False] * self.length
        self.res = []
        self.dfs([])
        return self.res


# endregion

# region 二分查找
import bisect


def __test_bisect():
    li = list(range(0, 20, 3))
    print(f'li:{li}')
    for x in [1, 2, 3, 4, 20]:
        print(f"{x}:[left]{bisect.bisect_left(li, x)}, [right]{bisect.bisect_right(li, x)}, ")


# endregion

# region product 多重循环
def __test_product():
    """shows:
            0 0 0
            0 0 1
            0 0 2
            0 1 0
            0 1 1
            0 1 2
            0 2 0
            0 2 1
            0 2 2
            1 0 0
            1 0 1
            1 0 2
            1 1 0
            1 1 1
            1 1 2
            1 2 0
            1 2 1
            1 2 2
            2 0 0
            2 0 1
            2 0 2
            2 1 0
            2 1 1
            2 1 2
            2 2 0
            2 2 1
            2 2 2
    """
    li = list(range(3))
    n, d = len(li), defaultdict(set)
    for i, j, k in product(range(n), repeat=3):
        print(i, j, k)
# endregion


# region 二位凸包
class Solution_587_安装栅栏:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0]:
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # // 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p], trees[q], tree) < 0:
                    q = r
            # 是否存在点 i, 使得 p q i 在同一条直线上
            for i, b in enumerate(vis):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True
            if not vis[q]:
                ans.append(trees[q])
                vis[q] = True
            p = q
            if p == leftMost:
                break
        return ans
# endregion