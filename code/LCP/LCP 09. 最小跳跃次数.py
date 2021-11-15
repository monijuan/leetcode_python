# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 17:09
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 09. 最小跳跃次数.py
# @Software: PyCharm
# ===================================
"""2020 春赛题集
为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。

为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

示例 1：

输入：jump = [2, 5, 1, 1, 1, 1]

输出：3

解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。

限制：

1 <= jump.length <= 10^6
1 <= jump[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        超时case：https://leetcode-cn.com/submissions/detail/238701415/testcase/
        """
        pass

    def minJump(self, jump: List[int]) -> int:
        length = len(jump)
        jump_from = [0]*length
        for start in range(length-1,-1,-1):
            if start + jump[start] >= length:
                jump_from[start] = 1    # 直接跳出去
            else:
                jump_from[start] = 1 + jump_from[start+jump[start]] # 需要继续跳

            # 更新后面的，如果发现回跳会更快，则必须要更新。因为可能一下子先跳到后面
            jump_from_now = jump_from[start]
            for start_behind in range(start+1,length):
                # jump_from[start_behind] = min(jump_from[start_behind],jump_from_now+1)    # 这样会超时，需要break优化
                if jump_from[start_behind]<=jump_from_now:
                    break
                else:
                    jump_from[start_behind] = jump_from_now+1
            # print(start,jump_from)    # 有print会超时
        return jump_from[0]


def test(data_test):
    s = Solution()
    return s.minJump(*data_test)


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
        [[2,5,1,1,1,1]],
        [[2,5,1,6,5,1,1,1,5,1,5,1,22,5,1,5,1,1]],
        [[2,5,1,600,5,1,1,1,500,1,5,1,22,5,1,5,1,1]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
