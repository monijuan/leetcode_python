# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 9:56
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 689. 三个无重叠子数组的最大和.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。

 

示例 1：

输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
示例 2：

输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        sum2, maxSum12, maxSum12Idx = 0, 0, ()
        sum3, maxTotal = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i - k * 3 + 1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.maxSumOfThreeSubarrays(*data)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
