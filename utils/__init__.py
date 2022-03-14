# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 21:33
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : __init__.py
# @Software: PyCharm 
# ===================================
from .rand_help import randListInt,randListListInt,randListListIntShow
from .all_node import ListNode,TreeNode
from .load_node import List2Tree,List2BST,List2Node,BST2List,Tree2List,Node2List
from .树状数组 import tree_树状数组
from .最短路径 import map_单源最短路径
import numpy as np
import sys
import time
import math
from typing import List,Callable,Optional
from functools import lru_cache
from collections import Counter,defaultdict,deque
from sortedcontainers import SortedList, SortedKeyList, SortedListWithKey, SortedDict, SortedKeysView, \
    SortedItemsView, SortedValuesView, SortedSet
from itertools import product
import queue
import heapq


@lru_cache(None)

########################### test
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
class Solution:
    """ 047. 全排列 II"""
    def dfs(self,now):
        if self.length>=len(now):
            if now not in self.res:
                self.res.append(now)
        else:
            for nextid in range(self.length):
                if not self.vis[nextid]:
                    self.vis[nextid]=True
                    self.dfs(now+[self.nums[nextid]])
                    self.vis[nextid]=False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length = len(nums)
        self.vis = [False]*self.length
        self.res = []
        self.dfs([])
        return self.res
# endregion

# region 二分查找
import bisect
def __test_bisect():
    li = list(range(0,20,3))
    print(f'li:{li}')
    for x in [1,2,3,4,20]:
        print(f"{x}:[left]{bisect.bisect_left(li,x)}, [right]{bisect.bisect_right(li,x)}, ")
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
    for i, j, k in product(range(n), repeat = 3):
        print(i,j,k)
# endregion


