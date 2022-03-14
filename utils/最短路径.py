# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 12:10
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 最短路径.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *

class map_单源最短路径():
    def __init__(self, edges):
        """ edges: [[from,to,weight],]"""
        self.link_dict = defaultdict(dict)

        for s, e, w in edges:
            if e in self.link_dict[s]:
                self.link_dict[s][e] = min(self.link_dict[s][e], w)
            else:
                self.link_dict[s][e] = w

    def bfs(self, source):
        """ 单源最短路径 """
        source2end = {}
        to_visit = [[0, source]]

        while len(to_visit) > 0:
            cost, pnow = heapq.heappop(to_visit)
            if pnow in source2end: continue
            source2end[pnow] = cost
            for pnext in self.link_dict[pnow]:
                if pnext in source2end: continue
                heapq.heappush(to_visit, [cost + self.link_dict[pnow][pnext], pnext])
        return source2end


def test_6032_得到要求路径的最小带权子图():
    class Solution:
        def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

            cgraph = CGraph_weight(edges)
            rcgraph = CGraph_weight([[t, s, w] for s, t, w in edges])
            dis1 = cgraph.bfs(src1)
            dis2 = cgraph.bfs(src2)
            dist = rcgraph.bfs(dest)
            # print(dis1)
            # print(dis2)
            # print(dist)
            to_ret = 1e99
            for mid in range(n):
                if mid in dis1 and mid in dis2 and mid in dist:
                    to_ret = min(to_ret, dis1[mid] + dis2[mid] + dist[mid])
            if to_ret > 1e88:
                return -1
            return to_ret
