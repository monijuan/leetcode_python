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

# region 并查集
def __unionset(bombs: List[List[int]]) -> int:
    n, d = len(bombs), defaultdict(set)
    for i, j in product(range(n), repeat = 2):
        if math.dist(bombs[i][:2], bombs[j][:2]) <= bombs[i][2]: d[i].add(j)
    for k, i in product(range(n), repeat = 2):
        if k in d[i]: d[i] |= d[k]
    return max(len(d[i]) for i in range(n))

class UnionFindSet(object):
    """并查集"""
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.parent_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.parent_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        """使用递归的方式来查找父节点
        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.parent_dict[node]
        if(node != father):
            if father != self.parent_dict[father]:    # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.parent_dict[node] = father
        return father

    def isConnected(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.parent_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.parent_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

def __test_UnionFindSet():
    pass

# endregion
