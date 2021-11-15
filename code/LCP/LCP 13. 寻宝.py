# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 10:21
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 13. 寻宝.py
# @Software: PyCharm
# ===================================
"""我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。

迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。

要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。

迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。

我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。

示例 1：

输入： ["S#O", "M..", "M.T"]

输出：16

解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。

示例 2：

输入： ["S#O", "M.#", "M.T"]

输出：-1

解释：我们无法搬到石头触发机关

示例 3：

输入： ["S#O", "M.T", "M.."]

输出：17

解释：注意终点也是可以通行的。

限制：

1 <= maze.length <= 100
1 <= maze[i].length <= 100
maze[i].length == maze[j].length
S 和 T 有且只有一个
0 <= M的数量 <= 16
0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xun-bao
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *
from collections import deque

class Solution:
    def __init__(self):
        """
        宏观思路：
            1. 计算关键点到关键点之间的最短距离
            2. 计算机关 经过任意石堆 再到另一个机关，的最短距离
            3. 从起点开始动态规划，计算触发不同机关所需要的步数
            4. 寻找所有机关都触发完的情况下，需要的最短步数
            5. 4求出的最短步数+最后一个被触发的机关到终点的距离
        """
        # #   墙壁，不可以路过。（不考虑）
        # .   可以路过。（不考虑）
        self.S = [] # S   起点。可以路过
        self.T = [] # T   终点。可以路过
        self.O = [] # O   石堆，每次只能取一个。可以路过
        self.M = [] # M   机关，需要搬石头过去。可以路过

    def 相邻点(self, i, j):
        for rowid, colid in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= rowid < self.height and 0 <= colid < self.width:
                yield rowid, colid

    def 计算该点到全图的最短距离(self, i, j):
        dist = [[float('inf')] * self.width for _ in range(self.height)]
        dist[i][j] = 0
        queue = [(i, j, 0)]
        while queue:
            row_id, col_id, dis = queue.pop(0)
            for row_id_next, col_id_next in self.相邻点(row_id, col_id):
                if self.maze[row_id_next][col_id_next] != '#' and dis + 1 < dist[row_id_next][col_id_next]:
                    dist[row_id_next][col_id_next] = dis + 1
                    queue.append((row_id_next, col_id_next, dis+1))
        return dist

    def minimalSteps(self, maze) -> int:
        # 初始化，记录STOM四类坐标
        self.maze = maze
        self.height, self.width = len(maze), len(maze[0])
        for row_id in range(self.height):
            for col_id in range(self.width):
                if maze[row_id][col_id] in 'STOM':
                    self.__getattribute__(maze[row_id][col_id]).append((row_id,col_id))

        # 计算所有点到机关、终点的最短距离（起点当成机关）
        machines = self.S + self.M  # 机关 = [起点, 机关]
        dis_所有点到机关 = [self.计算该点到全图的最短距离(row_id, col_id) for row_id, col_id in machines]
        dis_所有点到终点 = self.计算该点到全图的最短距离(*self.T[0])

        # 计算每个机关之间的最短距离（起点当成机关）（考虑石头）
        num_machine = len(machines)
        dis_机关到机关 = [[float('inf')]*num_machine for _ in range(num_machine)]
        for 机关1ID, dis_机关1 in enumerate(dis_所有点到机关):
            for 机关2ID in range(机关1ID + 1, num_machine):
                dis_机关到机关[机关1ID][机关2ID] = float('inf')
                for 石头i,石头j in self.O:
                    dis_机关1_石头 = dis_机关1[石头i][石头j]
                    dis_石头_机关2 = dis_所有点到机关[机关2ID][石头i][石头j]
                    # print(机关1ID,机关2ID,石头i,石头j,dis_机关1_石头,dis_石头_机关2)
                    dis_机关到机关[机关1ID][机关2ID] = dis_机关到机关[机关2ID][机关1ID] = min(dis_机关到机关[机关1ID][机关2ID], dis_机关1_石头 + dis_石头_机关2)

        # print('dis_所有点到机关\n',np.array(dis_所有点到机关))#true
        # print('dis_机关到机关\n',np.array(dis_机关到机关))#true

        # 动态规划计算不同触发顺序，触发完所有机关后的最短距离
        num_state = 1 << num_machine    # 二进制表示每个机关是否出发，一共有 2**num_machine 种状态
        dp = [[float('inf')] * num_state for _ in range(num_machine)]   # 对于每个机关，都有 num_state 种状态
        dp[0][1] = 0    # 起点只需要0步就可以触发了

        # 从state=1开始动态规划（也就是只有起点触发了）
        for state in range(1, num_state):
            for 机关1 in range(num_machine):
                if float('inf') == dp[机关1][state]: continue # 机关1的当前状态还没触发（比如：状态1的时候，只有起点触发了）
                for 机关2 in range(num_machine):
                    if state >> 机关2 & 1:continue    # 跳过已经触发了的机关
                    # 触发机关2后的 机关1的状态 = min(触发前的距离 + 机关1到机关2的距离)
                    dp[机关2][state | 1 << 机关2] = min(dp[机关2][state | 1 << 机关2], dp[机关1][state] + dis_机关到机关[机关1][机关2])

        # 所有机关都触发之后（满状态）+ 到终点的最短距离
        ans = min(dis_所有点到终点[i][j] + dp[cur][num_state-1] for cur, (i, j) in enumerate(machines))
        return -1 if ans == float('inf') else ans


def test(data_test):
    s = Solution()
    return s.minimalSteps(*data_test)


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
        [["S#O", "M..", "M.T"]],
        [["..#..", "..#..", "S.#T.", "..#..", "....."]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
