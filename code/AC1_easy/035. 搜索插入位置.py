# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 17:06
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 035. 搜索插入位置.py
# @Software: PyCharm
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<=nums[0]:return 0
        elif target==nums[-1]:return len(nums)-1
        elif target>nums[-1]:return len(nums)
        left,right = 0,len(nums)-1
        mid = left+(right-left)//2
        while nums[mid]!=target:
            if nums[mid]<target<nums[mid+1]:return mid+1
            elif nums[mid-1]<target<nums[mid]:return mid
            elif nums[mid]<target: left = mid
            elif nums[mid]>target: right = mid
            mid = left+(right-left)//2
        return mid


def test(data_test):
    s = Solution()
    return s.searchInsert(*data_test)


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
