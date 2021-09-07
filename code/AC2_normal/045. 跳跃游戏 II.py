# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 20:40
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 045. 跳跃游戏 II.py
# @Software: PyCharm 
# ===================================
"""给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
 

提示:

1 <= nums.length <= 104
0 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        jump_remain = 1
        next_remain = 0
        jump_times = 0
        id=0
        while 1:
            if id==length-1:
                return jump_times
            elif jump_remain:
                jump_remain-=1
                next_remain=max(next_remain-1,jump_remain,nums[id])
                id+=1
            if jump_remain==0 and next_remain:
                jump_remain = next_remain
                jump_times+=1

def test(data_test):
    s = Solution()
    return s.jump(*data_test)

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
        # [[2,3,1,1,4]],
        # [[2,3,0,1,4]],
        # [[0]],
        # [[2,1,1]],
        [[1,2]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')