# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 8:49
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 371. 两整数之和.py
# @Software: PyCharm
# ===================================
"""给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。

 

示例 1：

输入：a = 1, b = 2
输出：3
示例 2：

输入：a = 2, b = 3
输出：5
 

提示：

-1000 <= a, b <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def getSum(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        a &= x
        b &= x
        while b != 0:
            carry = (a & b) << 1 & x
            a ^= b
            b = carry
        return a if a<=0x7fffffff else ~(a^x)


def test(data_test):
    s = Solution()
    return s.getSum(*data_test)


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
