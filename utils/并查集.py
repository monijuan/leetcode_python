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

class union_并查集(object):
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

class union_并查集2:
    def __init__(self, n):
        self.parent = [x for x in range(n)]  # x的直接老板是谁（不是掌门，不是幕后boss ）
        self.sz = [0 for x in range(n)]  # 不同之处  等函数中置1了,从说明这是个人  每个人能管几个人  能管自己也算1个
        self.part = n  # 江湖上有几个门派

    def Find(self, x: int) -> int:  # 找x所在门派的 掌门（终极boss，门派老大）
        if self.parent[x] == x:
            return x
        return self.Find(self.parent[x])

    def Union(self, x: int, y: int) -> bool:  # 合并两个门派
        root_x = self.Find(x)  # x所在门派的掌门
        root_y = self.Find(y)  # y所在门派的掌门
        if root_x == root_y:  # 如果是同一个人  不用合并了  本就是同门
            return False
        if self.sz[root_x] > self.sz[root_y]:  # root_x 手下的人多
            root_x, root_y = root_y, root_x  # 为了代码写起来简洁  不然要写个else root_y合并到root_x门下
        self.parent[root_x] = root_y  # root_x带着门派投靠到root_y门下  root_x认root_y做老板
        self.sz[root_y] += self.sz[root_x]  # root_y手下的人马 更多了  把新增的人马数统计好
        self.part -= 1  # 江湖上从此少了一个门派
        return True

    def inthesamepart(self, x: int, y: int) -> bool:  # 判断 x y 在不在同一个门派
        root_x = self.Find(x)
        root_y = self.Find(y)
        return root_x == root_y

    def getpartsize(self, x: int) -> int:  # 判断 x 所在的门派， 有多少人
        root_x = self.Find(x)
        return self.sz[root_x]  # 其实就是  掌门手下有多少人马（包含掌门自己）


class union_并查集list:
    """
    1631. 最小体力消耗路径
    https://leetcode.cn/problems/path-with-minimum-effort/solutions/581109/zui-xiao-ti-li-xiao-hao-lu-jing-by-leetc-3q2j/?envType=daily-question&envId=2024-04-22
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)
