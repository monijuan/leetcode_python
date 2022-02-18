# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 16:38
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 2170. 使数组变成交替数组的最少操作数.py
# @Software: PyCharm
# ===================================
"""给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。

如果满足下述条件，则数组 nums 是一个 交替数组 ：

nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。

返回使数组变成交替数组的 最少操作数 。

 

示例 1：

输入：nums = [3,1,3,2,4,3]
输出：3
解释：
使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,1,3,1] 。
在这种情况下，操作数为 3 。
可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。
示例 2：

输入：nums = [1,2,2,2,2]
输出：2
解释：
使数组变成交替数组的方法之一是将该数组转换为 [1,2,1,2,1].
在这种情况下，操作数为 2 。
注意，数组不能转换成 [2,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-alternating
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c1 = Counter(nums[::2]).most_common()
        c2 = Counter(nums[1::2]).most_common()
        cand1, cand1Count = c1[0] if c1 else (0, 0)
        cand2, cand2Count = c1[1] if len(c1) > 1 else (0, 0)
        cand3, cand3Count = c2[0] if c2 else (0, 0)
        cand4, cand4Count = c2[1] if len(c2) > 1 else (0, 0)
        if cand1 != cand3:
            return n - cand1Count - cand3Count
        else:
            return min(n - cand2Count - cand3Count, n - cand1Count - cand4Count)



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
