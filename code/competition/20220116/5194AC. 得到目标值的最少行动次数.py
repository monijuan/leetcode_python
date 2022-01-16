# -*- coding: utf-8 -*-
# @Time    : 2022/1/16 9:14
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5194AC. 得到目标值的最少行动次数.py
# @Software: PyCharm 
# ===================================
"""你正在玩一个整数游戏。从整数 1 开始，期望得到整数 target 。

在一次行动中，你可以做下述两种操作之一：

递增，将当前整数的值加 1（即， x = x + 1）。
加倍，使当前整数的值翻倍（即，x = 2 * x）。
在整个游戏过程中，你可以使用 递增 操作 任意 次数。但是只能使用 加倍 操作 至多 maxDoubles 次。

给你两个整数 target 和 maxDoubles ，返回从 1 开始得到 target 需要的最少行动次数。



示例 1：

输入：target = 5, maxDoubles = 0
输出：4
解释：一直递增 1 直到得到 target 。
示例 2：

输入：target = 19, maxDoubles = 2
输出：7
解释：最初，x = 1 。
递增 3 次，x = 4 。
加倍 1 次，x = 8 。
递增 1 次，x = 9 。
加倍 1 次，x = 18 。
递增 1 次，x = 19 。
示例 3：

输入：target = 10, maxDoubles = 4
输出：4
解释：
最初，x = 1 。
递增 1 次，x = 2 。
加倍 1 次，x = 4 。
递增 1 次，x = 5 。
加倍 1 次，x = 10 。


提示：

1 <= target <= 109
0 <= maxDoubles <= 100
"""
from leetcode_python.utils import *


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target>1:
            if maxDoubles:# //2
                if target&1:#-1
                    res+=1
                res+=1
                target//=2
                maxDoubles-=1
            else:
                res+=(target-1)
                break
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.minMoves(*data)


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
        [5,0],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')