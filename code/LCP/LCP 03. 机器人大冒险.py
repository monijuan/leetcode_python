# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 10:39
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 03. 机器人大冒险.py
# @Software: PyCharm
# ===================================
"""力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

 

示例 1：

输入：command = "URR", obstacles = [], x = 3, y = 2
输出：true
解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
示例 2：

输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
输出：false
解释：机器人在到达终点前会碰到(2, 2)的障碍物。
示例 3：

输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
输出：true
解释：到达终点后，再碰到障碍物也不影响返回结果。
 

限制：

2 <= command的长度 <= 1000
command由U，R构成，且至少有一个U，至少有一个R
0 <= x <= 1e9, 0 <= y <= 1e9
0 <= obstacles的长度 <= 1000
obstacles[i]不为原点或者终点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/programmable-robot
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

"""
## False
"RUUR"
[[10, 5], [1, 6], [6, 10], [3, 0], [0, 3], [0, 10], [6, 2]]
7856
9033

## True
"URRURRR"
[[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]]
4915
1966
"""
mapc = {'U': 1, 'R': 0}
class Solution:
    def couldmeet(self, posadd):
        pos = [0,0]
        k = min(posadd[0]//self.posloop[0],posadd[1]//self.posloop[1])
        posadd = [posadd[0]-k*self.posloop[0],posadd[1]-k*self.posloop[1]]
        if posadd==[0,0]:return True
        for c in self.command:
            pos[mapc[c]]+=1
            if pos==posadd:return True
        return False

    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        self.command = command
        self.posloop = [command.count('R'),command.count('U')]
        if not self.couldmeet([x,y]):return False
        if any(posobs[0]<=x and posobs[1]<=y and self.couldmeet(posobs) for posobs in obstacles):return False
        return True

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.robot(*data)


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
        # ["RUUR",[[10, 5], [1, 6], [6, 10], [3, 0], [0, 3], [0, 10], [6, 2]],7856,9033],
        ["URRURRR", [[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]],4915,1966],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
