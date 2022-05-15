# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 8:39
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1728. 猫和老鼠 II.py
# @Software: PyCharm 
# ===================================
"""一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。

它们所处的环境设定是一个 rows x cols 的方格 grid ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。

玩家由字符 'C' （代表猫）和 'M' （代表老鼠）表示。
地板由字符 '.' 表示，玩家可以通过这个格子。
墙用字符 '#' 表示，玩家不能通过这个格子。
食物用字符 'F' 表示，玩家可以通过这个格子。
字符 'C' ， 'M' 和 'F' 在 grid 中都只会出现一次。
猫和老鼠按照如下规则移动：

老鼠 先移动 ，然后两名玩家轮流移动。
每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 grid 。
catJump 和 mouseJump 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。
它们可以停留在原地。
老鼠可以跳跃过猫的位置。
游戏有 4 种方式会结束：

如果猫跟老鼠处在相同的位置，那么猫获胜。
如果猫先到达食物，那么猫获胜。
如果老鼠先到达食物，那么老鼠获胜。
如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。
给你 rows x cols 的矩阵 grid 和两个整数 catJump 和 mouseJump ，双方都采取最优策略，如果老鼠获胜，那么请你返回 true ，否则返回 false 。

 

示例 1：



输入：grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
输出：true
解释：猫无法抓到老鼠，也没法比老鼠先到达食物。
示例 2：



输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4
输出：true
示例 3：

输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3
输出：false
示例 4：

输入：grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
输出：false
示例 5：

输入：grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
输出：true
 

提示：

rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] 只包含字符 'C' ，'M' ，'F' ，'.' 和 '#' 。
grid 中只包含一个 'C' ，'M' 和 'F' 。
1 <= catJump, mouseJump <= 8

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/cat-and-mouse-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        mm, nn = len(grid), len(grid[0])
        for x in range(mm):
            for y in range(nn):
                match grid[x][y]:
                    case 'C':
                        cat = x, y
                    case 'F':
                        food = x, y
                    case 'M':
                        mouse = x, y

        @lru_cache(None)
        def dfs(m, c, i):
            """
            极大极小博弈，
            老鼠尽量找自己获胜的，其次接受平局
            猫尽量找自己获胜的，其次接受平局

            :param m: 老鼠的位置
            :param c: 猫的位置
            :param i: 回合
            """
            if m == c or c == food or i > 128:
                return False
            if m == food:
                return True
            is_cat = False
            # 猫回合
            if i % 2:
                pos, jump = c, catJump
                is_cat = True
            else:
                pos, jump = m, mouseJump
            for dx, dy in DIRS:
                for jp in range(jump + 1):
                    nx, ny = pos[0] + dx * jp, pos[1] + dy * jp
                    if nx < 0 or ny < 0 or nx >= mm or ny >= nn or grid[nx][ny] == '#':
                        break
                    if not is_cat and dfs((nx, ny), c, i + 1):
                        return True
                    elif is_cat and not dfs(m, (nx, ny), i + 1):
                        return False
            return is_cat

        return dfs(mouse, cat, 0)




def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
