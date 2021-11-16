# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 13:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 14. 切分数组.py
# @Software: PyCharm
# ===================================
"""给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。

示例 1：

输入：nums = [2,3,3,2,3,3]

输出：2

解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。

示例 2：

输入：nums = [2,3,5,7]

输出：4

解释：只有一种可行的切割：[2], [3], [5], [7]

限制：

1 <= nums.length <= 10^5
2 <= nums[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qie-fen-shu-zu
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def initFactor(self,maxsize):
        self.left_factor = [0]*maxsize
        for num in range(2,maxsize):
            if not self.left_factor[num]:
                for j in range(num,maxsize,num):
                    self.left_factor[j] = num

    def splitArray(self, nums: List[int]) -> int:
        max_size = max(nums) + 1
        self.initFactor(max_size)
        res_last = 0
        length = len(nums)
        dp = [length]*max_size
        for num in nums:
            res_now = length
            while num>1:
                num_f = self.left_factor[num]
                while self.left_factor[num]==num_f: num//=num_f
                dp[num_f] = min(dp[num_f],res_last)
                res_now = min(res_now,dp[num_f]+1)
            res_last = res_now
        return res_last


def test(data_test):
    s = Solution()
    return s.splitArray(*data_test)


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
        [[2,3,3,2,3,3]],
        [[2,3,5,7]],
        [[2]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
