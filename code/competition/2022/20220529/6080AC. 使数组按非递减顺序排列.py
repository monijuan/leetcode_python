# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 10:18
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6080AC. 使数组按非递减顺序排列.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 < i < nums.length 。

重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。



示例 1：

输入：nums = [5,3,4,4,7,3,6,11,8,5,11]
输出：3
解释：执行下述几个步骤：
- 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11]
- 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11]
- 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11]
[5,7,11,11] 是一个非递减数组，因此，返回 3 。
示例 2：

输入：nums = [4,5,7,7,13]
输出：0
解释：nums 已经是一个非递减数组，因此，返回 0 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from leetcode_python.utils import *


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            cur = 0
            while stack and nums[stack[-1][0]] < nums[i]:
                _, v = stack.pop()
                cur = max(cur + 1, v)
            res = max(res, cur)
            stack.append([i, cur])
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.totalSteps(*data)


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
        # [[5,3,4,4,7,3,6,11,8,5,11]],
        [[10, 1, 2, 3, 4, 5, 6, 1, 2, 3]],
        [[7, 14, 4, 14, 13, 2, 6, 13]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
