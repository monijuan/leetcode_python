# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 15:36
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 归并排序.py
# @Software: PyCharm
# ===================================
"""
"""
from leetcode_python.utils import *


class 归并排序:
    def merge(self,left_list: List[int],right_list: List[int]) -> List[int]:
        res = []
        left_length,right_length = len(left_list),len(right_list)
        left_index,right_index=0,0
        while left_index<left_length and right_index<right_length:
            if left_list[left_index]<=right_list[right_index]:
                res.append(left_list[left_index])
                left_index+=1
            else:
                res.append(right_list[right_index])
                right_index+=1
        if left_index<left_length:
            res.extend(left_list[left_index:])
        if right_index<right_length:
            res.extend(right_list[right_index:])
        return res

    def sort(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length<=1:return nums
        mid = length//2
        left_list = self.sort(nums[:mid])
        right_list = self.sort(nums[mid:])
        res = self.merge(left_list,right_list)
        return res


def test(data_test):
    s = 归并排序()
    return s.sort(*data_test)

if __name__ == '__main__':
    datas = [
        [[7,5,6,4,41,654,3,9,12,3,54,6,486,3,413,85]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
