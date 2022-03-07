# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 15:47
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 976. 三角形的最大周长.py
# @Software: PyCharm
# ===================================
"""给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。

 

示例 1：

输入：nums = [2,1,2]
输出：5
示例 2：

输入：nums = [1,2,1]
输出：0
 

提示：

3 <= nums.length <= 104
1 <= nums[i] <= 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-perimeter-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:-x)
        l = len(nums)
        i = 0
        while i<l-2 and nums[i]>=nums[i+1]+nums[i+2]:i+=1
        return 0 if i==l-2 else sum(nums[i:i+3])


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
