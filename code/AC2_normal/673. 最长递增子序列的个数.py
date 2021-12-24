# -*- coding: utf-8 -*-
# @Time    : 2021/9/20 23:17
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 673. 最长递增子序列的个数.py
# @Software: PyCharm 
# ===================================
"""给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

def bisect(n: int, function: Callable[[int], bool]) -> int:
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if function(mid):
            right = mid
        else:
            left = mid + 1
    return left

class Solution:
    def __init__(self):
        """
        参考基础版： 300. 最长递增子序列.py
        看的官方
        """
        pass

    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp, cnt = [], []
        for num in nums:
            i = bisect(len(dp), lambda i: dp[i][-1] >= num)
            c = 1
            if i > 0:
                k = bisect(len(dp[i - 1]), lambda k: dp[i - 1][k] < num)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(dp):
                dp.append([num])
                cnt.append([0, c])
            else:
                dp[i].append(num)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]

    def findNumberOfLIS2(self, nums: List[int]) -> int:
        """300. 最长递增子序列"""
        dp,cnt = [],[]
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


def test(data_test):
    s = Solution()
    return s.findNumberOfLIS(*data_test)


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
        [[1,3,5,4,7]],
         [[2,2,2,2,2]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')