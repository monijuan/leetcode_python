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
# product 多重循环
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

# 并查集
def __unionset(bombs: List[List[int]]) -> int:
    n, d = len(bombs), defaultdict(set)
    for i, j in product(range(n), repeat = 2):
        if math.dist(bombs[i][:2], bombs[j][:2]) <= bombs[i][2]: d[i].add(j)
    for k, i in product(range(n), repeat = 2):
        if k in d[i]: d[i] |= d[k]
    return max(len(d[i]) for i in range(n))