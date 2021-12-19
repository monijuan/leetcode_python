# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 12:19
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 674. 最长连续递增序列.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def lengthOfLIS_非递减(self, nums: List[int]) -> int:
        """最长非递减子数组"""
        dp = []
        for num in nums:
            j = bisect.bisect_left(dp,num+1)
            if j==len(dp):
                dp.append(num)
            else:
                dp[j]=num
        return len(dp)

    def lengthOfLIS_严格递增(self, nums: List[int]) -> int:
        """最长递增子数组"""
        dp = []
        for num in nums:
            j = bisect.bisect_left(dp,num)
            if j==len(dp):
                dp.append(num)
            else:
                dp[j]=num
        return len(dp)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.findLengthOfLCIS(*data)


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
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')