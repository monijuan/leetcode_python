# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 9:15
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 并查集.py
# @Software: PyCharm
# ===================================
from leetcode_python.utils import *


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



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)
