# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 21:33
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : __init__.py
# @Software: PyCharm 
# ===================================
from .rand_help import *
from .all_node import *
from .load_node import *
import numpy as np
import time
import math
from typing import List,Callable,Optional
from functools import lru_cache
from collections import Counter,defaultdict
from sortedcontainers import SortedList, SortedKeyList, SortedListWithKey, SortedDict, SortedKeysView, \
    SortedItemsView, SortedValuesView, SortedSet
from itertools import product


########################### test
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
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        """使用递归的方式来查找父节点
        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.father_dict[node]
        if(node != father):
            if father != self.father_dict[father]:    # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
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
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

def __test_UnionFindSet():
    pass

# endregion