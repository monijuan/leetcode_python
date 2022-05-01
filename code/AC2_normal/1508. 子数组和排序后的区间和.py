# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 14:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1508. 子数组和排序后的区间和.py
# @Software: PyCharm 
# ===================================
"""给你一个数组 nums ，它包含 n 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 n * (n + 1) / 2 个数字的数组。

请你返回在新数组中下标为 left 到 right （下标从 1 开始）的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

 

示例 1：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 5
输出：13
解释：所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。
示例 2：

输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
输出：6
解释：给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和为 3 + 3 = 6 。
示例 3：

输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50
 

提示：

1 <= nums.length <= 10^3
nums.length == n
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-of-sorted-subarray-sums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

M = 10**9 + 7
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = [(total, index) for index, total in enumerate(nums)]
        heapq.heapify(pq)
        res = 0
        for k in range(1, right + 1):
            total, index = heapq.heappop(pq)
            if k >= left:
                res += total % M
            if index + 1 < n:
                heapq.heappush(pq, (total + nums[index + 1], index + 1))
        return res % M



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
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
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
