# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 10:49
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : Offer_day04_53 - II. 0～n-1中缺失的数字.py
# @Software: PyCharm
# ===================================
"""一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)


def test(data_test):
    s = Solution()
    return s.missingNumber(*data_test)


if __name__ == '__main__':
    datas = [
        [[0]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
