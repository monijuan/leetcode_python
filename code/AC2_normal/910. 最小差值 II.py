# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 9:47
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 910. 最小差值 II.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 nums，和一个整数 k 。

对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。

nums 的 分数 是 nums 中最大元素和最小元素的差值。

在更改每个下标对应的值之后，返回 nums 的最小 分数 。

 

示例 1：

输入：nums = [1], k = 0
输出：0
解释：分数 = max(nums) - min(nums) = 1 - 1 = 0 。
示例 2：

输入：nums = [0,10], k = 2
输出：6
解释：将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。
示例 3：

输入：nums = [1,3,6], k = 3
输出：3
解释：将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。
 

提示：

1 <= nums.length <= 104
0 <= nums[i] <= 104
0 <= k <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution():
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi, ma = nums[0], nums[-1]
        ans = ma - mi
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            ans = min(ans, max(ma-k, a+k) - min(mi+k, b-k))
        return ans


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
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
