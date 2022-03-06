# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 16:31
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1063. 有效子数组的数目.py
# @Software: PyCharm
# ===================================
"""给定一个整数数组 nums ，返回满足下面条件的 非空、连续 子数组的数目：

子数组 是数组的 连续 部分。
子数组最左边的元素不大于子数组中的其他元素 。
 

示例 1：

输入：nums = [1,4,2,5,3]
输出：11
解释：有 11 个有效子数组，分别是：[1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3] 。
示例 2：

输入：nums = [3,2,1]
输出：3
解释：有 3 个有效子数组，分别是：[3],[2],[1] 。
示例 3：

输入：nums = [2,2,2]
输出：6
解释：有 6 个有效子数组，分别为是：[2],[2],[2],[2,2],[2,2],[2,2,2] 。
 

提示：

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-valid-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        queue = []
        res = 0
        for x in nums:
            while queue and queue[-1]>x:queue.pop(-1)
            queue.append(x)
            res+=len(queue)
        return res


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
