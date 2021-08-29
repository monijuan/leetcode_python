# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 16:02
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 029. 两数相除.py
# @Software: PyCharm
# ===================================
"""给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2**31 and divisor==-1:return 2**31-1
        #如果有负数则都变为正数，并且记录一下结果要变号
        change_res = False
        if dividend < 0 and divisor > 0:
            change_res = True
            dividend = -dividend
        elif dividend>0 and divisor<0:
            change_res = True
            divisor = -divisor
        elif dividend < 0 and divisor<0:
            dividend = -dividend
            divisor = -divisor

        res = 0
        while dividend>=divisor:
            times = 1
            divisor_temp = divisor
            while dividend>=divisor_temp:
                res+=times
                dividend-=divisor_temp
                divisor_temp+=divisor_temp  # 相当于每次除数double
                times+=times

        if change_res:res = -res
        return res


def test(data_test):
    s = Solution()
    return s.divide(*data_test)


if __name__ == '__main__':
    datas = [
        # [10,3],#3
        # [7,-3],#-2
        [2**31-1,10],
        [2**31-1,1],
        # [-2**31,10],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
