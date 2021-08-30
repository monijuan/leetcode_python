# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 19:56
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : Offer_day08_10- I. 斐波那契数列.py
# @Software: PyCharm
# ===================================
"""写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List

class Solution:
    def __init__(self):
        pass

    def fib(self, n: int) -> int:
        if n==0:return 0
        elif n==1:return 1
        else:
            f_1 = 1
            f_2 = 0
            for i in range(2,n+1):
                f_i = f_2 + f_1
                f_2 = f_1
                f_1 = f_i

            return f_i%1000000007


def test(data_test):
    s = Solution()
    return s.fib(*data_test)

if __name__ == '__main__':
    datas = [
        [0],
        [1],
        [2],
        [3],
        [5],
        [1005],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')