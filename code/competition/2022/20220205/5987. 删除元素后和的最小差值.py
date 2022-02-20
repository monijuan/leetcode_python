# -*- coding: utf-8 -*-
# @Time    : 2022/2/5 22:21
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5987. 删除元素后和的最小差值.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。

你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。

前面 n 个元素属于第一部分，它们的和记为 sumfirst 。
后面 n 个元素属于第二部分，它们的和记为 sumsecond 。
两部分和的 差值 记为 sumfirst - sumsecond 。

比方说，sumfirst = 3 且 sumsecond = 2 ，它们的差值为 1 。
再比方，sumfirst = 2 且 sumsecond = 3 ，它们的差值为 -1 。
请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。



示例 1：

输入：nums = [3,1,2]
输出：-1
解释：nums 有 3 个元素，所以 n = 1 。
所以我们需要从 nums 中删除 1 个元素，并将剩下的元素分成两部分。
- 如果我们删除 nums[0] = 3 ，数组变为 [1,2] 。两部分和的差值为 1 - 2 = -1 。
- 如果我们删除 nums[1] = 1 ，数组变为 [3,2] 。两部分和的差值为 3 - 2 = 1 。
- 如果我们删除 nums[2] = 2 ，数组变为 [3,1] 。两部分和的差值为 3 - 1 = 2 。
两部分和的最小差值为 min(-1,1,2) = -1 。
示例 2：

输入：nums = [7,9,5,8,1,3]
输出：1
解释：n = 2 。所以我们需要删除 2 个元素，并将剩下元素分为 2 部分。
如果我们删除元素 nums[2] = 5 和 nums[3] = 8 ，剩下元素为 [7,9,1,3] 。和的差值为 (7+9) - (1+3) = 12 。
为了得到最小差值，我们应该删除 nums[1] = 9 和 nums[4] = 1 ，剩下的元素为 [7,5,8,3] 。和的差值为 (7+5) - (8+3) = 1 。
观察可知，最优答案为 1 。


提示：

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105
"""
from leetcode_python.utils import *

import heapq

from sortedcontainers import SortedList
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        def getsum(nums):
            ss = SortedList(nums[:n])
            res = [sum(ss)]
            for i in range(n,2*n):
                ss.add(nums[i])
                res.append(sum(ss[:n]))
            return res
        sumleft = getsum(nums)
        nums = [-x for x in nums[::-1]]
        sumright = getsum(nums)[::-1]
        res = min(l+r for l,r in zip(sumleft,sumright))
        return res

    def getResult2(self, args):
        n = len(args)//3
        print(args[:2*n])
        print(sorted(args[:2*n]))
        print(sorted(args[:2*n])[:n])
        lefts = sorted(args[:2*n])[:n]
        rights = sorted(args[n:])[n:]
        return sum(lefts)-sum(rights)

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.minimumDifference(*data)

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
        # [[7,9,5,8,1,3]],
        # [[3,1,2]],
        [[16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

