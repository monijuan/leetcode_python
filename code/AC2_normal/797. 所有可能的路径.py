# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 8:55
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 797. 所有可能的路径.py
# @Software: PyCharm
# ===================================
"""给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。

译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。

 

示例 1：



输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
示例 2：



输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
示例 3：

输入：graph = [[1],[]]
输出：[[0,1]]
示例 4：

输入：graph = [[1,2,3],[2],[3],[]]
输出：[[0,1,2,3],[0,2,3],[0,3]]
示例 5：

输入：graph = [[1,3],[2],[3],[]]
输出：[[0,1,2,3],[0,3]]
 

提示：

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i（即，不存在自环）
graph[i] 中的所有元素 互不相同
保证输入为 有向无环图（DAG）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-paths-from-source-to-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        self.routes = []

    def dfs(self,route_,now):
        route = route_.copy()
        route.append(now)
        if now == self.end:
            self.routes.append(route)
        else:
            for next in self.graph[now]:
                self.dfs(route, next)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.end = len(graph)-1
        self.dfs([],0)
        return self.routes


def test(data_test):
    s = Solution()
    return s.allPathsSourceTarget(*data_test)


if __name__ == '__main__':
    datas = [
        [[[1,2],[3],[3],[]]],# [[0,1,3],[0,2,3]]
        [[[4,3,1],[3,2,4],[3],[4],[]]],# [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        [[[1],[]]],             # [[0,1]]
        [[[1,2,3],[2],[3],[]]], # [[0,1,2,3],[0,2,3],[0,3]]
        [[[1,3],[2],[3],[]]],   # [[0,1,2,3],[0,3]]
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
