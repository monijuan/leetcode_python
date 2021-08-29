# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 7:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1588. 所有奇数长度子数组的和.py
# @Software: PyCharm
# ===================================
"""给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

 

示例 1：

输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
示例 2：

输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
示例 3：

输入：arr = [10,11,12]
输出：66

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List

class Solution:
    def __init__(self):
        pass

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        length = len(arr)
        for i in range(length):
            # print('-'*20)
            # print(f'i={i}')
            times = 0
            for w in range(1,length+1,2):
                time = min(i+1,length-i,w,length-w+1)
                times+=time
                # print(f'i:{i}, w:{w}, time:{time}')
            res+=times*arr[i]
            # print(f'[res]n:{length}, i:{i}, times:{times}, sum:{arr[i]}*{times}={times*arr[i]}')

        return res


def test(data_test):
    s = Solution()
    return s.sumOddLengthSubarrays(*data_test)

if __name__ == '__main__':
    datas = [
        [[1,4,2,5,3]],
        [[1,4,2,5,4,2,5,4,2,5,3]],
        # [[10,11,12]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')