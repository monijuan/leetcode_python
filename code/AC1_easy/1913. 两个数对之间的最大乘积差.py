# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 15:52
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1913. 两个数对之间的最大乘积差.py
# @Software: PyCharm
# ===================================
"""两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。

例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。

返回以这种方式取得的乘积差中的 最大值 。


示例 1：

输入：nums = [5,6,2,7,4]
输出：34
解释：可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
乘积差是 (6 * 7) - (2 * 4) = 34
示例 2：

输入：nums = [4,2,5,9,7,4,8]
输出：64
解释：可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4)
乘积差是 (9 * 8) - (2 * 4) = 64
 
提示：

4 <= nums.length <= 104
1 <= nums[i] <= 104
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def maxProductDifference_152ms(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2]-nums[0]*nums[1]

    def maxProductDifference_144ms(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        return nums_sorted[-1]*nums_sorted[-2]-nums_sorted[0]*nums_sorted[1]

    def maxProductDifference_184ms(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        min_1,min_2=nums_sorted[:2]
        max_1,max_2=nums_sorted[-2:]
        return max_1*max_2-min_1*min_2

def test(data_test):
    s = Solution()
    return s.maxProductDifference(*data_test)


if __name__ == '__main__':
    datas = [
        [[5,6,2,7,4]],  # 34
        [[4,2,5,9,7,4,8]],  # 64
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
