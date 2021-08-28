# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 20:09
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : Offer_day99_10- II. 青蛙跳台阶问题.py
# @Software: PyCharm
# ===================================
"""一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List

class Solution:
    def __init__(self):
        pass

    def numWays(self, n: int) -> int:
        n_2 = 0
        n_1 = 1
        for _ in range(n):
            n_1, n_2 = n_1+n_2, n_1
        return n_1 % 1000000007


def test(data_test):
    s = Solution()
    return s.numWays(*data_test)

if __name__ == '__main__':
    datas = [
        [0],
        [1],
        [2],
        [3],
        [13],
        [113],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')