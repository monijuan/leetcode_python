# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 21:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6054. 逃离火灾.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：

0 表示草地。
1 表示着火的格子。
2 表示一座墙，你跟火都不能通过这个格子。
一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。

请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 109 。

注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。

如果两个格子有共同边，那么它们为 相邻 格子。



示例 1：



输入：grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
输出：3
解释：上图展示了你在初始位置停留 3 分钟后的情形。
你仍然可以安全到达安全屋。
停留超过 3 分钟会让你无法安全到达安全屋。
示例 2：



输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
输出：-1
解释：上图展示了你马上开始朝安全屋移动的情形。
火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。
所以返回 -1 。
示例 3：



输入：grid = [[0,0,0],[2,2,0],[1,2,0]]
输出：1000000000
解释：上图展示了初始网格图。
注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。
所以返回 109 。


提示：

m == grid.length
n == grid[i].length
2 <= m, n <= 300
4 <= m * n <= 2 * 104
grid[i][j] 是 0 ，1 或者 2 。
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from leetcode_python.utils import *


class Solution_wa:
    @lru_cache(None)
    def next(self, rowid, colid):
        res = []
        for i, j in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= i < self.height and 0 <= j < self.width and self.grid[i][j] != 2:
                res.append([i, j])
        return res

    def maximumMinutes(self, grid: List[List[int]]) -> int:
        self.height, self.width = len(grid), len(grid[0])
        self.grid = grid

        # 计算火苗烧到每个位置需要的时间
        time_fire = [[float('inf')] * self.width for _ in range(self.height)]
        fires = []
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    fires.append((i, j, 0))
        while fires:
            i, j, t = fires.pop(0)
            if t < time_fire[i][j]:
                time_fire[i][j] = t
                for i_, j_ in self.next(i, j):
                    fires.append((i_, j_, t + 1))
        # time_fire[self.height-1][self.width-1]=float('inf')
        # for l in time_fire:print(l)

        min_step = [[float('inf')] * self.width for _ in range(self.height)]
        routes = []
        minstep = self.width + self.height

        routes_ = [((0, 0),[],0)]
        # def dfs(now, route, step):
        #     nonlocal routes
        while routes_:
            (x, y),r_,step = routes_.pop(0)
            if min_step[x][y] < step:
                continue
            min_step[x][y] = step
            print(x,y,step)
            if (x, y) == (self.height - 1, self.width - 1):
                print(x,y,step,minstep)
                if step < minstep:
                    routes = [r_]
                elif step == minstep:
                    routes.append(r_)
                continue
            for i, j in self.next(x,y):
                routes_.append(((i, j), r_ + [(i, j)], step + 1))
            # print(routes)

        # dfs((0, 0), [], 0)
        if len(routes) == 0:
            return -1
        END = (self.height-1,self.width-1)
        # print(routes)
        # 遍历每条路线
        res = float('inf')
        for route in routes:
            step = 0
            mindiss = float('inf')
            continued = False
            for x, y in route:
                if (x,y)==END:
                    mindiss = min(mindiss, time_fire[x][y] - step-1)
                    print(mindiss)
                    break
                step += 1
                diss = time_fire[x][y] - step-1
                print(x,y,diss)
                if diss>=0:
                    mindiss = min(mindiss, diss)
                else:
                    res = -1
                    continued = True
                    break
            if continued:continue
            if mindiss != float('inf'):
                if res == float('inf'):res=0
                res = max(res,mindiss)
        return res if res!=float('inf') else 10**9

class Solution_tle:
    @lru_cache(None)
    def next(self, rowid, colid):
        res = []
        for i, j in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= i < self.height and 0 <= j < self.width and self.grid[i][j] != 2:
                res.append([i, j])
        return res

    def maximumMinutes(self, grid: List[List[int]]) -> int:
        self.height, self.width = len(grid), len(grid[0])
        self.grid = grid

        # 计算火苗烧到每个位置需要的时间
        time_fire = [[float('inf')] * self.width for _ in range(self.height)]
        fires = []
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    fires.append((i, j, 0))
        while fires:
            i, j, t = fires.pop(0)
            if t < time_fire[i][j]:
                time_fire[i][j] = t
                for i_, j_ in self.next(i, j):
                    fires.append((i_, j_, t + 1))
        # time_fire[self.height-1][self.width-1]=float('inf')
        for l in time_fire:print(l)

        min_step = [[float('inf')] * self.width for _ in range(self.height)]
        routes = []
        minstep = self.width + self.height

        def dfs(now, route, step):
            nonlocal routes
            x, y = now
            if min_step[x][y] < step:
                return
            min_step[x][y] = step
            if now == (self.height - 1, self.width - 1):
                if step < minstep:
                    routes = [route]
                elif step == minstep:
                    routes.append(route)
                return
            for i, j in self.next(*now):
                dfs((i, j), route + [(i, j)], step + 1)

        dfs((0, 0), [], 0)
        if len(routes) == 0:
            return -1
        END = (self.height-1,self.width-1)
        print(routes)
        # 遍历每条路线
        res = float('inf')
        for route in routes:
            step = 0
            mindiss = float('inf')
            continued = False
            for x, y in route:
                if (x,y)==END:
                    mindiss = min(mindiss, time_fire[x][y] - step-1)
                    print(mindiss)
                    break
                step += 1
                diss = time_fire[x][y] - step-1
                # print(x,y,diss)
                if diss>=0:
                    mindiss = min(mindiss, diss)
                else:
                    res = -1
                    continued = True
                    break
            if continued:continue
            if mindiss != float('inf'):
                if res == float('inf'):res=0
                res = max(res,mindiss)
        return res if res!=float('inf') else 10**9


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.maximumMinutes(*data)


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
        # [[[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2], [0, 0, 0, 0, 0, 0, 0]]],
        # [[[0,0,0,0],[0,1,2,0],[0,2,0,0]]],
        # [[[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]]],
        # [[[0,1],[0,2],[0,0],[2,0]]],
        [[[0,1,1,2,0,2,2,2,1,1,0,0,2,2,0,0,2,2,1,2,1,0,0,0],[2,0,2,2,1,0,2,2,2,1,2,0,2,2,2,0,2,1,1,1,0,1,1,1],[2,0,1,0,1,0,1,0,0,0,2,1,0,2,0,1,1,0,0,2,1,0,1,2],[1,2,0,0,0,2,2,2,1,2,0,2,1,1,1,0,2,1,1,0,2,2,2,1],[2,1,0,1,0,1,2,0,0,0,2,1,1,2,1,2,1,1,2,1,0,2,1,0],[0,0,2,1,1,1,0,1,0,2,1,2,0,0,2,2,0,1,0,0,1,0,1,1],[0,0,1,2,1,2,2,2,1,1,0,0,2,2,0,1,0,2,2,2,1,2,1,0],[0,2,0,2,1,1,0,2,2,1,0,1,1,2,2,1,2,1,1,2,1,0,1,0],[2,0,1,1,0,1,2,0,2,1,1,2,2,1,0,2,2,1,0,0,0,0,1,1],[0,1,1,2,2,1,2,0,1,1,2,1,0,0,1,0,2,0,2,1,1,1,1,2],[0,1,0,0,2,0,0,2,0,1,2,1,2,2,2,1,0,1,0,0,1,1,0,2],[1,1,0,0,0,2,2,0,1,1,0,2,0,0,0,0,1,2,1,1,1,2,2,0],[0,2,1,0,2,0,0,1,1,2,0,2,0,0,0,2,2,0,2,1,1,2,2,2],[0,0,2,1,1,1,1,1,2,0,1,0,2,2,1,1,1,0,0,0,1,2,2,1],[2,0,1,2,0,0,1,1,1,0,0,2,0,0,2,0,1,1,2,2,0,1,0,0],[0,2,0,0,0,1,1,0,2,1,1,1,2,1,2,0,0,2,2,0,0,0,2,1],[0,0,0,0,1,1,2,1,2,1,1,0,1,0,1,1,1,0,0,2,1,2,2,2],[2,0,2,1,2,2,2,2,0,2,1,2,0,0,0,2,1,2,2,2,1,2,0,0],[2,0,0,0,1,1,2,0,2,0,1,2,1,1,1,0,2,1,1,0,2,2,2,1],[2,2,0,2,2,2,0,0,0,1,2,2,2,1,1,1,2,2,0,0,1,1,2,0]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
