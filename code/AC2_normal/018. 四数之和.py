# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 8:58
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 018. 四数之和.py
# @Software: PyCharm
# ===================================
"""给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        if length<4:return []
        res = []
        nums.sort()
        for ia,numa in enumerate(nums[:-3]):
            if ia>0 and numa==nums[ia-1]:continue
            for id in range(length-1,ia+2,-1):
                if id<length-1 and nums[id]==nums[id+1]:continue
                numd = nums[id]
                ib,ic = ia+1,id-1
                while ib<ic:
                    sum_temp = numa+nums[ib]+nums[ic]+numd
                    if sum_temp == target:
                        res.append([numa,nums[ib],nums[ic],numd])
                        while ib<ic and nums[ib]==nums[ib+1]:ib+=1
                        while ib<ic and nums[ic]==nums[ic-1]:ic-=1
                        ib+=1
                        ic-=1
                    elif sum_temp>target:
                        ic-=1
                    else:
                        ib+=1
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.fourSum(*data)


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
