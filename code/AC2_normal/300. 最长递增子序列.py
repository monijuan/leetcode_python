# -*- coding: utf-8 -*-
# @Time    : 2021/9/20 23:21
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 300. 最长递增子序列.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        """看的官方"""
        pass

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp  or num>dp[-1]:
                dp.append(num)
            else:
                left,right = 0,len(dp)-1
                index = right
                while left<=right:
                    mid = left+(right-left)//2
                    if dp[mid]>=num:
                        index = mid
                        right=mid-1
                    else:
                        left=mid+1
                dp[index] = num
        return len(dp)




    def lengthOfLIS_动态规划(self, nums: List[int]) -> int:
        if not nums:return 0
        dp = [1]*len(nums)
        for right in range(len(nums)):
            for left in range(right):
                if nums[left]<nums[right]:
                    dp[right] = max(dp[right],dp[left]+1)
        return max(dp)

def test(data_test):
    s = Solution()
    return s.lengthOfLIS(*data_test)


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
        [[10,9,2,5,3,7,101,18]],
        [[0,1,0,3,2,3]],
        [[7,7,7,7,7,7,7]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')