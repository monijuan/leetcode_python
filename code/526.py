# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 14:01
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 526.py
# @Software: PyCharm
# ===================================
"""假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

第 i 位的数字能被 i 整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

示例1:

输入: 2
输出: 2
解释:

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
说明:

N 是一个正整数，并且不会超过15。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def countArrangement(self, n: int) -> int:
        num_all = set(range(1,n+1))
        def dfs(index,num_remain):
            if index==n:
                last_num = num_remain.pop()
                return 1 if (last_num%index==0 or index%last_num==0) else 0
            res_this_route = 0
            for num_next in num_remain:
                if num_next%index==0 or index%num_next==0:
                    next_num_remain = num_remain.copy()
                    next_num_remain.remove(num_next)
                    res_this_route += dfs(index+1,next_num_remain)
            return res_this_route

        return dfs(1,num_all)


def test(data_test):
    s = Solution()
    return s.countArrangement(data_test)


if __name__ == '__main__':
    datas = range(16)
    # datas = [4]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
