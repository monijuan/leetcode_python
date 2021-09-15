# -*- coding: utf-8 -*-
# @Time    : 2021/9/15 13:24
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day22_56 - I. 数组中数字出现的次数.py
# @Software: PyCharm
# ===================================
"""一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

import functools

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """
        ret ：所有数字进行“异或”操作之后的结果
            因为出现过两次的数字异或操作就抵消了，所以ret保留的是最后ab两个数异或的结果
        div ：是ret用二进制表示时候第一个为1的数字的十进制数
            如果是0，可能a和b这一位都没有数字或都有数字，那就无法区分ab了，
            如果是1，就表明a和b在这一位只有一个1，另一个是0，异或才会是1
        所有数根据div位是否有数来异或，这样相同的数两两抵消，不相同的数会被分为a和b
        """
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


def test(data_test):
    s = Solution()
    return s.singleNumbers(*data_test)


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
        [[1,2,10,4,1,4,3,3]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
