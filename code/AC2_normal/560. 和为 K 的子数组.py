# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 15:40
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 560. 和为 K 的子数组.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        超时case：https://leetcode-cn.com/submissions/detail/240804073/testcase/
        """
        pass

    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cnt_save = {}
        sum_temp = 0
        for num in nums:
            sum_temp+=num
            res += cnt_save.get(sum_temp-k,0)
            cnt_save[sum_temp] = cnt_save.get(sum_temp,0)+1
            if sum_temp==k:res+=1
        return res

    def subarraySum_超时(self, nums: List[int], k: int) -> int:
        res = 0
        length = len(nums)
        for start in range(length):
            sum_temp = 0
            for end in range(start,length):
                sum_temp+=nums[end]
                if k==sum_temp:res+=1
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.subarraySum(*data)


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
        [[1,2,3],3],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')