# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 16:37
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 16. 游乐园的游览计划.py
# @Software: PyCharm
# ===================================
"""又到了一年一度的春游时间，小吴计划去游乐场游玩 1 天，游乐场总共有 N 个游乐项目，编号从 0 到 N-1。小吴给每个游乐项目定义了一个非负整数值 value[i] 表示自己的喜爱值。两个游乐项目之间会有双向路径相连，整个游乐场总共有 M 条双向路径，保存在二维数组 edges中。 小吴计划选择一个游乐项目 A 作为这一天游玩的重点项目。上午小吴准备游玩重点项目 A 以及与项目 A 相邻的两个项目 B、C （项目A、B与C要求是不同的项目，且项目B与项目C要求相邻），并返回 A ，即存在一条 A-B-C-A 的路径。 下午，小吴决定再游玩重点项目 A以及与A相邻的两个项目 B'、C'，（项目A、B'与C'要求是不同的项目，且项目B'与项目C'要求相邻），并返回 A ，即存在一条 A-B'-C'-A 的路径。下午游玩项目 B'、C' 可与上午游玩项目B、C存在重复项目。 小吴希望提前安排好游玩路径，使得喜爱值之和最大。请你返回满足游玩路径选取条件的最大喜爱值之和，如果没有这样的路径，返回 0。 注意：一天中重复游玩同一个项目并不能重复增加喜爱值了。例如：上下午游玩路径分别是 A-B-C-A与A-C-D-A 那么只能获得 value[A] + value[B] + value[C] + value[D] 的总和。

示例 1：

输入：edges = [[0,1],[1,2],[0,2]], value = [1,2,3]

输出：6

解释：喜爱值之和最高的方案之一是 0->1->2->0 与 0->2->1->0 。重复游玩同一点不重复计入喜爱值，返回1+2+3=6

示例 2：

输入：edges = [[0,2],[2,1]], value = [1,2,5]

输出：0

解释：无满足要求的游玩路径，返回 0

示例 3：

输入：edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]], value = [7,8,6,8,9,7]

输出：39

解释：喜爱值之和最高的方案之一是 3->0->1->3 与 3->4->5->3 。喜爱值最高为 7+8+8+9+7=39

限制：

3 <= value.length <= 10000
1 <= edges.length <= 10000
0 <= edges[i][0],edges[i][1] < value.length
0 <= value[i] <= 10000
edges中没有重复的边
edges[i][0] != edges[i][1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/you-le-yuan-de-you-lan-ji-hua
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        """
        参考大佬解释：https://leetcode-cn.com/problems/you-le-yuan-de-you-lan-ji-hua/solution/tu-jie-si-lu-xiang-xi-zheng-ming-by-newhar/
        """
        pass

    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        M,N = len(edges),len(value) # M:边的数量，N:点的数量

        # 对边按权值和排序，以便之后对每个点，直接获得按权值和排序的边
        edges.sort(key=lambda e:-(value[e[0]]+value[e[1]]))

        # 统计各个点的度数（出边数量）
        cnts = [0]*N
        for v in edges:
            cnts[v[0]]+=1
            cnts[v[1]]+=1

        # 将无向图重建为有向图（度小->度大）
        G = [[] for _ in range(N)]
        for e_id, (left_id, right_id) in enumerate(edges):
            if cnts[left_id] < cnts[right_id] or (cnts[left_id] == cnts[right_id] and left_id<right_id):
                G[left_id].append([right_id, e_id])
            else:
                G[right_id].append([left_id, e_id])

        # 求所有的三元环，并按边归类
        nodes,vis,idxs = [[] for _ in range(M)],[-1]*N,[0]*N
        for e_id, (a_id, b_id) in enumerate(edges):
            for next_id,next_e_id in G[a_id]:
                vis[next_id] = e_id
                idxs[next_id] = next_e_id
            for next_id,next_e_id in G[b_id]:
                if vis[next_id] == e_id:    # 形成回路
                    nodes[next_e_id].append(a_id)
                    nodes[idxs[next_id]].append(b_id)
                    nodes[e_id].append(next_id)

        # 将三元环按顶点归类，每个顶点自动获得按权值和排序的边
        centers = [[] for _ in range(N)]
        for i in range(M):
            for n in nodes[i]:
                centers[n].append(i)

        # 求出结果
        res = 0
        for c_id,nexts in enumerate(centers):
            len_next = len(nexts)
            bound = len_next-1
            for e_a_id,e_a in enumerate(nexts):
                if e_a_id>min(3,bound):break
                cur_0 = value[c_id] + value[edges[e_a][0]] + value[edges[e_a][1]] # 边a的两端（第一个三角形）
                for e_b_id in range(e_a_id, len_next):
                    cur = cur_0
                    cnt = 0
                    if edges[nexts[e_b_id]][0] not in edges[e_a]:   # b的一端（第二个三角形的一个点）
                        cur += value[edges[nexts[e_b_id]][0]]
                        cnt += 1
                    if edges[nexts[e_b_id]][1] not in edges[e_a]:   # b的另一端（第二个三角形的另一个点）
                        cur += value[edges[nexts[e_b_id]][1]]
                        cnt += 1
                    # print(f"c_id:{c_id}, c:{nexts}, a:{e_a_id}, b:{e_b_id}, cnt:{cnt}, cur:{cur}, res:{res}")
                    res = max(res, cur)
                    if cnt==2: # 从大到小，如果找到两个三角形了，则找到两个三角形的边界情况
                        bound = e_b_id-1 # 因为这个三角形还可能构成其他情况，所以 e_b_id 仍然需要检查
                        break
        return res


def test(data_test):
    s = Solution()
    # s = Solution_重构大佬CPP()
    return s.maxWeight(*data_test)


def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [[[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]],[7,8,6,8,9,7]],
        [[[0,2],[2,1]],[1,2,5]],
        [[[2,9],[4,9],[0,6],[0,1],[3,5],[1,2],[5,9],[2,5],[6,9],[7,8],[0,7],[1,4],[6,8],[8,9],[1,9],[6,7],[1,6],[2,4],[0,8],[4,5],[1,3],[0,9],[0,5],[3,6],[1,7],[4,7],[5,8],[0,4],[0,2],[3,9]],[9327,1424,8248,1216,6629,5729,6388,8371,6345,8]],
        [[[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[4,5],[4,6],[4,7],[4,8],[4,9],[5,6],[5,7],[5,8],[5,9],[6,7],[6,8],[6,9],[7,8],[7,9],[8,9]],[6808,5250,74,3659,8931,1273,7545,879,7924,7710]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
