# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 15:26
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 046. 全排列.py
# @Software: PyCharm
# ===================================
"""给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        self.res = []

    def dfs(self,nums_now:List[int]):
        if len(nums_now)==self.length:
            self.res.append(nums_now.copy())
        else:
            for num in self.nums:
                if num not in nums_now:
                    nums_now.append(num)
                    self.dfs(nums_now)
                    nums_now.remove(num)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        self.nums = nums
        self.dfs([])
        return self.res


def test(data_test):
    s = Solution()
    return s.permute(*data_test)


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
