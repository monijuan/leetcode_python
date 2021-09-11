# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 20:18
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 198. 打家劫舍.py
# @Software: PyCharm 
# ===================================
"""你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        dp_0 = nums[0]
        dp_1 = nums[1]
        for i in range(2,len(nums)):
            dp_0,dp_1 = max(dp_0,dp_1),dp_0+nums[i]
        return max(dp_0,dp_1)


    def rob_改进前(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        dp = [[0,0,0]for _ in range(len(nums))] # 左边偷了，左边一个没偷，左边两个没偷
        dp[0] = [0,nums[0],nums[0]]
        dp[1] = [nums[0],nums[1],max(nums[0:2])]
        for i in range(2,len(nums)):
            dp[i] = [max(dp[i-1][1:3]),dp[i-1][0]+nums[i],dp[i-2][0]+nums[i]]
        # print(dp)
        return max(dp[-1])


def test(data_test):
    s = Solution()
    return s.rob(*data_test)
def rob_改进前(data_test):
    s = Solution()
    return s.rob_改进前(*data_test)


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
        # [[9,1,6,9,8]],
        [[2,7,9,3,1]],
        [[1,2,3,1]],
        [randListInt(1,100,20)]
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output[test]:', test(data_test))
        print('output[true]:', rob_改进前(data_test))
        print(f'use time:{time.time() - t0}s')