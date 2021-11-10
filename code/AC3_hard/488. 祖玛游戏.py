# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 9:03
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 488. 祖玛游戏.py
# @Software: PyCharm
# ===================================
"""你正在参与祖玛游戏的一个变种。

在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。

你的目标是 清空 桌面上所有的球。每一回合：

从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
如果桌面上所有球都被移除，则认为你赢得本场游戏。
重复这个过程，直到你赢了游戏或者手中没有更多的球。
给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。

 

示例 1：

输入：board = "WRRBBW", hand = "RB"
输出：-1
解释：无法移除桌面上的所有球。可以得到的最好局面是：
- 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
- 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
桌面上还剩着球，没有其他球可以插入。
示例 2：

输入：board = "WWRRBBWW", hand = "WRBRW"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
- 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
只需从手中出 2 个球就可以清空桌面。
示例 3：

输入：board = "G", hand = "GGGGG"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'G' ，使桌面变为 GG 。
- 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty
只需从手中出 2 个球就可以清空桌面。
示例 4：

输入：board = "RBYYBBRRB", hand = "YRBGB"
输出：3
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B
- 插入一个 'B' ，使桌面变为 BB 。
- 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty
只需从手中出 3 个球就可以清空桌面。
 

提示：

1 <= board.length <= 16
1 <= hand.length <= 5
board 和 hand 由字符 'R'、'Y'、'B'、'G' 和 'W' 组成
桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zuma-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *
import collections

class Solution:
    def __init__(self):
        '''
        ['RRWWRRBBRR', 'WB']
            RRWWRRBBRR -> RRWWRRBBRWR -> RRWWRRBBBRWR -> RRWWRRRWR -> RRWWWR -> RRR -> ”“

        ["BGGRRYY","BBYRG"]
            共需要5次，不加保留缓存会超时
        '''
        self.res = -1

    @lru_cache(None)
    def remove(self,board):
        length = len(board)
        left = 0
        while left<length:
            right = left
            while right<length and board[left]==board[right]: right+=1
            if right-left>=3: return self.remove(board[:left]+board[right:])
            else: left = right
        return board

    @lru_cache(None)
    def dfs(self,board,time=0):
        length = len(board)
        if 0==length:
            if self.res == -1:self.res=time
            else: self.res = min(self.res,time)
            return
        elif self.res!=-1 and time>self.res:
            return

        for id,char in enumerate(board):
            for color in self.hand.keys():
                if self.hand[color]>0:
                    self.hand[color] = self.hand[color]-1
                    if 0==id:
                        new_board = color + board
                    else:
                        new_board = board[:id] + color + board[id:]
                    # print(new_board,self.hand,time,color)
                    self.dfs(self.remove(new_board),time+1)
                    self.hand[color] = self.hand[color]+1

    def dfs_可以解决大部分问题(self,board,time=0):
        """对于需要插在不同颜色中间才能解决的问题，这样就不行"""
        length = len(board)
        if 0==length:
            self.res = min(self.res,time)
            return
        elif time>self.res:
            return

        last_char = None
        for id,char in enumerate(board):
            if 0==id or char != last_char: last_char=char
            else: continue

            if self.hand.get(char,0)>0:
                self.hand[char] = self.hand[char]-1
                if 0==id:
                    new_board = char + board
                else:
                    new_board = board[:id] + char + board[id:]
                print(new_board,self.hand,time,char)
                self.dfs(self.remove(new_board),time+1)
                self.hand[char] = self.hand[char]+1


    def findMinStep(self, board: str, hand: str) -> int:
        self.hand = collections.Counter(hand)
        self.dfs(board)
        return self.res


def test(data_test):
    s = Solution()
    return s.findMinStep(*data_test)


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
    # s = Solution()
    # res = s.remove('asdasddsssa')
    # print(res)
    datas = [
        # ["WRRBBW","RB"],
        # ["RBYYBBRRB","YRBGB"],
        # ["WWRRBBWW","WRBRW"],
        # ["RRWWRRBBRR","WB"],
        ["BGGRRYY","BBYRG"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
