# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 14:28
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 908. 最小差值 I.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 nums，和一个整数 k 。

在一个操作中，您可以选择 0 <= i < nums.length 的任何索引 i 。将 nums[i] 改为 nums[i] + x ，其中 x 是一个范围为 [-k, k] 的整数。对于每个索引 i ，最多 只能 应用 一次 此操作。

nums 的 分数 是 nums 中最大和最小元素的差值。 

在对  nums 中的每个索引最多应用一次上述操作后，返回 nums 的最低 分数 。

 

示例 1：

输入：nums = [1], k = 0
输出：0
解释：分数是 max(nums) - min(nums) = 1 - 1 = 0。
示例 2：

输入：nums = [0,10], k = 2
输出：6
解释：将 nums 改为 [2,8]。分数是 max(nums) - min(nums) = 8 - 2 = 6。
示例 3：

输入：nums = [1,3,6], k = 3
输出：0
解释：将 nums 改为 [4,4,4]。分数是 max(nums) - min(nums) = 4 - 4 = 0。
 

提示：

1 <= nums.length <= 104
0 <= nums[i] <= 104
0 <= k <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0,max(nums)-min(nums)-2*k)


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
