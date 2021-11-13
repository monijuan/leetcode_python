# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 22:34
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5911AC. 模拟行走机器人 II.py
# @Software: PyCharm 
# ===================================
"""给你一个在 XY 平面上的 width x height 的网格图，左下角 的格子为 (0, 0) ，右上角 的格子为 (width - 1, height - 1) 。网格图中相邻格子为四个基本方向之一（"North"，"East"，"South" 和 "West"）。一个机器人 初始 在格子 (0, 0) ，方向为 "East" 。

机器人可以根据指令移动指定的 步数 。每一步，它可以执行以下操作。

沿着当前方向尝试 往前一步 。
如果机器人下一步将到达的格子 超出了边界 ，机器人会 逆时针 转 90 度，然后再尝试往前一步。
如果机器人完成了指令要求的移动步数，它将停止移动并等待下一个指令。

请你实现 Robot 类：

Robot(int width, int height) 初始化一个 width x height 的网格图，机器人初始在 (0, 0) ，方向朝 "East" 。
void move(int num) 给机器人下达前进 num 步的指令。
int[] getPos() 返回机器人当前所处的格子位置，用一个长度为 2 的数组 [x, y] 表示。
String getDir() 返回当前机器人的朝向，为 "North" ，"East" ，"South" 或者 "West" 。


示例 1：

example-1

输入：
["Robot", "move", "move", "getPos", "getDir", "move", "move", "move", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
输出：
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

解释：
Robot robot = new Robot(6, 3); // 初始化网格图，机器人在 (0, 0) ，朝东。
robot.move(2);  // 机器人朝东移动 2 步，到达 (2, 0) ，并朝东。
robot.move(2);  // 机器人朝东移动 2 步，到达 (4, 0) ，并朝东。
robot.getPos(); // 返回 [4, 0]
robot.getDir(); // 返回 "East"
robot.move(2);  // 朝东移动 1 步到达 (5, 0) ，并朝东。
                // 下一步继续往东移动将出界，所以逆时针转变方向朝北。
                // 然后，往北移动 1 步到达 (5, 1) ，并朝北。
robot.move(1);  // 朝北移动 1 步到达 (5, 2) ，并朝 北 （不是朝西）。
robot.move(4);  // 下一步继续往北移动将出界，所以逆时针转变方向朝西。
                // 然后，移动 4 步到 (1, 2) ，并朝西。
robot.getPos(); // 返回 [1, 2]
robot.getDir(); // 返回 "West"



提示：

2 <= width, height <= 100
1 <= num <= 105
move ，getPos 和 getDir 总共 调用次数不超过 104 次。
"""
from leetcode_python.utils import *


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__direction_move = {
            "East":[1,0],
            "North":[0,1],
            "West":[-1,0],
            "South":[0,-1],
        }
        self.__direction_li = ["East","North","West","South"]
        self.__direction_id = 0
        self.pos = [0,0]
        self.__round = 2 * (width+height) - 4
        self.first = True

    def __move_one_wrong(self):
        """走完就掉头"""
        self.pos = [a+b for a,b in zip(self.pos,self.__direction_move[self.__direction_li[self.__direction_id]])]
        next_pos = [a+b for a,b in zip(self.pos,self.__direction_move[self.__direction_li[self.__direction_id]])]
        if not (0<=next_pos[0]<self.width and 0<=next_pos[1]<self.height):
            self.__direction_id = (self.__direction_id + 1) % 4


    def __move_one(self):
        """走前掉头"""
        next_pos = [a+b for a,b in zip(self.pos,self.__direction_move[self.__direction_li[self.__direction_id]])]
        if 0<=next_pos[0]<self.width and 0<=next_pos[1]<self.height:
            self.pos = next_pos
        else:
            self.__direction_id = (self.__direction_id + 1) % 4
            self.__move_one()


    def move(self, num: int) -> None:
        num = num % self.__round
        if num==0 and self.first:       # 最后三个case的坑！！！第一次从起点出发绕一圈回来的话，pos没变，方向从east变成了south
            self.__direction_id = 3
        self.first=False
        while num:
            self.__move_one()
            num-=1
        return


    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.__direction_li[self.__direction_id]
        # return list(self.__direction_move.keys())[self.__direction_id]


def test_obj(data_test):
    result = [None]
    obj = Robot(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        # [["Robot","move","move","getPos","getDir","move","move","move","getPos","getDir"],[[6,3],[2],[2],[],[],[2],[1],[4],[],[]]],
        [["Robot","move","move","move","move","getPos","getDir","move","move","move","move","getPos","getDir","move","move","getPos","getDir","move","move","move","move","move","getPos"],[[4,5],[44],[19],[8],[36],[],[],[17],[49],[14],[40],[],[],[18],[7],[],[],[8],[5],[2],[36],[22],[]]],
        # [["Robot","move","move","move","move","getPos","getDir","move","move","move","move","getPos","getDir","move","move","getPos","getDir","move","move","move","move","move","getPos"],[[4,5],[44],[19],[8],[36],[],[],[17],[49],[14],[40],[],[],[18],[7],[],[],[8],[5],[2],[36],[22],[]]],
        # [["Robot","move","move","getPos","getDir","move","getPos","getDir","getPos","getDir"],[[20,13],[12],[21],[],[],[17],[],[],[],[]]],
        # [["Robot","move","getPos","getDir","move","getPos","getDir","move","getPos","getDir","move","move","move","move","getPos","getDir","move","move","getPos","getDir","move","move","getPos","getDir","move","move","getPos","getDir","move","getPos","getDir","move","move","move","move","move","getPos","getDir","move","move"],[[2,10],[19170],[],[],[94934],[],[],[11550],[],[],[93188],[79826],[37114],[63011],[],[],[80727],[45627],[],[],[71034],[25698],[],[],[31724],[5511],[],[],[77037],[],[],[81611],[18532],[18036],[72341],[34177],[],[],[88715],[40490]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')