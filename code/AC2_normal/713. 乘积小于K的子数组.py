# -*- coding: utf-8 -*-
# @Time    : 2021/12/13 10:06
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 713. 乘积小于K的子数组.py
# @Software: PyCharm
# ===================================
"""给定一个正整数数组 nums和整数 k 。

请找出该数组内乘积小于 k 的连续的子数组的个数。

 

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
示例 2:

输入: nums = [1,2,3], k = 0
输出: 0
 

提示: 

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        product,left,res = 1,0,0
        for right in range(length):
            product*=nums[right]
            while product>=k and left<right:
                product//=nums[left]
                left+=1
            # print(left, right, product, right - left +1)
            if product<k: res+=(right - left + 1)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.numSubarrayProductLessThanK(*data)


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
        [[10,5,2,6],100],
        # [[57,44,92,28,66,60,37,33,52,38,29,76,8,75,22],18],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

    # print(randListInt(0,100,100))
