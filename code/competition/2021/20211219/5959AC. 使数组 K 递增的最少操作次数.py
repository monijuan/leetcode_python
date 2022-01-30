# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5959AC. 使数组 K 递增的最少操作次数.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始包含 n 个正整数的数组 arr ，和一个正整数 k 。

如果对于每个满足 k <= i <= n-1 的下标 i ，都有 arr[i-k] <= arr[i] ，那么我们称 arr 是 K 递增 的。

比方说，arr = [4, 1, 5, 2, 6, 2] 对于 k = 2 是 K 递增的，因为：
arr[0] <= arr[2] (4 <= 5)
arr[1] <= arr[3] (1 <= 2)
arr[2] <= arr[4] (5 <= 6)
arr[3] <= arr[5] (2 <= 2)
但是，相同的数组 arr 对于 k = 1 不是 K 递增的（因为 arr[0] > arr[1]），对于 k = 3 也不是 K 递增的（因为 arr[0] > arr[3] ）。
每一次 操作 中，你可以选择一个下标 i 并将 arr[i] 改成任意 正整数。

请你返回对于给定的 k ，使数组变成 K 递增的 最少操作次数 。



示例 1：

输入：arr = [5,4,3,2,1], k = 1
输出：4
解释：
对于 k = 1 ，数组最终必须变成非递减的。
可行的 K 递增结果数组为 [5,6,7,8,9]，[1,1,1,1,1]，[2,2,3,4,4] 。它们都需要 4 次操作。
次优解是将数组变成比方说 [6,7,8,9,10] ，因为需要 5 次操作。
显然我们无法使用少于 4 次操作将数组变成 K 递增的。
示例 2：

输入：arr = [4,1,5,2,6,2], k = 2
输出：0
解释：
这是题目描述中的例子。
对于每个满足 2 <= i <= 5 的下标 i ，有 arr[i-2] <= arr[i] 。
由于给定数组已经是 K 递增的，我们不需要进行任何操作。
示例 3：

输入：arr = [4,1,5,2,6,2], k = 3
输出：2
解释：
下标 3 和 5 是仅有的 3 <= i <= 5 且不满足 arr[i-3] <= arr[i] 的下标。
将数组变成 K 递增的方法之一是将 arr[3] 变为 4 ，且将 arr[5] 变成 5 。
数组变为 [4,1,5,4,6,5] 。
可能有其他方法将数组变为 K 递增的，但没有任何一种方法需要的操作次数小于 2 次。


提示：

1 <= arr.length <= 105
1 <= arr[i], k <= arr.length
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def lengthOfLIS_超时(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1]*length
        for i in range(length):
            for j in range(0,i):
                if nums[j]<=nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
        return max(dp)


    def lengthOfLIS(self, nums: List[int]) -> int:
        """最长非递减子数组"""
        dp = []
        for num in nums:
            j = bisect.bisect_left(dp,num+1)
            if j==len(dp):
                dp.append(num)
            else:
                dp[j]=num
        return len(dp)

    def kIncreasing(self, arr: List[int], k: int) -> int:
        res = 0
        length = len(arr)
        for i in range(k):
            li = arr[i:length:k]
            res += (len(li) - self.lengthOfLIS(li))
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.kIncreasing(*data)


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
        [[5,4,3,2,1],2],
        [[4,1,5,2,6,2],2],
        [[4,1,5,2,6,2],3],
        [[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3],1],
        [[2,2,2,2,2,1,1,4,4,3,3,3,3,3],1],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')