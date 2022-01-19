# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 8:44
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 219. 存在重复元素 II.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
 

 

提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        for i in range(length):
            # print(i,nums[i],nums[i+1:min(length,i+k+1)])
            if nums[i] in nums[i+1:min(length,i+k+1)]:
                return True
        return False


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.containsNearbyDuplicate(*data)


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
        [[1,2,3,1],3],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
