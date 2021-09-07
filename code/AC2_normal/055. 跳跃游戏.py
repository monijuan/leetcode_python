# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 20:05
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 055. 跳跃游戏.py
# @Software: PyCharm 
# ===================================
"""
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        jump_remain = 1
        for id,num in enumerate(nums):
            if id+jump_remain>=length:
                return True
            elif jump_remain:
                jump_remain = max(jump_remain-1,nums[id])
            else:
                return False


def test(data_test):
    s = Solution()
    return s.canJump(*data_test)


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
        [[2,3,1,1,4]],
        [[3,2,1,0,4]],
        [[2,0]],
        [[0,1]],
        [[0]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')