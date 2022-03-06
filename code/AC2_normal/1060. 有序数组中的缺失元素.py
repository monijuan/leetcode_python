# -*- coding: utf-8 -*-
# @Time    : 2022/3/2 19:00
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1060. 有序数组中的缺失元素.py
# @Software: PyCharm 
# ===================================
"""现有一个按 升序 排列的整数数组 nums ，其中每个数字都 互不相同 。

给你一个整数 k ，请你找出并返回从数组最左边开始的第 k 个缺失数字。

 

示例 1：

输入：nums = [4,7,9,10], k = 1
输出：5
解释：第一个缺失数字为 5 。
示例 2：

输入：nums = [4,7,9,10], k = 3
输出：8
解释：缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。
示例 3：

输入：nums = [1,2,4], k = 3
输出：6
解释：缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。
 

提示：

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums 按 升序 排列，其中所有元素 互不相同 。
1 <= k <= 108
 

进阶：你可以设计一个对数时间复杂度（即，O(log(n))）的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            loss = nums[i] - nums[i-1] - 1
            if loss >= k:
                return nums[i-1] + k
            else:
                k -= loss
        return nums[n-1] + k


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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

