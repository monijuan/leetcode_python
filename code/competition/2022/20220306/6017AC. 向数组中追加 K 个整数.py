# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6017AC. 向数组中追加 K 个整数.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。

返回追加到 nums 中的 k 个整数之和。



示例 1：

输入：nums = [1,4,25,10,25], k = 2
输出：5
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。
示例 2：

输入：nums = [5,6], k = 6
输出：25
解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。


提示：

1 <= nums.length <= 105
1 <= nums[i], k <= 109
"""
from leetcode_python.utils import *


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.append(0)
        nums.sort()
        res = 0
        for i,n in enumerate(nums):
            if i==len(nums)-1:
                l,r = n+1,10**11
            else:
                l,r = n+1,nums[i+1]
            # print(l,r,r-l,k,res)
            size = r-l
            if size>=k:
                # print(range(l,l+k),res)
                res+=((l+l+k-1)*k//2)
                return res
            elif size>0:
                res+=((l+r-1)*(r-l)//2)
                # res+=sum(range(l,r))
                k-=size

    def minimalKSum_wtl(self, nums: List[int], k: int) -> int:
        new = set()
        idx = 1
        numsset = set(nums)
        while len(new)<k:
            while idx in numsset:idx+=1
            new.add(idx)
            idx+=1
        # print(nums,new)
        print(new)
        return sum(new)



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    # return s.minimalKSum_wtl(*data)
    return s.minimalKSum(*data)


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
        [[1,4,25,10,25],2],
        [[53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83],76],
        [[1],1000000000],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

