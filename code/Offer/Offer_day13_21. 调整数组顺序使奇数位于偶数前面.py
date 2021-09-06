# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 13:55
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day13_21. 调整数组顺序使奇数位于偶数前面.py
# @Software: PyCharm
# ===================================
"""输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

0 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def exchange(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1
        while left<right:
            while left<len(nums) and nums[left]&1: left+=1
            while right>0 and nums[right]&1==0: right-=1
            if left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        return nums


def test(data_test):
    s = Solution()
    return s.exchange(*data_test)


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
        [[1,2,3,4]],
        [[1,3,4]],
        [[]],
        [[5,51,65,48,3,13,35,4,8,79,4,5,1312,2,15,136,5465,132,13,103]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
