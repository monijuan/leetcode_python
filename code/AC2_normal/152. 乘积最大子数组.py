# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 10:35
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 152. 乘积最大子数组.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。~
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def maxProduct(self, nums: List[int]) -> int:
        max_save,min_save,max_all =nums[0],nums[0],nums[0]
        for i,num in enumerate(nums):
            if i==0:continue
            max_save,min_save = max(max(max_save*num,num),min_save*num),min(min(max_save*num,num),min_save*num)
        return max(max_all,max_save)


def test(data_test):
    s = Solution()
    return s.maxProduct(*data_test)


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
        [[2,3,0,-1,5,-2,4]],
        [[2,3,0,5,-2,4,9]],
        # [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')