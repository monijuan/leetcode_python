# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 16:50
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 2834. 找出美丽数组的最小和.py
# @Software: PyCharm
# ===================================
"""给你两个正整数：n 和 target 。

如果数组 nums 满足下述条件，则称其为 美丽数组 。

nums.length == n.
nums 由两两互不相同的正整数组成。
在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。
返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 109 + 7。



示例 1：

输入：n = 2, target = 3
输出：4
解释：nums = [1,3] 是美丽数组。
- nums 的长度为 n = 2 。
- nums 由两两互不相同的正整数组成。
- 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
可以证明 4 是符合条件的美丽数组所可能具备的最小和。
示例 2：

输入：n = 3, target = 3
输出：8
解释：
nums = [1,3,4] 是美丽数组。
- nums 的长度为 n = 3 。
- nums 由两两互不相同的正整数组成。
- 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
可以证明 8 是符合条件的美丽数组所可能具备的最小和。
示例 3：

输入：n = 1, target = 1
输出：1
解释：nums = [1] 是美丽数组。


提示：

1 <= n <= 109
1 <= target <= 109
"""
from leetcode_python.utils import *


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        m = target // 2
        if n < m:
            # res = 1 + 2 + ... + n
            res = n * (n + 1) // 2
        else:
            # res = 1 + 2 + ... + m + t + t+1 + .. t+n-m-1
            res = m * (m + 1) // 2 + (target * 2 + n - m - 1) * (n - m) // 2
        return res % (10**9+7)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.minimumPossibleSum(*data)


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
        [2, 3],
        [3, 3],
        [20000, 30000000],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
